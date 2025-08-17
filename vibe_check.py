#This is a simple script to just get used to the given dataset by going through some of the basic stuff, like headers, number of unique entries, mean, median, etc.

import pandas as pd

df = pd.read_csv('dataset/housing.csv')

print(df.head())   #head prints the first 5 columns from the dataset

print(df.info())    #info gives a technical summary of the dataset i.e. the columns, number of non-null entries, etc

print(df.describe())    #describe gives statistical summary like highest values, unique values, etc

print(df.isnull().sum())    #tells us if there are any missing values to handle