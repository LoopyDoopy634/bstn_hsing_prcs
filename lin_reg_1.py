#This script is used to check if the 'Number of Rooms' attribute is a good feature to determine Housing Prices or not
#R-squred gives an understanding of how well the 'Number of Rooms' factors into the Housing Prices.

import pandas as pd

#sklearn provides all the machine learning functions.
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv('dataset/housing.csv', delim_whitespace=True)

X = df[['RM']]   #This is our main attribute we'll use for the linear regression.
Y = df[['MEDV']]   #This is the attribute we compare X to.

#Split the dataset into 2 parts - 80% training data and 20% test data.
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = LinearRegression()   #Create an instance of a Linear Regression model.
model.fit(X_train, Y_train)   #This function analyzes the training data to find the best possible straight line to describe the relation between X and Y.
print("Model trained using only the 'Number of Rooms' feature!")

y_pred = model.predict(X_test)   #After training, we test the model using the test data.
r2 = r2_score(Y_test, y_pred)   #Compare the predicted value we get from our model to the given value from the test data.

print("\n--- Model Evaluation ---")
print(f"R-squared (R2): {r2:.2f}")
