'''
 Task 2 :
Data manipulation with pandas :
Description :This task involves using the pandas library to manipulate data.

Responsibility: Load a CSV file into a pandas dataframe. Perform operations like 
filtering data bssed on condition, handling missing values, and calculating 
summary statistics.

'''

import pandas as pd 
import numpy as np
import matplotlib.pyplot
from scipy import stats

# Read a CSV file 
data = pd.read_csv("C:\\Users\\DELL\Downloads\\01.Data Cleaning and Preprocessing.csv")

# print the type of data 
print(type(data))

# print information about the dataframe
print(data.info())

# print descriptive statistics of the DataFrame
print(data.describe())

# Drop duplicate rows
data = data.drop_duplicate()

# Print the updated DataFrame after dropping dulicates 
print("DataFrame after dropping duplicates:")
print(data)

#print a DataFrame indicating if values are null 
print(data.isnull())

# Print the sum of null values for each column 
print(data.isnull().sum())

#Print the total numer of null values in the DataFrame
print(data.isnull().sum().sum())

# Fill NaN values with 222222 and assign to data2
data2 = data.fillna(value = 222222)

# Print the updated DataFrame with NaN values filled
print(data2)

# Print the total number of null values in the updated DataFrame
print(data2.isnull().sum().sum())

# Fill NaN values using the 'pad' method and assign to data3
data3 = data.fillna(method='pad')

# Print the updated DataFrame with NaN values filled using 'pad' method
print(data3)

# Fill NaN values using the 'bfill' method and assign to data4
data4 = data.fillna(method='bfill')

#Print the updated DataFrame with NaN values filled using 'bfill' method
print(data4)

# Print the columns of data2 before dropping a column 
print("columns before dropping 'observations' :",data2.columns)

# Drop the 'observations' column from data2
data2.drop(['Blowflow'],axis=1, implace=True)

# Print the columns of data2 after dropping a column
print("Columns after dropping 'observations :",data2.columns)

# Select only numeric columnns for quantile calculatinos 
numeric_data2 = data2.select_dtypes(include=[np.number])

# Calculate the first and third quartiles (Q1 and Q3)
Q1 = numeric_data2.quantile(0.25)
Q3 = numeric_data2.quantile(0.75)

# Calculate the interquantile range (IQR)
IQR = Q3 - Q1

# Print the IQR
print("Interquantile Range (IQR):",IQR)

outliers = numeric_data2[((numeric_data2 < (Q1 - 1.5 * IQR)) | (numeric_data2 > (Q3 + 1.5 * IQR))).any(axis=1)]

# Print the rows with outliers 
print("Rows with outliers :")
print(outliers)

print(outliers.describe)
