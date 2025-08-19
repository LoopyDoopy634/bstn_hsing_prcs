#This script trains a basic Decision Tree Model over 2 attributes: RM and LSTAT.
#Using multiple features leads to better accuracy in our results.

import pandas as pd

#Import all the functions/libraries required for our model.
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score

import joblib
import os

df = pd.read_csv('dataset/housing.csv', delim_whitespace=True)

features = ['RM', 'LSTAT']   #As we are using 2 features now, we can put them in a list.
target = 'MEDV'

X = df[features]   #Using the list, we can take the values in one variable.
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)   #Split the training and test data.

model = DecisionTreeRegressor(max_depth=3, random_state=42)   #Create a Decision Tree instance with a maximum depth of 3.
model.fit(X_train, y_train)   #Train the model over the training data.

y_pred = model.predict(X_test)   #Once training is done, we test the model over the test data.
r2 = r2_score(y_test, y_pred)   #R-squared score is very useful in determining how well our features factor into our target.
print("--- Multi-Feature Model Evaluation ---")
print(f"R-squared (R2): {r2: .2f}")

model_folder = 'models'
os.makedirs(model_folder, exist_ok=True)
model_filename = 'multi_feature_model.joblib'
full_path = os.path.join(model_folder, model_filename)
joblib.dump(model, full_path)   #Save the model for further uses.

print(f"\nModel trained and saved to '{full_path}'")
