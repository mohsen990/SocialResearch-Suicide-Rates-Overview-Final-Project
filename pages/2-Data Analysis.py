import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import GetDataFrame as gf

#--Get Cleaned Data------------------------------------------------------------
Vehicle_Prices_db = gf.GetCleanData()

#--Histogram with seaborn library----------------------------------------------
st.subheader("Histogram")
st.write('''
           Showing the number of observations in Dataset includes: Years , Price , Seats
           Doors, Fuel Consumption and Kilometres.
         ''')

fig = plt.figure(figsize=(18,12))
SubFig_1 = fig.add_subplot(2,3,1)
sns.histplot(Vehicle_Prices_db[['Year']] , bins=20 , kde=True)
plt.title('Years', fontsize = 16)

SubFig_2 = fig.add_subplot(2,3,2)
sns.histplot(Vehicle_Prices_db[['Price']] , bins=20 , kde=True )
plt.title('Price', fontsize = 16)

SubFig_3 = fig.add_subplot(2,3,3)
sns.histplot(Vehicle_Prices_db[['Seats']] , bins=30 ,kde=True)
plt.title('Seats', fontsize = 16)

SubFig_4 = fig.add_subplot(2,3,4)
sns.histplot(Vehicle_Prices_db[['Doors']] , bins=30 ,kde=True)
plt.title('Doors', fontsize = 16)
plt.suptitle('Histogram of integer columns')

SubFig_5 = fig.add_subplot(2,3,5)
sns.histplot(Vehicle_Prices_db[['FuelConsumption']] , bins=20 ,kde=True )
plt.title('Fuel Consumption', fontsize = 16)


SubFig_6 = fig.add_subplot(2,3,6)
sns.histplot(Vehicle_Prices_db[['Kilometres']] , bins=20 , kde=True )
plt.title('Kilometres', fontsize = 16)
plt.suptitle('Histogram of integer columns', fontsize = 25)

st.pyplot(fig)
st.write("\n____________________________________________________________________")
#--Heat map matrix-----------------------------------------------------------------
# -- corrolatin between columns with integer data type
st.subheader("Correlation Matrix")
st.write('Correlation matrix is simply a table showing the correlation coefficients between variables.')

df_Number = Vehicle_Prices_db[['Year','FuelConsumption','CylindersinEngine','Kilometres','Doors','Seats','Price']]
df_Corr = df_Number.corr()
HeatFig = plt.figure(figsize=(8,6))
sns.heatmap(df_Corr  , annot=True)
plt.title('Correlation', fontsize = 14)

st.pyplot(HeatFig)
st.write("\n____________________________________________________________________")
#--Distribution Of Items ----------------------------------------------------------
st.subheader("Distribution Of Items")
st.write('''Bar graphs show distribution of clomuns includes: transmission, used Or new, doors,
            fuelType, cylinders in engine, body type, brand and location.
         ''')

CountOfTransmission = Vehicle_Prices_db['Transmission'].value_counts()
CountOfUse = Vehicle_Prices_db['UsedOrNew'].value_counts()
CountOfDoors = Vehicle_Prices_db['Doors'].value_counts()
CountOfFuelType = Vehicle_Prices_db['FuelType'].value_counts()
CountOfCylinder = Vehicle_Prices_db['CylindersinEngine'].value_counts()
CountOfBodyType = Vehicle_Prices_db['BodyType'].value_counts()

MainFig = plt.figure(figsize=(8,8) )
SubFig_1 = MainFig.add_subplot(2,2,1)
SubFig_1.bar(CountOfTransmission.index , CountOfTransmission.values, color = 'pink' )
plt.title("Transmission")

SubFig_2 = MainFig.add_subplot(2,2,2)
SubFig_2.bar(CountOfUse.index, CountOfUse.values , color = 'lightgreen')
plt.title("Use Or New Cars")

SubFig_3 = MainFig.add_subplot(2,2,3)
SubFig_3.bar(CountOfFuelType.index , CountOfFuelType.values , color = 'cyan')
plt.xticks(rotation=90 ,ha='right')
plt.title("Fuel Type")

SubFig_4 = MainFig.add_subplot(2,2,4)
SubFig_4.bar(CountOfBodyType.index , CountOfBodyType.values , color = 'magenta')
plt.xticks(rotation=90 , ha='right')
plt.title("Body Type")
plt.suptitle('Distribution Of Items', fontsize = 14)

st.pyplot(MainFig)
st.write("\n____________________________________________________________________")
#---Plot Distribution Of Brands -------------------------------------------------

CountOfBrand = Vehicle_Prices_db['Brand'].value_counts()
BrandFigure = plt.figure(figsize=(12,8))
plt.bar(CountOfBrand.index , CountOfBrand.values , color = 'darkblue')
plt.xticks(rotation=90 ,ha='right')
plt.title('Distribution Of Brands' ,fontsize = 16)
plt.xlabel('Brand' ,fontsize = 12)
plt.ylabel('Count' ,fontsize = 12)

st.pyplot(BrandFigure)

#---Plot Distribution Of Location -------------------------------------------------

CountOfLocation = Vehicle_Prices_db['Location'].value_counts()
LocFigure = plt.figure(figsize=(12,8))
plt.bar(CountOfLocation.head(50).index , CountOfLocation.head(50).values , color = 'darkgreen')
plt.xticks(rotation=90 ,ha='right')
plt.title('Distribution Of Location' ,fontsize = 16)
plt.xlabel('Location' ,fontsize = 12)
plt.ylabel('Count' ,fontsize = 12)

st.pyplot(LocFigure)

st.write("\n____________________________________________________________________")
#--Pie Chart top 5 brands , Cylinders In Engine , DriveType , FuelType--------------
st.subheader("Pie Chart")
st.write("Pie Chart top 5 brands , Cylinders In Engine , DriveType , FuelType.")

Top5Brand = Vehicle_Prices_db['Brand'].value_counts(ascending=True).tail(5)
PieFig = plt.figure(figsize=(8,8))
explode1 = [0, 0, 0, 0 , 0.2]
plt.subplot(2,2,1)
plt.pie(Top5Brand.values , labels= Top5Brand.index ,explode= explode1 ,autopct='%.1f%%', shadow=True)
plt.title('Top 5 Brands', fontsize = 12)

plt.subplot(2,2,2)
explode2 = [0.2, 0, 0, 0, 0, 0, 0, 0, 0]
plt.pie(CountOfCylinder.values , labels = CountOfCylinder.index , explode= explode2 , autopct='%.1f%%', shadow=True)
plt.title('Cylinders In Engine' , fontsize = 12)

plt.subplot(2,2,3)
CountOfDriveType = Vehicle_Prices_db[['DriveType']].value_counts()
plt.pie(CountOfDriveType.values , labels= CountOfDriveType.index,autopct='%.1f%%' ,shadow=True)
plt.title('Drive Type' , fontsize = 12)

plt.subplot(2,2,4)
CountOfFuelType = Vehicle_Prices_db[['FuelType']].value_counts()
explode3 = [0.1, 0, 0, 0, 0.2, 0.4, 0.4, 0.4]
plt.pie(CountOfFuelType.values ,labels=CountOfFuelType.index, explode= explode3 , autopct='%.1f%%' )
plt.title('Fuel Type' , fontsize = 12)

st.pyplot(PieFig)

st.write("\n____________________________________________________________________")
#--Linear Plot of Total Price By Year and average of Kilometer by year-----------------
st.subheader("Linear Plot")
st.write("Graph of total price by year and average of kilometer by year")
pFig = plt.figure(figsize=(15,6))
GroupByYearPrice = Vehicle_Prices_db[['Year','Price']].groupby(['Year']).sum()
plt.subplot(1,2,1)
plt.plot(GroupByYearPrice.index,GroupByYearPrice.values )
plt.title("Total Price By Year" , fontsize = 20)
plt.xlabel("Year" , fontsize = 14)
plt.ylabel("Total Price" , fontsize = 14)
plt.grid()

GroupByYearKilometer = Vehicle_Prices_db[['Year','Kilometres']].groupby(['Year']).mean()
plt.subplot(1,2,2)
plt.plot(GroupByYearKilometer.index, GroupByYearKilometer.values)
plt.title("Mean Kilometer By Price" , fontsize = 20)
plt.xlabel("Year" , fontsize = 14)
plt.ylabel("Mean Kilometer" , fontsize = 14)
plt.grid()

st.pyplot(pFig)
st.write("\n____________________________________________________________________")
#---A kernel density estimate (KDE) of Price and Kilometers----------------------------
st.subheader("KDE Graph")
st.write("A kernel density estimate of Price and Kilometers.")

Vehicle_Prices_db = Vehicle_Prices_db[Vehicle_Prices_db['Price'] < 120000]

DenPriceFig = plt.figure(figsize=[10,6])
sns.kdeplot(data= Vehicle_Prices_db, x='Price')
plt.ticklabel_format(useOffset=False, style='plain', axis='x')
st.pyplot(DenPriceFig)


DenPriceFig = plt.figure(figsize=[10,6])
sns.kdeplot(data= Vehicle_Prices_db, x='Kilometres')
plt.ticklabel_format(useOffset=False, style='plain', axis='x')
st.pyplot(DenPriceFig)

st.write("\n____________________________________________________________________")
#--Scatter Plot Price and Brand----------------------------------------------------------
st.subheader("Scatter Plot")

ScatPlot = plt.figure(figsize=(15,12))
X = Vehicle_Prices_db['Price']
Y = Vehicle_Prices_db['Brand']
plt.scatter(X,Y)
plt.xlabel('Price' , fontsize= 14)
plt.ylabel('Brand' , fontsize= 14)
plt.ticklabel_format(useOffset=False, style='plain', axis='x')
st.pyplot(ScatPlot)

st.write("\n____________________________________________________________________")

#-----End--------------------------------------------------------------------------------