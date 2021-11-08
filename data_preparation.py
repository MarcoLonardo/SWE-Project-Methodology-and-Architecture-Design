# Write code that prepares your data

import pandas as pd
df = pd.read_csv('DBData.csv')

# Basic data description
print(df.shape)
print(df.head(5))
print(df.columns)

# Print the column labels and data types
print(df.info(verbose=True))

# Removing unnecessary columns
df = df.drop(['Indicator Code'], axis=1)
df = df.drop(['Unnamed: 21'], axis=1)
print(df.shape)

# Identifying null values
print(df.isnull().sum())

# Removing all the columns with a significant number of null values
df = df.drop(['2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015'], axis=1)

# Dropping all the rows with a NaN value
df.dropna(axis=0, inplace=True)
print(df.shape)

# Finding Unique Values in the last 5 years to check for anomalies
df['2016'].unique()
df['2017'].unique()
df['2018'].unique()
df['2019'].unique()
df['2020'].unique()

# Load another dataset into a pandas dataframe.
# Some of the columns of this dataset will be merged into the main ones to filter for UE countries
df1 = pd.read_csv('DBCountry.csv')
print(df1.shape)
print(df.columns)

# Drop all columns except the ones we are interested in merging with the other dataset. Based on code written by user
# MaxU on Stack Overflow at https://stackoverflow.com/questions/45846189/how-to-delete-all-columns-in-dataframe
# -except-certain-ones. Accessed 20/10/2021
df1 = df1[['Country Code', 'Currency Unit']]

# Merging the two dataframes
df = df.merge(df1, on='Country Code', how='inner')
print(df.head(5))
print(df.shape)

# Removing all rows for countries containing a currency different from Euro. Adapted from code written by usercs95 on
# Stack Overflow at https://stackoverflow.com/questions/53784017/drop-rows-that-do-not-contain-a-string-within-a
# -value-using-pandas. Accessed 20/10/2021
df = df[df["Currency Unit"].str.contains("Euro")]

# Save the DataFrame back to .csv
df.to_csv('cleaned_dataset.csv', index=False)
