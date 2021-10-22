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

The Scenario: EU.com wants to develop (copy this from previous scnario examples)

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
economic growth and opportunities. The Board is considering assessing as many parameters as possible from the 
World Bank Dataset, however, they are struggling to translate this data into actionable business intelligence for 
senior leaders. 

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

Given the questions and the problem statement, some of the questions that can be answered using the dataset are:

1. Which countries in Europe have the lowest "ease of doing business" scores?
2. Which variables, representing the biggest problems in doing business, have the lowest scores across EU countries?
3. How do the bottom 5 European countries compare to each other across each of the variables?
4. How have these nations' scores evolved from 2014 to 2020? In other words, have the nations been improving in their 
respective variables?
5. Over the years, has getting credit been easier or more difficult for businesses across Europe?

Once the countries with the lowest scores have been identifies, some of the more specific questions that can be 
answered are:

1. How easy it is for country X to trade across borders?
2. Given that countries XYZ have the lowest score for "Paying Taxes", has it improved over the years?
3. Is "Enforcing Contracts" one of the reasons why it is difficult to do business in country X?

Addressing these questions can help the EU understand which countries are the least attractive investment for businesses
and what are the sub-problems. This is very useful because it will allow the EU to come up with a specific investments 
plan and set of initiatives that best address the country and the problems from a wide variety of different perspectives.
Rather than focusing only on aspect (i.e. paying taxes), this data can offer insights into a wide range of variables. 
Moreover, as part of this assessment, it is important to assess the trend before making a final investment decision. 
It could be very worthwhile to understand whether a country has been improving before investing. 
This could drastically improve the EU's impact on the economic outlook of a country.



### Suggested web app

## Data preparation and exploration
### Data preparation

[Data Preparation](data_preparation.py)

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
