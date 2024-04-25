import pandas as pd
import streamlit as st
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