# Write code that prepares your data

#Importing Pandas
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


# Checking is the number of rows and columns has reduced after deliting a column
print(df.shape)

# Identifying null values ('Null results' + '\n' +)
print(df.isnull().sum())
print(df.isna().sum())

#Removing Addtional Columns becuase I can see too many blank cells for 2004 to 2015 and also it will be more valueable
# for EU leaders to condense the improvements only based on the initiaves of the last 5 years

# Our research is country specific, so we need to ensure we have data for the countries. If we dont, we need to
# remove it becuase we can't come up with assumptions for each category. We could do the mean for each parameter
# but it is risky

# Dropping all the rows with with a NaN value
df.dropna(axis=0, how='any', inplace=True)

# Re-checking null values
print(df.shape)

# Finding Unique Values in the last 5 years to check for anomalies
df['2020'].unique

# merging datasets