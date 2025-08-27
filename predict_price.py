#This script takes data on RM and LSTAT values and then uses the model to predict a price.
#The model is working fine if it gives:
# 1. High price for a Large House (high RM, low LSTAT)
# 2. Low price for a Small House (low RM, high LSTAT)

import pandas as pd   #As all of our data has been used through the DataFrame format for this model, we need to import pandas to work with the model.
import joblib
import os

model_folder = 'models'   #Name of the folder with the models.
model_filename = 'multi_feature_model.joblib'   #Name of the model.
full_path = os.path.join(model_folder, model_filename)   #Join the model folder and model filename to get the path of the model.
model = joblib.load(full_path)   #Load the model using the path.

#This is where we create a DataFrame that has 2 columns and 3 rows:
# 1. The columns are our attributes: RM and LSTAT
# 2. The first row has values for an Average House (average RM, average LSTAT)
# 3. The second row has values for a Large House (high RM, low LSTAT)
# 4. The third row has valuse for a Small House (low RM, high LSTAT)

scenarios = {
    "Average House":pd.DataFrame([[6.5, 10.0]], columns=['RM', 'LSTAT']),
    "Large House (Wealthy Area)":pd.DataFrame([[8.0, 4.0]], columns=['RM', 'LSTAT']),
    "Small House (Poorer Area)":pd.DataFrame([[5.0, 20.0]], columns=['RM', 'LSTAT'])
}

print("\n--- Making Predictions ---")

for name, data in scenarios.items():   #We take a for loop to run through the rows in the DataFrame one by one.
    predicted_price = model.predict(data)[0]   #.predict() takes the data from the row and applies the model through it to get a prediction on the price.
    
    rooms = data['RM'].iloc[0]   #iloc is used to select data based on their integer position from a DataFrame.
    lstat = data['LSTAT'].iloc[0]
    
    print(f"\nScenario: {name}")
    print(f" > Features: {rooms} rooms, {lstat}% LSTAT")
    print(f" > Predicted Price: ${predicted_price * 1000:,.2f}")
