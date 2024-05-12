import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder
from settings import Path


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import accuracy_score


data = pd.read_csv(Path)
# Drop unnecessary columns
data.drop(["country-year"], axis=1, inplace=True)
data.drop(["HDI for year"] ,axis=1, inplace=True)
data.dropna(inplace=True)

#map data 
lb = LabelEncoder()
data['age'] = lb.fit_transform(data['age'])
data['sex'] = lb.fit_transform(data['sex'])
data['country'] = lb.fit_transform(data['country'])

# Encode categorical variables
data = pd.get_dummies(data)


X , y = data.drop(['suicides_no'] ,axis=1) , data['suicides_no']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2 ,random_state=42)


#-- Model 1 : Linear Regression To predict Price -------------------------------------------
model = LinearRegression()
model.fit(X_train , y_train)

y_test_prediction = model.predict(X_test)
mae = mean_absolute_error(y_test, y_test_prediction)
mse = mean_squared_error(y_test, y_test_prediction)
rmse = np.sqrt(mse)
r2_test = r2_score(y_test, y_test_prediction)

y_train_prediction = model.predict(X_train)
maeTrain = mean_absolute_error(y_train, y_train_prediction)
mseTrain = mean_squared_error(y_train, y_train_prediction)
rmseTrain = np.sqrt(mseTrain)
r2_train = r2_score(y_train, y_train_prediction)

st.subheader(':blue[Model 1:] Linear Regression')
st.write("Mean Absolute Error for Test (MAE) :", mae)
st.write("Mean Squared Error for Test  (MSE):", mse)
st.write("R-squared for Test (Coefficient of Determination):", r2_test)

st.write("\n____________________________________________________________________")
st.write("Mean Absolute Error for Train (MAE) :", maeTrain)
st.write("Mean Squared Error for Train  (MSE):", mseTrain)
st.write("R-squared for Train (Coefficient of Determination):", r2_train)
st.write("\n____________________________________________________________________")
st.write(''' \n :red[Result:] The model doesn't work very well becouse the R-squared of traning close to validation and test
         so model is not good and we can try another model to get nmore accurce.''')
st.write("\n____________________________________________________________________")

# Plotting the actual values vs. predicted values
fig = plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_test_prediction, color='blue', label='Actual vs. Predicted')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2, color='red', label='Ideal Line')
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs. Predicted Values')
plt.legend()
st.pyplot(fig)





#-- Model 2 : Random Forest Regression To predict Price -------------------------------------------


Forestreg = RandomForestRegressor().fit(X_train, y_train)
score = Forestreg.score(X_train, y_train)
y_predition = Forestreg.predict(X_test)
mae = mean_absolute_error(y_test, y_predition)
mse = mean_squared_error(y_test, y_predition)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_predition)

st.subheader(':blue[Model 2:] Random Forest Regression')
st.write(f"Mean Absolute Error (MAE):" , mae)
st.write(f"Mean Squared Error (MSE):", mse)
st.write(f"Root Mean Squared Error (RMSE):" ,rmse)
st.write(f"Score:" ,score*100)
#st.write(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
st.write("\n____________________________________________________________________")
st.write(''' \n :red[Result:] The model seems to perform better than the previous one.''')
st.write("\n____________________________________________________________________")

# Plotting the actual values vs. Random Forest predicted values
fig = plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_predition, color='green', label='Actual vs. Random Forest Predicted')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2, color='red', label='Ideal Line')
plt.xlabel('Actual')
plt.ylabel('Random Forest Predicted')
plt.title('Actual vs. Random Forest Predicted Values')
plt.legend()
st.pyplot(fig)  