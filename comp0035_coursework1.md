# Coursework 1

## Technical information
### Repository URL

[Repository](https://github.com/ucl-comp0035/coursework-1-MarcoLonardo.git)

### Set-up instructions

Assume that requirements will be installed from requirements.txt.

If you have used any libraries that require set-up beyond `pip install ...` then use this section to explain any set-up
instructions to be followed to run your coursework.

If the marker cannot execute your coursework they can't grade it!


## Selection of project methodology
### Methodology (or combination) selected

The Scenario
DataFirst, a software development company made up of graduates, is developing a web app for their client, the European 
Commission. The European Commission have created a fund for a set of economic investments aimed at reducing the economic
inequalities across the European countries. For this plan, The EU Leadership Team has decided to target countries 
with many barriers to doing business and therefore are the least attractive options for new investments and businesses. 
To make this assessment, they would like to focus specifically on 4 Indicators from World Bank Dataset: Getting Credit,
Starting a Business, Resolving Insolvency, Trading Across Borders. The European Commission has a vague idea of what 
the Senior Leaders might find useful to make the investment decision, nevertheless, they do not know what solution would
be optimal to have the best interpretation of business insights.
The DataFirst Team

Choosing an Agile methodology for this project will be essential given the business criteria identified in the next 
section. In particular, we will focus on the Scrum Methodology as it will equip the team with a rigorous but flexible 
process applicable for data science. This will be important, because not only, we are looking to develop a web 
application, but we also want to provide exploratory data insights in the form of visualizations and reports.


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

The European Commission needs to shortlist 3 countries in EU for a significant investment plan aimed at facilitating
the ease of doing business to reducing inequalities across EU.
This is 5 year-long plan that needs to be implemented by 2022 to improve the current economic outlook, 
creating future opportunities for younger generations. 
Nevertheless, with the current economic uncertainties and inequalities across Europe, the Commission faces 
an intense pressure to make a sound investment decision.

This decision represents a problem for the board because investing in the wrong countries would contribute to 
increased inequalities, widening the gap between the businesses and nations in EU. As a result, the EU predicts 
that with a widening gap, businesses will avoid investing in poorer countries like Italy where the conditions of 
doing businesses are more disadvantageous. This, in turn, affects the whole nation and its population limiting its 
economic growth and opportunities. The EU Commission is specifically assessing 4 metrics (Getting Credit, Starting a 
Business, Resolving Insolvency Trading across borders)World Bank Dataset, however, they are struggling to translate 
this data into actionable business intelligence for senior leaders. 

There have multiple investment occasions in the past across Europe and, this problem arises every time that an
investment opportunity arise. Thus, through a web product, the EU Commission can visualize clearly the parameters of 
each country. Benchmarking these parameters through data visualizations across the different countries would help 
Leaders at the EU Commission to objectively map and assess the EU situation. This will make their decisions actionable, 
measurable and specifically oriented at ensuring growth in less developed nations. 

### Target audience

The target audience is the leadership management board at the European Commission as they would be interested to gain actionable 
insights from this data. From this web product and the embedded data visualizations they can implement policies an
initiatives that best address  in nations and problems with disadvantageous business conditions. 
Not only with this data they can make become more specific on the nations that require improvement, but they can also
drastically improve the impact of their initiatives by addressing the specific problem. As all fields (i.e. Economics, 
Politics, Environments), all contribute to the ease of doing business, this data targets the whole EU Board of 
Commission, irrespective of the industry each director manage. Thus, the board, our target audience, can jointly work on
new initiatives collaboratively tackling each problem from the respective perspective (legal, economic, environmental).

While each director has an understanding of tech, we are targeting experienced sales professional aged at least over 50 
years old. Therefore, ease of access and intuitiveness should be our key priorities when  working on the design of the
app. Moreover, as they are part of the management board, we expect these people to be very busy and accustomed to famous
economic journals (i.e. FT). Therefore, results should be presented concisely with clear visualizations. 

### Questions to be answered using the dataset

Given the problem statement and the target audience, we assume that these are the type of questions this project aims to answer:

1. Which countries in Europe have performed worse in 2020?
2. What problems are the worst-performing countries facing?
3. Has the "Starting a new Business" Score improved over the years for Italy?
4. What countries have the lowest scores in Getting Credit?
5. Overall, across the 4 variables, has the ease of doing business improved over the years?


Addressing these questions can help the EU understand what problems each of the countries are facing before 
making an investment. This is very useful because it will allow the EU to come up with a specific investments 
plan and set of initiatives that best address the country and the problems from a wide variety of different perspectives.
Rather than focusing only on one problem (i.e. getting credit), this data can offer insights into a wide range of variables. 
Moreover, as part of the investment decision, it is important to consider whether countries have been improving in a 
particular area over the years. Deciding to invest and implement new initiatives in a country who has not been
improving can have a  more significant impact than investing in a country with a low score but that is starting to improve. 
As a result, besides providing the EU board with stronger awareness of EU challenges,  answering these questions will be 
help the EU Team maximise the impact of their initiatives on the economies of EU countries.

## Data preparation and exploration
### Data preparation
[Data Preparation](data_preparation.py)

The first step in preparing the data was to have a basic understanding of the dataset. Therefore, 
after loading the dataset as a dataframe variable, it was essential to print the number and the labels of rows and columns. 
From the output, it is clear that we are dealing with a very big dataset as we have 43665 rows and 22 columns. 
The first 4 columns represent categorical data, giving us information about the country and the type of metric the score is based upon. 
Whereas, the remaining column were numerical representing the score in each year from 2004 to 2020.
At first glance, and considering the size of the dataset, the only obvious column I could remove was the Indicator Code because it was repeating the preceding column. 
Nevertheless, another column, Unnamed:21, was automatically created with null values when loading the dataset into the dataframe
It was necessary to eliminate this column before checking for null values, because dropping rows while maintaining this column would have removed my all dataset. 

While, I was able to remove the null values from the automatically created column, I still needed to check for null values across all the other columns.
Based on the is.null() output, the current 3 categorical column had 0 null values whereas all the Years columns had null
values, decreasing with the most recent years. Thus, because the number of null values was significant in years 
2004 - 2015 (at least above 18,000 with a dataset of 43,000 rows), I decided that the best solution was to remove columns 2004 to 2015.
Because most of the null values are in the columns that have been drop, whenever we will remove the remaining null 
values in the remaining columns, we will still be able to deal with significant amount of data which also more relevant 
and recent to the EU Leadership Team.
Moreover, replacing the null variables with other values (i.e. mean) was not an option in this scenario because we are 
dealing with scores of multiple indicators. Averaging all the data for a particular year would give us an average that 
does not specifically represent each category. 
Finally, given that there were no anomalies from the remaining columns 2016 to 2020, the last step was to remove the 
remaining null values with dropna().

At this point, we have reduced the dataset to 31263 rows and 8 columns. However, the dataset still has worldwide data 
which is not yet relevant to the EU Commission. The current dataset does not have any columns that could help us filter 
for EU Countries only, however there is a different dataset from the World Bank (DBCountry.csv) with more information on each of this 
country. After loading this dataset, we notice there are 31 columns and 193 rows. From this dataset, we identify only 
two columns that we can be useful to our problem: Country Code and Currency Unit. 
We, therefore set the newly created dataframe as only these 2 columns removing the remaining 29. Country Code would serve 
us as the common column (index) when merging the 2 dataframes, and Currency Unit will allow us to filter only for countries trading with Euros
Indeed, after removing all other currencies, we have a final dataset of 3315 rows and 9 columns addressing the essential requirements of the EU Commission.



### Prepared data set
Please add names of your data set files in this repository below, then delete this instruction text.
[Original data set]()
[Prepared data set]()

### Data exploration

[Data Exploration]()

## Weekly progress reports
Copy and paste from Moodle or use the following structure. Delete this instruction text.

What I did in the last week:
- item
- item

What I plan to do in the next week:
- item
- item

Issues blocking my progress (state ‘None’ if there are no issues):
- item
- item

### Report 1

### Report 2

### Report 3

### Report 4

## References
Use any [referencing style](https://library-guides.ucl.ac.uk/referencing-plagiarism/referencing-styles) that you are
used to using in your course.
