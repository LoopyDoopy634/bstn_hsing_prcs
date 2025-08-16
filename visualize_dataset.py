import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

#Check for the folder images. If it doesn't exist then create one.
output_folder = 'images'
os.makedirs(output_folder, exist_ok=True)

df = pd.read_csv('dataset/housing.csv', delim_whitespace=True)   #Read the data from csv file.

print(f"Generating Plot 1: Distribution of Housing Prices...")
plt.figure(figsize=(15, 9))   #Creates a figure of width 15 and height 9.
sns.histplot(df['MEDV'], bins=30, kde=True)   #Create a histogram of given data divided into 30 columns with a KDE line.
plt.title('Distribution of Boston Housing prices')   #Title of the plot
plt.xlabel('Median Value in $1000s (MEDV)')   #Text on x-axis
plt.ylabel('Number of Houses')   #Text on y-axis
plt.savefig(os.path.join(output_folder, 'Plot 1.png'))   #Save the plot as an image in the images folder.
plt.close()   #Close the matplotlib function

print("Generating Plot 2: House Price vs Number of Rooms...")
plt.figure(figsize=(15, 9))
sns.scatterplot(x='RM', y='MEDV', data=df)   #Create a scatter plot to correlate between 2 different columns.
plt.title('House Price vs Number of Rooms')
plt.xlabel('Average Number of rooms (RM)')
plt.ylabel('Median Value in $1000s (MEDV)')
plt.savefig(os.path.join(output_folder, 'Plot 2.png'))
plt.close()

print('Generating Plot 3: Correlation Matrix Heatmap...')
correlation_matrix = df.corr().round(2)   #Create a correlation matrix for the heatmap.
plt.figure(figsize=(18, 15))
sns.heatmap(data=correlation_matrix, annot=True, cmap='coolwarm')   #Use the correlation matrix to create the heatmap.
plt.title('Correlation Matrix of Housing Data')
plt.savefig(os.path.join(output_folder, 'Plot 3.png'))
plt.close()
