# Write code that explores your data set

# Setting Pandas Options so that all rows and columns will be printed in the output
# First step here is to print all the rows this is important becuase we need to explore the different metrics/indicators and eventusally filter for them
import pandas as pd

pd.set_option('display.max_rows', df.shape[0] + 1)
pd.set_option('display.expand_frame_repr', False)

# Setting the column width to 150 so that we can read lengthy strings in the output / https://stackoverflow.com/questions/29902714/print-very-long-string-completely-in-pandas-dataframe/29902819
pd.options.display.max_colwidth = 150

# Understanding how many metrics we have
# Checking for unique values and quantyfing them
df['Indicator Name'].describe()

#Listing all the Unique Rows
df['Indicator Name'].unique()

# Counting how many obeservations have the value "Score"
df[df["Indicator Name"].str.contains("Score")].nunique()
#Double-checking the unique values number / https://stackoverflow.com/questions/45759966/counting-unique-values-in-a-column-in-pandas-dataframe-like-in-qlik/45760042
df['Indicator Name'].nunique()

# Filtering only for the Score rows -
df = df[df["Indicator Name"].str.contains("Score")]

#Re-checking the list - we can see we narrow it down to 22 but what are these https://stackoverflow.com/questions/50165953/python-dataframes-describing-a-single-column
df['Indicator Name'].describe()

# List and check all the number of indicators. We have too many metrics describing the total score and the score within
# each components making up the total scores. We need to understand what rows are not relevant /https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html
df['Indicator Name'].value_counts()

# Creating a list of the Selected Rows that we don't want to drop. These are our key indicator for insights / https://stackoverflow.com/questions/28679930/how-to-drop-rows-from-pandas-data-frame-that-contains-a-particular-string-in-a-p
Not_to_drop = ["Getting credit (DB15-20 methodology) - Score",
               "Resolving insolvency - Score",
               "Starting a business - Score",
               "Trading across borders (DB16-20 methodology) - Score"]
# Dropping all rows except the ones in Not_to_drop
df = df[df["Indicator Name"].isin(Not_to_drop) == True]

# Checking the number of unique rows and the final number of rows of our dataset
df['Indicator Name'].value_counts()
print(df.shape)

# Now we that we have the relevant indicators we can check the basic stats of the whole dataframe
print(df.describe())

# Rearranging columns - convert columns into rows / https://stackoverflow.com/questions/28654047/convert-columns-into-rows-with-pandas
df = df.melt(id_vars=["Country Name", "Indicator Name", "Country Code", "Currency Unit"],
        var_name="Year",
        value_name="Score")


#Turn values in a DataFrame column into column labels/ https://stackoverflow.com/questions/36982313/turn-values-in-a-dataframe-column-into-column-labels
df = df.pivot_table(index=['Country Name','Country Code', 'Currency Unit', 'Year'], columns='Indicator Name', values='Score', fill_value='')
df = df.rename_axis(None, axis=1)
df = df.reset_index()

# Rename the longer column names
df.rename(columns={
'Getting credit (DB15-20 methodology) - Score': 'Getting Credit - Score',
'Starting a business - Score': 'Starting a business - Score',
'Trading across borders (DB16-20 methodology) - Score': 'Trading across borders - Score',
'Resolving insolvency - Score' : 'Resolving insolvency - Score',
}, inplace=True)


# Adding a new measure / https://stackoverflow.com/questions/48366506/calculate-new-column-as-the-mean-of-other-columns-pandas/48366525
df['Overall Score'] = df[['Getting Credit - Score', 'Starting a business - Score', 'Trading across borders - Score','Resolving insolvency - Score']].mean(axis=1)


# Checking type
print(df.info(verbose=True))

# Final View over the dataset
print(df.shape)
print(df.head(10))

# Add this import

import matplotlib.pyplot as plt

# Checking for Outliers - From this we can see that there are no outliers because these values
boxplot = df.boxplot(column=['Getting Credit - Score','Resolving insolvency - Score',
                             'Starting a business - Score', 'Trading across borders - Score'], fontsize=6)
boxplot.plot()
plt.show()

# Plotting dataset
df.plot()
plt.show()

# First Step is to explore the overall performance of the different countries across these variables in 2020
# When trying to plot this data, it is clear that dealing with too many variables makes it diffcult to plot the data in a meanigful way.
# As we have repeating rows, we do not need to plot every single score of each row, but an average  of the score by the country, year or indicator type.
# We cannot, however, plot the average of multiple columns, therefore we will split the current dataset creating to explore the variables indipendently.
# Creating a new dataframe containing only 2020 data
df2 =df[df["Year"].str.contains("2020")]
# Dropping the column year so that we can explore the avarage of all the indicators by the individual countries
df2 =df2.drop('Year',1)

# Plotting the average of all indicators and grouping these by the countries / https://realpython.com/pandas-python-explore-dataset/#visualizing-your-pandas-dataframe
df2.groupby(['Country Name']).agg(['mean']).plot.bar()
plt.show()

# Creating a new dataset with only two columns
df3 = df[['Country Name', 'Overall Score']]
# Plotting the average of the overall scores by each country
df3.groupby(['Country Name']).agg(['mean']).plot.bar()
plt.show()

#Creating a new dataframe only containing 2020 values
df4 = df[df["Year"].str.contains("2020")]
# Creating a new variable only with the worst-performing countries
Worst_Countries = ["Malta",
               "Luxembourg",
               "Greece",
               "San Marino"]
# Dropping all rows except the ones in Worst_Countries
df4 = df4[df4["Country Name"].isin(Worst_Countries) == True]

# Dropping the Year Column to avoid skewing the results
df4 =df4.drop('Year',1)

# Plotting the average of all indicators and grouping these by the countries
df4.groupby(['Country Name']).agg(['mean']).plot.bar(fontsize=6)
plt.show()


# Create a line chart plotting the mean of all indicators over the years
df.groupby(['Year']).agg(['mean']).plot.line(fontsize=15)
plt.show()











# Removing all the rows that do not contain the word "Score". This allows us to remove noise,
# focusing specifically on the final score for each category. All the final scores for each category
# have the word "score", so we can quickly filter for them.


# While, however, we have filtered for all the scores, we still have too many score rows that
# represent the sub-categories upon which the general category score is calcualted with a simple average.
# We, therefore have to filter specifically for the cateogries. Considering that the EU board is made up of busy
# professionals, we need to provide consices insights specif on results


# From the dataset, we observe that the overall category score is formatted without a semicolon. We can therefore filter
# for this removing all rows with a semicolon

