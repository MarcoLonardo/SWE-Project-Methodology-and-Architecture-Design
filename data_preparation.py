# Write code that prepares your data

# Importing Pandas
import pandas as pd

# Load .csv file into a pandas dataframe variable
df_from_csv = pd.read_csv('DBData.csv')

# Load the .csv into dataframe variable with a more convenient name
df = pd.read_csv('DBData.csv')

## Basic Data Statistics
# Print the number of rows and columns in the Dataframe
print(df.shape)

# Print the first 5 rows of data
print(df.head(5))

# Print the column labels
print(df.columns)

# Print the column labels and data types
print(df.info(verbose=True))


# Removing unnecessary columns
df = df.drop(['Indicator Code'], axis=1)
df = df.drop(['Unnamed: 21'], axis=1)



# Checking is the number of rows and columns has reduced after deleting a column
print(df.shape)

# Identifying null values ('Null results' + '\n' +)
print(df.isnull().sum())


#Removing Addtional Columns becuase I can see too many blank cells for 2004 to 2015 and also it will be more valueable
# for EU leaders to condense the improvements only based on the initiaves of the last 5 years
df = df.drop(['2004','2005','2006','2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014','2015'], axis=1)

# Our research is country specific, so we need to ensure we have data for the countries. If we dont, we need to
# remove it becuase we can't come up with assumptions for each category. We could do the mean for each parameter
# but it is risky

# Dropping all the rows with with a NaN value
df.dropna(axis=0, inplace=True)

# Re-checking null values
print(df.shape)

# Finding Unique Values in the last 5 years to check for anomalies

df['2020'].unique()

# Load another dataset into a pandas dataframe. From this we will need other columns to filter for Euro Countries
df1 = pd.read_csv('DBCountry.csv')

# Basic description of variables and data
print(df1.shape)
print(df.columns)

# Drop all columns except the ones we are interested in merging with the other dataset (to add reference)
# https://stackoverflow.com/questions/45846189/how-to-delete-all-columns-in-dataframe-except-certain-ones
df1 = df1[['Country Code', 'Currency Unit']]

# Summarise the current dataframe to see if the latest scrips have been reflected
print(df1.shape)
print(df1.head(5))

#Merging datasets to add additional variables allowing us to filter for EU Countries
df = df.merge (df1, on = 'Country Code', how='inner')

print(df.head(5))
print(df.shape)

# Removing all rows for countries containing a currency different from Euro
# https://stackoverflow.com/questions/53784017/drop-rows-that-do-not-contain-a-string-within-a-value-using-pandas
df = df[df["Currency Unit"].str.contains("Euro")]

# Save the DataFrame back to a ndf.to_csv('cleaned_dataset.csv', index=False)ew csv
df.to_csv('cleaned_dataset.csv', index=False)


df.to_csv('cleaned_dataset1.csv', index=False)

