# Write code that explores your data set

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cleaned_dataset.csv')
pd.set_option('display.max_rows', df.shape[0] + 1)
pd.set_option('display.expand_frame_repr', False)

# Set the column width to 150 so that we can read lengthy strings in the output. Adapted from code written by
# user joris on StackOverflow at https://stackoverflow.com/questions/29902714/print-very-long-string-completely-in
# -pandas-dataframe/29902819 Accessed 27/10/2021
pd.options.display.max_colwidth = 150

# Print all of the unique indicators from the Indicator Name Column
df['Indicator Name'].describe()
df['Indicator Name'].unique()

# Count how many observations have the value "Score" Based on code written by Scott Boston on Stack Overflow at
# https://stackoverflow.com/questions/45759966/counting-unique-values-in-a-column-in-pandas-dataframe-like-in-qlik
# /45760042 Accessed 27/10/2021
df[df["Indicator Name"].str.contains("Score")].nunique()

# Filtering only for the Score rows
df = df[df["Indicator Name"].str.contains("Score")]
df['Indicator Name'].describe()
df['Indicator Name'].value_counts()

# Create a list of the selected rows and drop all the rows from the dataset that are not
# in this list. Based on code written by user Ffisegydd on Stack Overflow at
# https://stackoverflow.com/questions/27965295/dropping-rows-from-dataframe-based-on-a-not-in-condition Accessed
# 29/10/2021
Not_to_drop = ["Getting credit (DB15-20 methodology) - Score",
               "Resolving insolvency - Score",
               "Starting a business - Score",
               "Trading across borders (DB16-20 methodology) - Score"]
df = df[df["Indicator Name"].isin(Not_to_drop)]

# Check the number of unique rows, the final number of rows and basic stats of our dataset
df['Indicator Name'].value_counts()
print(df.shape)
print(df.describe())

# Convert all the years columns into the rows of a new column (Year). Based on code written by user cs95 on Stack
# Overflow at https://stackoverflow.com/questions/28654047/convert-columns-into-rows-with-pandas Accessed 29/10/2021
df = df.melt(id_vars=["Country Name", "Indicator Name", "Country Code", "Currency Unit"],
             var_name="Year",
             value_name="Score")

# Convert the values in the Indicator Name column into new columns. Based on code written by user jezrael on Stack
# Overflow at https://stackoverflow.com/questions/36982313/turn-values-in-a-dataframe-column-into-column-labels
# Accessed 03/11/2021
df = df.pivot_table(index=['Country Name', 'Country Code', 'Currency Unit', 'Year'], columns='Indicator Name',
                    values='Score', fill_value='')
df = df.rename_axis(None, axis=1)
df = df.reset_index()

df.rename(columns={
    'Getting credit (DB15-20 methodology) - Score': 'Getting Credit - Score',
    'Starting a business - Score': 'Starting a business - Score',
    'Trading across borders (DB16-20 methodology) - Score': 'Trading across borders - Score',
    'Resolving insolvency - Score': 'Resolving insolvency - Score',
}, inplace=True)

# Create a new parameter as the mean of the 4 indicators. Based on code written by Alex on Stack Overflow at 
# https://stackoverflow.com/questions/48366506/calculate-new-column-as-the-mean-of-other-columns-pandas/48366525
# Accessed 03/11/2021
df['Overall Score'] = df[['Getting Credit - Score', 'Starting a business - Score', 'Trading across borders - Score',
                          'Resolving insolvency - Score']].mean(axis=1)

# Checking data type and size of dataset
print(df.info(verbose=True))
print(df.shape)
print(df.head(10))

# Create a boxplot to check for outliers
boxplot = df.boxplot(column=['Getting Credit - Score', 'Resolving insolvency - Score',
                             'Starting a business - Score', 'Trading across borders - Score'], fontsize=6)
boxplot.plot()
plt.show()

df.plot()
plt.show()

# Create a new dataframe containing only 2020 data
df2 = df[df["Year"].str.contains("2020")]
df2 = df2.drop('Year', 1)

# Plot the average of all indicators and group them by country. Adapted from code written by Reka Horvath
# on the Real Python blog at https://realpython.com/pandas-python-explore-dataset/#visualizing-your-pandas
# -dataframe. Accessed 05/11/2021
df2.groupby(['Country Name']).agg(['mean']).plot.bar()
plt.show()

# Create a new dataframe with only two columns
df3 = df[['Country Name', 'Overall Score']]

# Plot the average of the overall scores by each country
df3.groupby(['Country Name']).agg(['mean']).plot.bar()
plt.show()

# Create a new dataframe containing 2020 only values
df4 = df[df["Year"].str.contains("2020")]
df4 = df4.drop('Year', 1)

# Create a new variable including only with the worst-performing countries. Drop from the new dataframe any rows not
# included in Worst_Countries.
Worst_Countries = ["Malta",
                   "Luxembourg",
                   "Greece",
                   "San Marino"]
df4 = df4[df4["Country Name"].isin(Worst_Countries)]

# Plot the average of all indicators and group these by the countries
df4.groupby(['Country Name']).agg(['mean']).plot.bar(fontsize=6)
plt.show()

# Create a line chart plotting the mean of all indicators over the years
df.groupby(['Year']).agg(['mean']).plot.line(fontsize=15)
plt.show()
