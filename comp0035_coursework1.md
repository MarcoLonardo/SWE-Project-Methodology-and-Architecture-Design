# Coursework 1

## Technical information
### Repository URL

[Repository](https://github.com/ucl-comp0035/coursework-1-MarcoLonardo.git)

### Set-up instructions

Assume that requirements will be installed from requirements.txt.

If you have used any libraries that require set-up beyond `pip install ...` then use this section to explain any set-up
instructions to be followed to run your coursework.

If the marker cannot execute your coursework they can't grade it!

In my data exploration, I have imported the matplot library. To ensure that this library is imported, I installed the matplotlib package by navigating to Settings and selecting the Python Intepreter for my project.

## Selection of project methodology
### Methodology (or combination) selected

#### The Scenario
DataFirst, a software development company, is developing a web app for their client, the European 
Commission. We are assuming that the European Commission has created a fund for a set of economic investments aimed at reducing the economic
inequalities across the European countries. For this plan, The EU Leadership Team has decided to target countries 
with many barriers to doing business and therefore are the least attractive options for new businesses. 
The European Commission has a vague idea of what 
the Senior Leaders might find useful to make the investment decision, nevertheless, they are relying on DataFirst to 
explore the different feasible options and realise what is the best business intelligence solution.
We are assuming that The DataFirst Team is made up by a small team of students with relevant internship-level experience in the Scrum Methodology. 
They have been asked to have the final web application ready within a fixed timeframe of 4 months. Nevertheless, they
have agreed with the European Board to frequently review the work to adapt to the undefined requirements.


For this particular scenario, it was important to select a software engineering methodology because the main deliverable of the project is a web application. 
Nevertheless, it was also important to consider a methodology that would integrate flexibly and adequately with data science given that at the heart of the web applications we have insights. 
Thus, considering specific selection criteria, we will focus on the Scrum Methodology because it allows the team to develop a web application, while remaining flexible and agile to data science (Scrum for Data Science, n.d.).


### Selection criteria and justification of selection

The Scrum Methodology has been selected evaluating the following 5 criteria: Requirements Understanding, Team Location, 
Ease of access to the client, Working Experience with the team and the Scrum Methodology and the Expected Lifetime of 
the product. These 5 criteria have been identified as the most important because they take into consideration any 
the current ability and skills to deploy the web app, original knowledge of dataset, potential risks and blockers
affecting the quality of the work. 

The first criteria considered was the understanding of the requirements ,referring to both their volatility and
complexity. Selecting a flexible methodology, in this regard,  was crucial because we expect  the deliverables to 
vary depending on the business problem and the key findings in the dataset. In other words, remaining flexible 
throughout the whole product development will allow us to be more relevant to the problem, better adapting to the 
customer and the requirements. Scrum can really help in this scenario because it expects the team to plan flexibly with 
sprint plans. This is where all the backlog items will be explained and programmed with an actionable sprint plan. 
Moreover, the Scrum Methodology, not only has a good integration with data science, it 
also allows to specifically and sufficiently meet the deliverables of this project. This is because Scrum is centered 
around working increment of the software. As a result this is the ideal agile data science method for data explorations,
insights and visualisation because we can answer data science questions without having to invest unnecessary time and 
resources that more structured data science methodologies (i.e. TDSP) would require in the modelling phase 
(i.e. Advanced Data Analytics ). With Scrum, this means that while being flexible to uncertain requirements, 
we can still meet the criteria within the scope of Data Science (with visualisation and exploratory data analysis), 
reducing costs that would come from more complex and structured data science processes.

Secondly, the expected lifetime of the web application was an important criterion in selecting the Agile 
Methodology for this project. The main assumption is that the web application will be developed for a specific purpose
where data visualization will help the client answer questions on their business. As the data is static and will not 
change, we are not expecting the web app to last years and it should, therefore, be developed in a fixed timeframe with 
a pre-determined set of resources. The Agile methodology would be very useful in this scenario because it is an 
efficient method to deliver quality work in a scheduled time. This is mainly due to the nature of sprints that allow 
the team to break down the product development in mini projects each with a fixed duration of one month.
The Agile process is well-suited for this situation because we can flexibly change our requirements over the whole 
lifecycle, but it still allows us to deliver incremental results in a fixed time.

Moreover, another important criterion was determining any risks that could block member of the teams working together. 
Working remotely as international students from all over the world with limited team and work experience could be a 
challenge to the client's rapidly changing requirements. With these risks in mind, the Agile methodology offers the best 
balance between working independently while ensuring a regular work cadence. Not only this ensures that all members 
can accomplish objectives autonomously, but it also guarantees that all members share their updates constantly with 
the team. This is achieved through the daily scrums or stand-ups where all the members are asked to 
share their progress and future plans. Moreover, the three pillars upon which the Agile methodology is built 
best address remote workers. Transparency, inspection and adaption pose emphasis keeping each other 
accountable for anomalies and change. This is very important to our project because regardless of the location, everyone
is responsible for the progress and can rapidly adapt to change.

Finally, it was important to consider the level of experience the team had working together and with the Scrum 
Methodology. As a group of students with limited work and methodology experience, it was important to consider a method
that not only that would ease collaboration, but would elicit quick feedback, support and transparency. Within the team,
the Scrum Method offers many learning and feedback opportunities. At the end of each sprint and throughout 
the whole product development, the team can review the incremental product with the customer to elicit feedback. 
This would allow an inexperienced team in the software industry to quickly re-address customers needs. 
Moreover, there is also an opportunity to share feedback internally in the team with sprint retrospectives where the 
team can reflect on areas of improvement. Finally, as Scrum is a well-known industry and the most popular agile 
methodology, support and documentation are widely available. Together with ongoing feedback, they make Scrum ideal for 
entry-level professionals.

## Definition of the business need
### Problem definition

The European Commission needs to shortlist 3 countries in Europe for a significant investment plan aimed at facilitating
the ease of doing business to reduce inequalities across the EU.
This is 5 year-long plan that needs to be implemented by 2022 to improve the current economic outlook, 
creating future opportunities for younger generations. 
Nevertheless, with the current economic uncertainties and inequalities across Europe, the Commission faces 
 intense pressure to make a sound investment decision.

This decision represents a problem for the board because investing in the wrong countries would contribute to 
increased inequalities, widening the gap between the businesses and nations in Europe. As a result, the EU predicts 
that with a widening gap, businesses will avoid investing in poorer countries where the conditions of 
doing business are more disadvantageous. This, in turn, affects the whole nation and its population limiting its 
economic growth and opportunities. The EU Commission is specifically assessing 4 metrics (Getting Credit, Starting a 
Business, Resolving Insolvency Trading across borders) from the World Bank Dataset, however, they are struggling to translate 
this data into actionable business intelligence for senior leaders. 

There have multiple investment occasions in the past across Europe and this problem seems to be a recurring challenge.
Thus, through this web application, the EU Commission can visualize clearly the parameters of 
each country. Benchmarking these parameters through data visualizations across the different countries would help 
Leaders at the EU Commission measure the impact of their policies. This will make their decisions actionable, 
measurable and specifically oriented at ensuring growth in less developed nations. 

### Target audience

The target audience is the leadership team at the European Commission as they would be interested to gain actionable 
insights from this data. From this web application, they can implement policies and
initiatives that best address nations with disadvantageous business conditions. 
Not only with this data they can make become more specific on the nations that require improvement, but they can also
drastically improve the impact of their initiatives by addressing the specific problem. As all fields (i.e. Economics, 
Politics, Environments), all contribute to the ease of doing business, this data targets the whole EU Board of 
Commission, irrespective of the industry each director manage. Thus, the board, our target audience, can jointly work on
new initiatives collaboratively tackling each problem from the respective perspective (legal, economic, environmental).

While each director has an understanding of tech, we are targeting experienced sales professional aged at least over 50 
years old. Therefore, ease of access and intuitiveness should be our key priorities when working on the design of the
app. Moreover, as they are part of the management board, we expect these people to be very busy and accustomed to renowned 
economic journals (i.e. FT). Therefore, results should be presented concisely with clear visualizations. 

![image](https://user-images.githubusercontent.com/64501760/140772961-4128350f-3fc6-4654-a7ab-8f2f8bbd1b01.png)


### Questions to be answered using the dataset

Given the problem statement and the target audience, we assume that these are the type of questions this project aims to answer:

1. Which countries in Europe have performed worse in 2020?
2. What problems are the worst-performing countries facing?
3. Overall, across the 4 variables, has the ease of doing business improved over the years?


Addressing these questions can help the Leadership Team understand what problems each of the countries are facing before 
making an investment. This is very useful because it will allow the EU to come up with a specific investment
plan that best address the country and the problems from a wide variety of different perspectives.
Rather than focusing only on one problem (i.e. getting credit), this data can offer insights into a wide range of variables. 
Moreover, as part of the investment decision, it is important to consider whether countries have been improving over the years. 
This can be very useful to understand how senior leaders' previous policies have impacted the European Union, addressing
any outstanding gaps.
As a result, besides providing the EU board with stronger awareness of EU challenges, answering these questions will 
help the EU Team maximise the impact of their initiatives on the economies of EU countries.

## Data preparation and exploration
### Data preparation
[Data Preparation](data_preparation.py)

The first step in preparing the data was to have a basic understanding of the dataset. Therefore, 
after loading the dataset as a dataframe variable, it was essential to print the number and the labels of rows and columns. 
From the output, it is clear that we are dealing with a very big dataset as we had 43665 rows and 22 columns. 
The first 4 columns represent categorical data, giving us information about the country and the type of metric the score is based upon. 
Whereas, the remaining column are numerical representing the score in each year from 2004 to 2020.
At first glance, and considering the size of the dataset, the only obvious column I could remove was the Indicator Code because it was repeating the preceding column. 
Nevertheless, another column, Unnamed:21, was automatically created with null values when loading the dataset into the dataframe.
It was necessary to eliminate this column before dealing with null values, because dropping rows while maintaining this column would have removed my whole dataframe. 

While, I was able to remove the null values from the automatically created column, I still needed to check for null values across all the other columns.
Based on the is.null() output, the 3 categorical columns had 0 null values whereas all the "Years" columns (from 2004 to 2020) had null
values, decreasing with the most recent years. Thus, because the number of null values was significant in years 
2004 - 2015 (at least above 18,000 with a dataset of 43,000 rows), I decided that the best solution was to remove columns 2004 to 2015.
As most of the null values are in the columns that have been drop, whenever we will remove the remaining null 
values for the remaining columns, we will still have a significant amount of data. This will also make our dataset more 
relevant to the problem statement helping the EU Leaders focus on the most recent data. 
Moreover, using an imputation technique to fill the missing values (i.e. mean) was not an option in this scenario because we are 
dealing with scores of multiple indicators. Averaging all the data for a particular year would give us an average that 
does not specifically represent each indicator. 
Finally, given that there were no anomalies from the remaining columns 2016 to 2020 (using the unique() function), the 
last step was to remove the remaining null values with dropna().

At this point, we have reduced the dataset to 31263 rows and 8 columns. However, the dataset still has worldwide data 
which is not relevant to the EU Commission. The current dataset does not have any columns that could help us filter 
for EU Countries only, however there is a different dataset from the World Bank (DBCountry.csv) with more information on each of this 
country. After loading this dataset, we noticed that there were 31 columns and 193 rows. From this dataset, we identified only 
two columns that we could be useful to our problem: Country Code and Currency Unit. 
We, therefore set the newly created dataframe as only these 2 columns removing the remaining 29. Country Code would serve 
us as the common column (index) when merging the 2 dataframes, and Currency Unit would allow us to filter only for countries trading with Euros.
Indeed, after removing all other currencies, we had a final dataset of 3315 rows and 9 columns addressing the minimum requirements of the EU Commission.



### Prepared data set
Please add names of your data set files in this repository below, then delete this instruction text.
[Original data set](DBData.csv)
[Prepared data set](cleaned_dataset.csv)

### Data exploration

[Data Exploration]()

The first step, once having prepared the data, was to explore all the different indicators, which represented a metric for a specific area of doing business. In fact, while  the 
data preparation section allowed us to select the years and countries relevantly to the problem statement, we 
are now still dealing with many indicators. We, therefore, wanted to understand how many unique rows we had with the
describe() functions to understand how many indicators our dataset had. Initially, we could see that we had 151 metrics, and 
with the nunique () function, we could see that only 58 of them had the word "score" for a specific indicator. 
This meant that all the remaining 93 rows were different metrics (i.e. time, cost) that were used to calculate the score.
Given that we are only interested in the Score, we decided to remove all other irrelevant metrics (i.e. time, cost) by keeping only the rows containing the word "Score" in the Indicator Name column.
At this point, we could check each unique row with the value_counts() function to understand what each of this 58 scores were measuring.
From this activity, we considered that the Leadership Team's focus was related on the results of 4 specific rows:"Getting credit (DB15-20 methodology) - Score",
"Resolving insolvency - Score","Starting a business - Score", "Trading across borders (DB16-20 methodology) - Score. 
It was clear that we needed to keep only these rows in the dataset, and we achieved this creating 
a list of these rows and dropping all the other rows not included in this list.

At this point, we were presented with few challenges hindering our ability to plot data.
Firstly, having the Years (2016,2017,2018,2019,2020) as columns was limiting the amount of data exploration we could do.
With this format, our primary findings would be related about what happened over the years, nevertheless, our key variables were the indicators.
Therefore, it was crucial to transform them as columns to explore their behaviours across countries and years. 
We could achieve this by converting the Years columns (from 1014 to 2020) into rows of a new column, Year. Subsequently, we turned the rows of the "Indicator Name" column as new columns. 
The second challenge was that, because we had 4 different indicators, it was difficult to rank the final score of these countries.
Therefore, to summarise the overall performance of a country, we introduced a new column, overall score, calculating the average of the 4 selected indicators.
After checking the data types of the columns and the size of the dataset, we could now complete the data exploration with visualizations.
The first analysis was done using a boxplot of all the indicators to understand whether we had any outliers. From the output, 
we could see that there were no outliers because all the scores were within the expected range: 0 and 100. 
While there were a fer less frequent scores away from the mean, it was important to keep them because these are part
of the scores and the ranges, providing a clear picture of areas of improvements. Besides looking at outliers, this boxplot is 
also helpful to describe the overall distribution for each of the indicators in Europe.

<p align="center">
  <img width="640" height="480" src="https://user-images.githubusercontent.com/64501760/140777837-28329963-37ed-44f1-b319-884992cc3823.png">
</p>

Considering the questions identified in the Target Audience section, we continued our data exploration identifying the worst-performing countries in 2020.
Our first plot allowed us to realise that, with the current dataset, we are plotting every single observation. 

<p align="center">
  <img width="640" height="480" src="https://user-images.githubusercontent.com/64501760/140779824-2129c7a9-9a3f-40f9-9651-a79100d28925.png">
</p>

Therefore, to obtain more meaningful visualizations,  we would need to plot averages across a more defined dataframe.
Thus, we split the dataset into multiple datasets, where in the first dataset we focused only on 2020 data. 
After dropping the "Year" column, we could now plot the average of all the indicators grouped by the countries. 

<p align="center">
  <img width="640" height="480" src="https://user-images.githubusercontent.com/64501760/140780071-646ae53c-4993-4e07-8a29-be708f70bea7.png">
</p>

The output comprehensively describes all the indicators by any of the countries, but it could be cumbersome to interpret 
Therefore, we decided to use Overall Score only to rank countries by the indicators.
Therefore, using a third dataframe with only two columns, we could see that showing that the worst-performing countries were: Luxembourg, Greece, San Marino and Malta.

<p align="center">
  <img width="640" height="480" src="https://user-images.githubusercontent.com/64501760/140779991-41c27c78-da5c-452c-83bc-9977d9b948d8.png">
</p>

At this point, we kept only the rows with the lowest performing countries in our new dataframe so that we could see all indicators by these 4 countries.


<p align="center">
  <img width="640" height="480" src="https://user-images.githubusercontent.com/64501760/140779677-7d838e45-5c1f-4814-9bf5-d95e8506e05e.png">
</p>


Finally, the last part of the exploration was Time, providing an example of how indicators changed by year. 
In this case, there was no need to split the data, and we were able to plot the mean of all the indicators by the Years.


<p align="center">
  <img width="640" height="480" src="https://user-images.githubusercontent.com/64501760/140779172-ed8fce82-d23a-41bf-a53d-3df70b9ba22c.png">
</p>




As a result, we were able to explore the dataset both
from a Country and Year Perspective in relation to the Indicators. Considering the target audience, problem statements and the assumed questions, we believe this is 
the best structure for our dataset because we have the flexibility to observe the behaviours of the indicators (EU's key focus) across any other parameters. 
One of the negatives of this choice is that we had to trade off the possibility of doing more advanced Time analysis (i.e. Time Series of the years). 
We could have achieved this if we decided to keep the Years as our main columns. Nevertheless, Time is not as relevant as 
focusing on the indicators, and the chosen data structure still allows us to perform some basic visualizations maintaining the Years as one column.








## Weekly progress reports
### Report 1
List what you completed or made progress on this week (in the coursework project).
- Finish Setting Up CW1 on PyCharm
- Worked on some assumptions as the context of the project
- Identified the most important business criteria for the project
- Studied and learnt about the different methodologies 
- Selected the best methodology for the project
-Finished writing section 1, explaining the Scrum methodology and justifying my choice

  
List what you plan to do next week (for the coursework project):
- Defining a Business Need, clarifying what problems I am solving for the client
- Defining a target audience
- Understanding how the dataset can solve the business need and provide value to the client
- Understanding how Software Development and Data Science specifically are related to  the business need


Briefly describe any issues that are impeding your progress (in the coursework project).
- None

### Report 2
List what you completed or made progress on this week (in the coursework project).
- Worked on a hypothetical scenario that would help me define a problem statement taking my dataset into account.
- Defined the problem statement considering different approaches from the PBL 3 Document - Lack of data insights for EU Investment Decisions
- Identified the target audience considering why their needs and goals - EU Commission Board
- Created one persona better describing my target audience
- Developed 3 Questions that we can answer using the DataSet provided and explaining how the answers might be useful to the target audience


List what you plan to do next week (for the coursework project):
- Review Problem Statement with the Tutor Session Feedback
- Adding suggested use of the web product based on review and feedback
- Preparing data (i.e. cleaning data, finding  outliers, condensing the size of the data in relation to the problem statement)
- Documenting the steps in cleaning data and the why

Briefly describe any issues that are impeding your progress (in the coursework project).
-No major issues at the moment. The only challenge is with the dataset: 
 The dataset seems to be limited in terms of the hypothetical scenarios in which it can be used to solve a problem. 
 In other words, with this dataset, it is challenging to think of a real-life scenario in which a client might need to 
 use it. So, I am not sure to what extent the fictional scenario I have imagined will really help me answer the 
 questions identified in the problem statement.

### Report 3
List what you completed or made progress on this week (in the coursework project).
- Installed the set of the relevant libraries to prepare the data (i.e. Pandas). As part of this, I had to troubleshoot
  problems relating to setting up the venv library. Whenever I was working with new projects like the prepare data pdf from PLB3 Pycharm was working, however, with this coursework working with the venv library has been a challenge
- Opened the "Doing Business" Dataset in a Pandas Dataframe
- Completed Basic Data Statistics to have basic information about the data frame (i.e. rows, columns, size)
- Worked on unnecessary columns and missing data
-Checking for unique values


List what you plan to do next week (for the coursework project):
- Documenting my "prepare the data" code. This means adding to the main coursework a description of the dataset and 
  justifications of how I have used the code to prepare the data relevantly to the problem statement
- Exploring the data, using new code that is relevant to the problem statement and the questions raised in PLB3
- Improving my description of the scenario at the beginning of the coursework. This is a small section at the beginning 
  to explain the context and assumptions  upon which problem statement, methodology, target audience have been created


Briefly describe any issues that are impeding your progress (in the coursework project).
- None
### Report 4
List what you completed or made progress on this week (in the coursework project).
- Documented and justified the steps in my data preparation code
- Completed the code for the data exploration
- Refined the question to be answered relevantly to the target audience and problem statement
- Added a introductory scenario description to better describe assumptions and context of the project
- Added Status Reports to the project


List what you plan to do next week (for the coursework project):
- Document Data Exploration Code
- Refine the Data Exploration Plots and Visualisations
- Improve formatting and referencing
- Review and finalise the whole project


Briefly describe any issues that are impeding your progress (in the coursework project). 
- Is answering the questions from the "Business Need" section part of this assessment?
  I am asking this because, while I have managed to narrow down the data to a manageable size, there are many labels 
  requiring more advanced visualisation. I am wondering whether it may be worth reducing the dataset even more to 
  simplify this process. 




## References
Data Science Process Alliance. n.d. Scrum for Data Science. [online] Available at: <https://www.datascience-pm.com/scrum/https://www.datascience-pm.com/scrum/> [Accessed 8 November 2021].
Use any [referencing style](https://library-guides.ucl.ac.uk/referencing-plagiarism/referencing-styles) that you are
used to using in your course.
