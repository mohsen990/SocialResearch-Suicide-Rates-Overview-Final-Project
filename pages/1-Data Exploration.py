import streamlit as st
from settings import Path , AboutDataSet , KeyFeaturesInDataSet
import GetDataFrame as gf
#-------------------------------------------------------------------------


st.subheader("About Dataset:")
st.markdown( AboutDataSet )

with st.expander("See Key Features:"):
   st.markdown( KeyFeaturesInDataSet )
   

# get orignal Dataset and uncleaned -----------------------------------------

df = gf.GetUncleanData()

# Disply data frame----------------------------------------------------------

st.write('Shape of Dataset:', df.shape)
st.markdown('Dataset Descrition:')
DataSetDescribe = df.describe(include='all')
st.write(DataSetDescribe)

st.subheader("Display Data set: " )
SelectedItem = st.selectbox("Select number of rows to show: " , ["select number","10","100","1000","All"])
if SelectedItem == "10":
   st.write(df.head(10))
elif SelectedItem == "100":
   st.write(df.head(100))
elif SelectedItem == "1000":
   st.write(df.head(1000))
elif SelectedItem == "All":
    st.write(df)
else:
   st.write(df.head())


# Data Cleaning ------------------------------------------------------------

st.subheader('Data Cleaning:')
st.write('''
            Data cleaning includes data casting , converting into integer in some columns,
            ,extracting numbers from strings, removing rows with low number of null values
            and replacing null cells with mean of value in cloumns with large number of null values.
         ''')

# display count of null valuses in each column
sumNa = df.isna().sum()
with st.expander("Show number of null values in each columns before cleaning"):
     strs = ""
     for item in sumNa.index:
         strs = strs +'\t\t' +item + ' : :red[' + str(sumNa[item]) +']'
     st.write(strs)

# get Clean Datafarme and check null values-----------------------------------
CleanDataFrame = gf.GetCleanData()
sumNa = CleanDataFrame.isna().sum()
with st.expander("Show number of null values in each columns after cleaning"):
     strs = ""
     for item in sumNa.index:
         strs = strs +'\t\t' +item + ' : :red[' + str(sumNa[item]) +']'
     st.write(strs)

     
#Filter Data to dispaly---------------------------------------------------------
CleanDataFrame['Year'] = CleanDataFrame['Year'].astype(str)   

ListOfBrands = ["Select Brand"]
ListOfBrands.extend(CleanDataFrame.Brand.drop_duplicates().tolist())
SelectedBrand = st.selectbox("Filter By Brand" ,ListOfBrands )
if SelectedBrand == "Select Brand":
    FiltterdDf = ""
else:
   FiltterdDf =  CleanDataFrame[ CleanDataFrame.Brand == SelectedBrand ]
st.write(FiltterdDf)


ListOfBody = ["Select BodyType"]
ListOfBody.extend(CleanDataFrame.BodyType.drop_duplicates().tolist())
SelectedBody = st.selectbox("Filter By Body Type" ,ListOfBody )
if SelectedBody == "Select BodyType":
    FiltterdDf2 = ""
else:
   FiltterdDf2 =  CleanDataFrame[ CleanDataFrame.BodyType == SelectedBody ]
st.write(FiltterdDf2)

#-- Group by ------------------------------------------------------------------------------
st.subheader('Group By Features')
st.write('Group by with Brand and Model:')
df_gr1 = CleanDataFrame.groupby(['Brand','Model'])
st.write(df_gr1.first())

st.write('Total Price based on brand, model and type:')
df_gr2 = CleanDataFrame.groupby(['Brand','Model','BodyType'])['Price'].sum()
st.write(df_gr2)