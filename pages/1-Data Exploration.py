import pandas as pd
import io
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from re import sub
from decimal import Decimal

from settings import Path

AboutDataSet = '''
            This compiled dataset pulled from four other datasets linked by time and place, and was built to find signals correlated to
            increased suicide rates among different cohorts globally, across the socio-economic spectrum.
            '''

KeyFeaturesInDataSet = '''
              
            :green[Country:] Country Name
            
            :green[Year:] The year of suicide information collected 
            
            :green[Sex:] The gender of the person who committed suicide 

            :green[Age:] Age category of suicidal person

            :green[suicide NO:] Count of suicides

            :green[Population:] Population of the country in the corresponding year

            :green[suicide rate:] Suicides per 100000 people 

            :green[country-year:] The Country and Year (key)

            :green[HDI for year:] Human Development Index / per year

            :green[GDP for year:] Gross Domestic Product / per year

            :green[Generation:] generation type baed on 

            '''




st.subheader("About Dataset:")
st.markdown(AboutDataSet)
st.write('________________________________________________________')
st.subheader("KeyFeaturesInDataSet:")
st.markdown(KeyFeaturesInDataSet)
st.write('________________________________________________________')

df = pd.read_csv(Path)
#------------------Dataset info------------------------------------
st.subheader("Dataset Information: " )
buffer = io.StringIO()
df.info(buf=buffer)
s = buffer.getvalue()
st.text(s)
#------------------Dataset Description-----------------------------
st.subheader("Dataset Description: " )
DataSetDescribe = df.describe(include='all')
st.write(DataSetDescribe)

#-----------------Display top 30 records of Dataset----------------
st.write('________________________________________________________')
st.subheader("Display Dataset: " )
st.write('Top 30 recoeds of Dataset')
st.write(df.head(30))
#---------------------------correlation of columns -----------------
st.subheader("Correlation Matrix") 
df_number = df[['year','suicides_no','suicides/100k pop','HDI for year',' gdp_for_year ($) ','gdp_per_capita ($)']]
df_corr = df_number.corr()
heatfig = plt.figure(figsize=(8,6))
sns.heatmap(df_corr , annot=True)
plt.title('correlation', fontsize =14)
st.pyplot(heatfig)