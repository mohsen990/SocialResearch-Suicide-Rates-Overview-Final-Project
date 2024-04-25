import streamlit as st
# Design main page with basic features of stream library


st.header('Suicide Rates Overview 1985 to 2016')


st.image('https://english.mathrubhumi.com/image/contentid/policy:1.9160079:1702711234/uyf%20(1).jpg?$p=98c1d33&f=16x10&w=852&q=0.8', width=400)
st.write("____________________________________________________________")
st.subheader('Introduction:')
st.markdown('''
            The dataset comprises annual suicide counts in a specific country, categorized by gender and age groups, alongside the total population within each group. This setup enables the calculation of crude rates per 100,000 individuals.

            While employing rates may seem intuitive since the total number of suicides correlates with population size (larger countries tend to have more suicides), it's less apparent that these rates, also known as crude rates, aren't suitable for cross-country comparisons. 
            Suicide rates vary significantly based on demographic factors. Thus, to assess a country's situation accurately, it's imperative to consider its current demographic makeup. 
            
            Overall, the dataset appears satisfactory, albeit with some missing values. To enhance clarity, I'll perform two transformations to organize and present age categories more effectively.
            ''')