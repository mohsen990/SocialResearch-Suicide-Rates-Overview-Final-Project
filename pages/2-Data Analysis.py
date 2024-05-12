import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go
import plotly.express as px
import cufflinks as cf
from plotly.offline import iplot,init_notebook_mode
from collections import Counter
from plotly.subplots import make_subplots

from settings import Path


datafarme = pd.read_csv(Path)

# Number of suicide committed in each country
st.subheader('Number of suicide committed in the top 25 countries')
suicide_in_countries = datafarme.groupby('country')
country_suicide_series = suicide_in_countries['suicides_no'].sum().sort_values().tail(25)

country_suicide_Figure = plt.figure(figsize=(15,8))
colors = ['#1b9e77', '#a9f971', '#fdaa48','#6890F0','#A890F0']
plt.bar(country_suicide_series.index, country_suicide_series.values, color = colors )
plt.ylim(0,1300000)
plt.xticks(rotation=90 ,ha='right')
plt.xlabel('Countries')
plt.ylabel('Number of suicide')
st.pyplot(country_suicide_Figure)


# Group the data by country and calculate the average suicide rate
avg_suicide_rate_by_country = datafarme.groupby('country')['suicides/100k pop'].mean().reset_index()

# Create an interactive bar plot with red bars
fig = px.bar(
    avg_suicide_rate_by_country,
    x='country',
    y='suicides/100k pop',
    title='Average Suicide Rate by Country',
    labels={'country': 'Country', 'suicides/100k pop': 'Average Suicide Rate'},
)

# Customize the appearance to set the bars' color to red (optional)
fig.update_traces(marker_color='blue', marker_line_color='grey', marker_line_width=1)

# Add interactivity (hover text)
fig.update_traces(texttemplate='%{y}', textposition='outside')

# Set axis labels
fig.update_xaxes(title_text='Country')
fig.update_yaxes(title_text='Average Suicide Rate')

# Show the interactive plot
st.plotly_chart(fig)

# Number of suicides genderwise---------------------------------------------------------------------
st.subheader('Number of suicides genderwise')
genderwise_suicide = datafarme.groupby('sex')
genderwise_suicide_series = genderwise_suicide['suicides_no'].sum()
genderwise_suicide_Figure = plt.figure(figsize=(8,4))
colors = ['pink','skyblue']
plt.bar(genderwise_suicide_series.index, genderwise_suicide_series.values, color = colors )
plt.xticks(rotation=90 ,ha='right')
plt.xlabel('Gender')
plt.ylabel('Number of suicide')
st.pyplot(genderwise_suicide_Figure)

# Suicides number by year -------------------------------------------------------------------------

st.subheader('Suicides Number By Year')
year_suicide = datafarme.groupby('year')
year_suicide_series = year_suicide['suicides_no'].sum()
year_suicide_Figure = plt.figure(figsize=(15,7))
colors = ['#A52A2A', '#B22222', '#DC143C', '#FF0000', '#FF6347', '#FF7F50', '#CD5C5C', '#F08080', '#E9967A', '#FA8072', '#FFA07A', '#FF4500','#FF8C00']
plt.bar(year_suicide_series.index, year_suicide_series.values, color = colors )
plt.xticks(rotation=90 ,ha='right')
plt.xlabel('Year')
plt.ylabel('Number of suicide')
st.pyplot(year_suicide_Figure)


fig = plt.figure(figsize = (12, 6))
sns.set_style('white')

# set colors
my_palette = sns.cubehelix_palette(n_colors = 7, start=.46, rot=-.45, dark = .2, hue=0.95)
color = my_palette[4]
plt.plot( year_suicide_series.index,year_suicide_series.values, color = color)
plt.title('', fontsize = 14, fontweight = 'bold')
plt.xlabel('Year')
plt.ylabel('Number of suicide')
sns.despine()
st.pyplot(fig)


#Suicides Number Over the time-----------------------------------------------------------------
st.subheader('Suicides Number Over the time')
fig = px.choropleth(datafarme, locations='country',
                   locationmode='country names',color=np.log(datafarme['suicides_no']),
                   animation_frame=datafarme['year'],
                   title='Suicides Number over the Time',color_continuous_scale='matter') #px.colors.sequential.matter

st.plotly_chart(fig)

#---------------------------------------------------------------------------------------------

st.subheader('Exploring the trend of overall suicides through the years')
overall     = pd.DataFrame(datafarme.groupby('year')['suicides_no'].sum())
pop_overall = pd.DataFrame(datafarme.groupby('year')['population'].sum())

fig = make_subplots(rows = 2, cols=1)

fig.append_trace(go.Scatter(
                            x = overall.index,
                            y = overall['suicides_no'],
                            name = 'Number of Suicies',
                            mode = 'lines+markers',
                            marker=dict(color="red")
                            ), row=1, col=1)

fig.append_trace(go.Scatter(
                            x = pop_overall.index,
                            y = pop_overall['population'],
                            name = 'Population',
                            mode = 'lines+markers',
                            marker=dict(color="#00CC96")
                            ), row=2, col=1)


fig.update_layout(height=600, width=800, title = 'Population V/S Total Suicides Trend')
fig.update_xaxes(title_text = 'Year', row=1, col=1)
fig.update_xaxes(title_text = 'Year', row=2, col=1)
fig.update_yaxes(title_text='Suicides', row=1, col=1)
fig.update_yaxes(title_text='Population', row=2, col=1)

st.plotly_chart(fig)

#-----------------------------------------------------------------------------------
st.subheader('Male v/s Female suicide proportion through the years')

total_gender = datafarme[['sex', 'suicides_no', 'population', 'year', 'country']]
total_gender['proportion'] = total_gender.suicides_no / total_gender.population
gender_prop = pd.DataFrame(total_gender.groupby(['year', 'sex'])['proportion'].mean()).unstack()

fig = go.Figure()
fig.add_trace(go.Scatter(x= gender_prop.index,
                         y = gender_prop.proportion.male,
                         mode = 'lines+markers',
                         name = 'Male death proportion',
                         marker = dict(color='#FF9900')))

fig.add_trace(go.Scatter(x= gender_prop.index,
                         y = gender_prop.proportion.female,
                         mode = 'lines+markers',
                         name = 'Female death proportion',
                         marker = dict(color='rgb(179,222,105)')))

fig.update_layout(height=600, width=800,
                  title = 'Male v/s Female suicide proportion through the years',
                  font = dict(color="Brown"))

fig.update_xaxes(title_text = 'Year', color="RebeccaPurple")
fig.update_yaxes(title_text = 'Proportion', color="RebeccaPurple")

st.plotly_chart(fig)

#-----------------------------------------------------------------------------------
st.subheader('Suicides in gender by different Age group')
gender_age = pd.DataFrame(datafarme.groupby(['age', 'sex'])[ 'suicides_no'].sum()).reset_index()
age_order = ['5-14 years','15-24 years','25-34 years','35-54 years','55-74 years','75+ years']

fig = px.bar(gender_age,
             x = gender_age.age,
             y = gender_age.suicides_no,
             color = 'sex',
             pattern_shape = 'sex',
             pattern_shape_sequence = ['x',''],
             text = gender_age.suicides_no,
             color_discrete_map={'female':'#4C78A8', 'male':'#FFA15A'}
             )

fig.update_layout(height=500, width=800,
                  title = 'Suicides in gender by different Age group',
                  font = dict(color = 'RebeccaPurple')
                  )

fig.update_xaxes(categoryorder='array', categoryarray= age_order, title_text = 'Age Group')
fig.update_yaxes(title_text = 'Suicides (In millions)')

st.plotly_chart(fig)


# Group the data by age group and calculate the total number of suicides
suicides_by_age = datafarme.groupby('age')['suicides_no'].sum().reset_index()

# Create an interactive bar plot with red bars
fig = px.bar(
    suicides_by_age,
    x='age',
    y='suicides_no',
    title='Suicides by Age Group',
    labels={'age': 'Age Group', 'suicides_no': 'Total Suicides'},
)

# Customize the appearance to set the bars' color to red (optional)
fig.update_traces(marker_color='lightblue', marker_line_color='black', marker_line_width=1)

# Add interactivity (hover text)
fig.update_traces(texttemplate='%{y}', textposition='outside')

# Set axis labels
fig.update_xaxes(title_text='Age Group')
fig.update_yaxes(title_text='Total Suicides')

# Show the interactive plot
st.plotly_chart(fig)

#------------------------------------------------------------------------------

# Suicides by country
st.subheader('Suicide in different generations')
Generation = pd.DataFrame(
                       datafarme.groupby('generation')['suicides_no']\
                       .sum()\
                       .reset_index().\
                       sort_values('suicides_no', ascending=False)[:20]
                       )

fig = px.pie(
            Generation,
            values = 'suicides_no',
            names = 'generation',
            title = 'Suicides and its Proportion in different generations'
            )

fig.update_layout(height=600, width=800)
fig.update_traces(textposition='outside', textinfo='percent+label')
st.plotly_chart(fig)

#------------------------------------------------------------------------------------
st.subheader('')
st.write()
total_gender = datafarme[['sex', 'suicides_no', 'population', 'year', 'country', ' gdp_for_year ($) ']]
total_gender['proportion'] = total_gender.suicides_no / total_gender.population
gdp_max = total_gender[total_gender.year == 2015]\
                      .groupby('country')[[' gdp_for_year ($) ', 'proportion']]\
                      .agg({' gdp_for_year ($) ' : 'max', 'proportion' : 'mean'})\
                      .reset_index()

fig = go.Figure()

fig.add_trace(go.Scatter(y= gdp_max.proportion,
                         x = gdp_max[' gdp_for_year ($) '],
                         mode = 'markers+lines',
                         name = 'Male death proportion',
                         marker = dict(color='#17BECF')))


fig.update_layout(height=600, width=800,
                  title = 'GDPs in 1999 v/s Mean suicide proportion',
                  font = dict(color="#FF7F0E"))

fig.update_xaxes(title_text = 'GDP (1995)', tickangle=45)
fig.update_yaxes(title_text = 'Suicide Proportion')

st.plotly_chart(fig)


#-------------------------------------------------------------------------
shortenSR= datafarme.head(1200)
sizes = shortenSR['population'] / 10000
fig = plt.figure(figsize=(10, 8))
plt.scatter(x='gdp_per_capita ($)', y='suicides/100k pop', data=shortenSR, s=sizes, c='suicides/100k pop', cmap='viridis', alpha=0.7,edgecolors='black')
plt.title('Suicide rates vs. GDP per Capita')
plt.xlabel('GDP per Capita $')
plt.ylabel('Suicides per 100k population')
plt.grid()
cbar = plt.colorbar()
cbar.set_label('Suicides/100k pop')
st.pyplot(fig)


#--------------------------------------------------------
# Group the data by 'country' and 'year' to get total suicides and population
grouped_data = datafarme.groupby(['country', 'year'])[['suicides_no', 'population']].sum().reset_index()

# Choose a specific country for prediction (e.g., 'United States')
country_name = 'United States'

# Filter data for the chosen country
country_data = grouped_data[grouped_data['country'] == country_name]

# Create an interactive time series plot with a red line
fig = px.line(
    country_data,
    x='year',
    y='suicides_no',
    title=f'Suicides Over Time in {country_name}',
    labels={'year': 'Year', 'suicides_no': 'Total Suicides'},
    line_shape='linear',  # Choose line shape
    line_dash_sequence=['solid'],  # Choose line style
)

# Customize line color to red
fig.update_traces(line=dict(color='red'))

# Add axis labels
fig.update_xaxes(title_text='Year')
fig.update_yaxes(title_text='Total Suicides')

# Show the interactive plot
st.plotly_chart(fig)