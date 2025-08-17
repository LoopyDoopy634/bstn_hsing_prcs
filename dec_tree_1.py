#This script uses a Decision Tree model over the 'Number of Rooms' attribute.
#Then it gives us an idea of how the 'Number of Rooms' attribute can influence the Housing Prices.

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor   #Contains all the functions related to Decision Trees.
from sklearn.metrics import r2_score

df = pd.read_csv('dataset/housing.csv', delim_whitespace=True)

X = df[['RM']]   #This is our main attribute we'll use for the Decision Tree.
y = df[['MEDV']]   #This is the attribute we compare X to.

#Split the dataset into 2 parts - 80% training data and 20% test data.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeRegressor(max_depth=3, random_state=42)   #Create an instance of a Decision Tree model with three levels as the maximum limit.
model.fit(X_train, y_train)   #This function analyzes the training data to find the best possible straight line to describe the relation between X and Y.
print("Model trained using a Decision Tree!")

y_pred = model.predict(X_test)   #After training, we test the model using the test data.
r2 = r2_score(y_test, y_pred)   #Compare the predicted value we get from our model to the given value from the test data.

print("\n--- Model Evaluation ---")
print(f"R-squared (R2): {r2:.2f}")
