# Coursework 2

Most students will use the same repository for coursework 2. You may use this file to present the results of that
coursework if you wish. Alternatively you can use video or audio to provide the explanations instead of writing them.

## Requirements definition and analysis
Working with our customer, the EU Commission, and considering the problem statement, the DataFirst team has created a context diagram to agree and define the scope of the web app. 

<p align="center">
  <img width="632" alt="Context Diagram" src="https://user-images.githubusercontent.com/64501760/147003130-0139ef9a-afee-4644-8cca-cc9beab07f8c.png">
</p>


From the context diagram,  we can see that the primary function of the web app is to provide inisghts to  the European Leadership Team with a visualization dashboard.
Nevertheless, with the diagram, we could identify a few additional features relevant to EU Leadership Team's needs. The first one is a news feature displaying stories from relevant third-party Newspapers. News and articles from these newspapaers feed into the website, allowing the EU Team to assess the public sentiment over key deveopment areas. Moreover, another requested functionality is to allow users to tailor visualzations and save preferences. This means that it will be essential to allow users to access their accounts to access history of preferences and saved articles.

### Requirements identification methods

To elicit requirements for this project, we decided to use the following methods: Document Analysis and Brainstorming. As the client has not been very specific in the deliverables, we believe that this combination is the best way to elict requirements because we can creatively think of the client's desired features while remaining pragmatic with real and comparable solutions. In fact, firstly, we would use document analysis to ensure that we capture with no ambiguity the main and most essential requirements from existing solutions. This is a great way to address the client's vague description because we can refer to existing examples (Document Analysis, n.d.). As a comparable example for document analysis, we would mainly levarage the World Bank Platform, to understand what requirements and details are relevant to the web application we are building. Reviewing and confirming these requirements with the client will be essential becuase we are able to capture requirements based on a real example. 
The second step is to build upon these essential requirements (elicited from the document analysis) using brainstorming. With the brainstorming method, we can elicit new desired requirements creatively that can increase the business value to the EU Leadrship Team. The aim is to promote as many ideas as possible and selecting the most important through teamwork and collaboration. One of the challenges of using brainstorming is that the quality of the sessions can be limited by the Organization Politics or the interpersonal traits (Brainstorming, n.d.).
Nevertheless, as a result of this combined choice, we have able to have a more balanced approach to eliciting requirements. 
In fact we can ensure that we creatively think of all the potential uselful requirements, yet remaining pragmatic with an agreed set of key existing requirements from comparable documents. 

### Requirement specification method

Considering the choice of our methodology, Scrum, the best specification method are User Stories, however, we will also be using Use Cases for the more complex requirements related to tailoring data visualizations. We choose to use User Stories because we want to understand why the European Leadership Team requires specific features. With a simple format, user stories help us to understand requirements from a user perspective decribing clearly what the user would like to achieve (User Stories: What They Are And Why And How To Use Them, n.d.). This would allow us to understand why users might want a particular requirement and prioritize accordingly. With User Stories, we can also reiterate frequently with the customers, describing our understanding of the requirements in a non-technical way. In other words, this method can help us assess and adapt easily to the changing requirements. 
One of the challenges of this choice is that, given the many combinations of parameters (i.e. metrics, countries and years), user stories might not capture fully all the insights from data. Neverthelss, we can leverage the acceptence criteria and complement our analysis with user cases to be more specific about the data visualizations. Indeed, with so many parameters, Use Cases can help us specifically with the requirements related to tailoring the visualization and saving the preferences. As the these requirements are more complex, use cases will help us to ensure that we can clearly define pre-conditions, main and alternative flows. Detailed Use cases will also be used to analyse the log in requirements to facilitate the web app and relational database design.


### Prioritisation method

To prioritise our requirements, we chose forced ranking prioritisation. This method involves looking at any two requirements at the time and choose which one is more important collectively. The main resons why this is the best method for our project is becuase with forced ranking prioritiation, we can prioritise based on a give user role or persona (Wick, 2017). Not only this alighn very well with user stories, but it also allows us to choose requirements empathazing with what users from the leadrship Team need.

One advantage of this is that we can focus on two at the time, making it easier to rank what are the most importnant ranks. Similarly, this means that ranking the least importart will be more difficult and therefore one potential challenge of this method is agreeing on the least important requirements. Nevertheless, as we assume that requirements change, the precise rank of the least important requirements is not very important as we aim to iterate this prioritisation often. Another way of dealing with this challenge would be to divide groups in smaller ones when making a ranking decision.


### Documented and prioritised requirements
Link to the full list of documented and prioritised requirements.


#### User Stories
[Requirements - Prioritised User Stories.pdf](https://github.com/ucl-comp0035/coursework-1-MarcoLonardo/files/7758189/Requirements.-.Prioritised.User.Stories.pdf)

#### Detailed Use Cases
[Detailed Use Cases.pdf](https://github.com/ucl-comp0035/coursework-1-MarcoLonardo/files/7758192/Detailed.Use.Cases.pdf)


#### Use Case Diagram

<p align="center">
  <img width="762" alt="Use Case Diagram" src="https://user-images.githubusercontent.com/64501760/146814104-70deed63-b3d5-4eee-9bef-501faf7706c7.png">

</p>




## Design
### Structure and flow of the interface

#### Goals
To Model the User Interface, we decided to use Wireframes becuase they provide a prototype of the end product with the minimimal effort. In fact, without spending too many resources on the visual aspect, with Lo-Fi wireframes we can interate quickly to obtain feedback and refine existing requirements (Adojutelegan, 2021). Thus, it is a great way to complement our Scrum Methology and address the customers' changing requirements. 
With the requirements and the ensuing use case diagram identified in the previous section, we decided to wireframe starting with the main goals of the users. Thus, we categorized all the goals and sub-goals in the following way:

1. Access Account
  - Log in
  - Create Account
2. Visualize Data
  - Filter for parameters (Years, Country)
  - Modify Chart (Bar Chart, Line Chart)
  - Save Prefrences
  - Export Reports Offline
3.  Read News
  - Click on the article
  - Save the article
4. Access History
  - Previous Preferences
  - My Saved Articles


#### User Flows
At this point, before wireframing the main goals, it was necessary to understand the relationships among these goals. In other words, once we understood what the users would like to achieve using our web app, we needed to understand how the user would navigate from one goal to another. Using the goals above, we sketched the main user flows using the following flow chart. From the chart, we can observe that once the users signs in, there are four key goals he/she can achieve (in orange): Access Account, Visualize Data, Read News and Access History. Each of these goals would then allow the user to more advanced actions (in grey) defined as the sub-goals. 

<p align="center">
  <img width="811" alt="User Flow" src="https://user-images.githubusercontent.com/64501760/146958984-be863fbb-e1a0-4fbc-a6cd-aac151495869.png">

</p>


#### Wireframes
Finally, we were able to wireframe focusing specifically on the four main goals (Access Account, Visualize Data, Read News and Access History) and describing their relationships. When wireframing, we considered designing for desktop use. This is becuase we are assuming, as identified in the target audience section, the EU Leadership team has more familiary with PCs and laptops and these dashboards will have to be accessed at work. Each of the wireframes has a wireframe reference number allowing us to associate the wireframe with specific routes and controllers of our Model-View-Controller (MVC) application. In fact, The following Wireframes will represent the views of our MVC Application described in the next section. The flows among the different views are described in the the Wireframes Flows.pdf file.

[Wireframes.pdf](https://github.com/ucl-comp0035/coursework-1-MarcoLonardo/files/7757098/Wireframes.pdf)
[Wireframes Flows.pdf](https://github.com/ucl-comp0035/coursework-1-MarcoLonardo/files/7757099/Wireframes.Flows.pdf)


### Application structure

For our Flask web application, we are going to use the Model-View_Controller pattern. This model seprates the input, the processing and the output of the apps in three components: Models, Views and Controllers (Six Benefits Of Using MVC Model For Effective Web Application Development, n.d.). This separation can be very helpful for our project because if the requirements changes, these will not affect the whole architecture of the model.

#### Models
The first step is to design the models using the Data Driven Design (DDD) approach, where nouns, adjectives and verbs suggest classes, attributes and method, respectively. 
Thus, using User Stories, we selected the following 8 models for our app. Attributes and methods for each of the classes are defined in the with UML class diagrams below.

1. Account
2. Metric
3. Country
4. Year
5. Exports
6. Articles
7. Preferences
8. History


<p align="center">
  <img width="698" alt="Class Diagram UML" src="https://user-images.githubusercontent.com/64501760/146812327-a3033557-4fc2-46dd-b9ec-f4eb7e2884c3.png">
</p>

#### Routes and Controllers
At this point given the many number of flows among the models, we used the views (wireframes) and the user flows diagram to identify the the routes and the associated controller function. From the table below, we can see that, excluding the landing page (index), there are 8 routes, each of the routes correspond to a particular view (and therefore, user goal) we have identified in the wireframe section. The 9 routes and the relating controller functions are described in the following table.

<p align="center">
  <img width="754" alt="Route and Controllers" src="https://user-images.githubusercontent.com/64501760/146974502-98ab6c9e-96d3-4195-9a19-fcedb22aa7ba.png">


</p>



### Relational database design

#### Conceptual Design
For the database design, we firstly start with the conceptual database design by identifying the important entities, their attributes and the relationships among them. Similarly to identifying models in the application structure section, we can use the data driven approach (DDD) to identify the entities. Choosing the entities relevantly to our models and with a consistent approach will help us ensure that our database design is comprehensive of all the models we have identified. In other words, we can ensure that we plan for for every specific model if we are able to understand their position in the relational database design. Thus, we obtain the following list of entities:

1. Account
2. Metric
3. Country
4. Year
5. Articles
6. Preferences
7. History
8. Selection

As we can see, this list is very similiar to the list of our models. This similiarity will help us ensure that all the requirements of our web app will be considered from a database design perspective. Nevertheless, differently from the models, in entities we don't find Exports. This is because we are assuming that the files that will be exported are stored as a blob files. As these files cannot to be stored in a relational databese, we keep exports as a model but it will not be an entity of the relational database. Another difference is that selection has been added as an entity only to address normalisation in the logical design stage.
At this point, after having identified the attributes for each of the entities, we determine the relationships among entities and we describe thier cardinality using the Crow's Foot Notation. 

#### Logical Design
Having defined the database conceptually, we can now work with the logical database design where we can start to validate the relations using normalisation. Thorugh normalisation we can ensure that when structuring data into a table, we avoid update anomalies and reduce data redundancy. Thus, for each entity and its attributes (representing a table) we first identify the primary keys and the correspoding foreign keys in the other tables. Primary keys are defined with the attribute ID and they are integer and with the "auto increment" constraint. This ensures that each primary key represents a column guranteed to be unique for each record. Setting the constraints of the relevant attributes as unique and not null was also important for referential integrity, as we needed to ensure that data within the relationships was consistent and accurate. Indeed, it was necessary to ensure that for all the one-to-many relationships, the primary key in one tables becomes the foreign key in the other table. This makes it very clear to understand what are the common columns that link tables together. As a result, we could now eliminate redundant data because, through this process, we could split larger tables into small ones. For instance, instead of repeating the access date attribute both for articles and preferences, we can now retrive that attribute looking at the history entity. This allowed us to avoid transitive functional dependency, grouping attributes in a more efficient and meaningful way. 

Moreover, an additional key entity, Selection, has been added. Introducing this entity was very important for the process of normalisation, because initially the preference entity had a many-to-many relationship with the entities metric, year and countries. This is happening because we are assuming that the user can select as preferences multiple years, countries and metrics. Indeed, flexibility in tailoring the visualization is one of the key requirements identified in the user stories, therefore it was important to design the database accordinly. To achieve this, we had to break-down this many-to-many relationship introducing an additional table that would capture the selection of multiple attributes uniquely. A composite primary key has been considered for this particular scenario, nevertheless we believed it was worth adding the Selction entity to improve clarity and intuitiveness of the overall database design.

After describing the different contraints of each attribute we can describe our relational database design with the Entity Relationship Diagram below. 
Starting from the left we can see that to each account we have associated preferences and articles (linked with the User ID). These associations are decribed with the one-to-many relationships becuase one user can have zero or multiple preferences or articles but saved articles and preferences must have at least and at most one account.  
Articles and preferences have unique IDs, a title/name and are associated to History with the Record ID. History would allow to retrive the Access Date, Url and the record type which describes whether the saved obejct is an article or a preference. The relationships between History and Article/Preference is a one-to-many because Articles and preferences, if saved, must have at least one record. Assuming that an article/preference can be saved multiple times, a preference or article can have multiple records. One saved record, however, must have at least one article/preference to be associated to and cannot be associated to multiple articles/preferences. Moving on into preferences specifically, we see that they are associated to selection with the selection ID and a one-to-many relationship. While one preference needs to have at least one selection, one preference can be made up of multiple selections as assumed previously. Nevertheless, a selection needs to have at least one preference and can be associated at most to one preference only. Metric, Country and Year (with the respective IDs) are then linked to Selection (with the respective IDs) via a one-to-many relationships. Focusing on Country as an example, one selection needs at least one country but can include one country at the time. One country needs to be part of at least of a selection but it can be associated to multiple selections.


<p align="center">
  <img width="1020" alt="Relational Database Design" src="https://user-images.githubusercontent.com/64501760/146956273-42532b06-7199-4331-a05d-0f4c893202c2.png">
</p>




## Testing
### Choice of unit testing library

### Tests
The tests have been performed in the tests directory: https://github.com/ucl-comp0035/coursework-1-MarcoLonardo/tree/master/tests. 

After installing the pytest library ,from the sample user class code provided, we decided to focus on testing the following two methods for this project: create_full_name and calculate_age. We are assuming that perfoming unit testing on this code will help us test part of the Account model identified in the design section. Both of the tests have been determined and described below using the GIVEN-WHEN-THEN Approach. With this approach, we realized that the set-up condition is the same for both tests. Indeed, both methods (create_full_name and calculate_age) required us to create a new user for unit testing. Therefore, we used fixtures to provide a common function (general_user) for both tests, allowing us to reduce common code. As the fixture will need to be executed for each of the test functions (Gao, 2020), we will be using the "function" scope. Finally, each of the functions have been tested twice: both with the correct data and the incorrect data.

#### Test function 1: test_create_full_name
The first test function test_create_full_name aims to test whether the correct full name is returned for a new user. 
It can be, therefore, be described with the following GIVEN-WHEN-THEN Approach: 
   
   
    """
    GIVEN a new user (created as fixture) named James White
    WHEN his first_name and last_name are passed to the "create_full_name" function
    THEN the full_name should be James White

    """
    
#### Test Function 2: test_calculate_age 
The second function test_calculate_age aims to test whether the correct age is returned given the date of birth of a new user. It was necessary to convert the date of birth from string to date, in order to correctly test this function. It can be descibed with the following GIVEN-WHEN-THEN Approach: 
    
    """
    GIVEN a new user (created as fixture) born in 1998
    WHEN his date of birth (dob) is passed to the "calculate_age" function
    THEN the age should be equal to 23

    """
    
   

### Test results

Testing Results with Correct Data

<p align="center">
  <img width="1031" alt="image" src="https://user-images.githubusercontent.com/64501760/146686691-7f83aa62-25e4-4f05-9095-fd3890440c37.png">
</p>

Testing Results with Incorrect Data (for both functions)

<p align="center">
  <img width="1033" alt="image" src="https://user-images.githubusercontent.com/64501760/146686832-13f41cea-2067-4379-9460-78eec074a212.png">
</p>


Coverage Reports

<p align="center">
  <img width="1033" alt="image" src="https://user-images.githubusercontent.com/64501760/146687096-ec11636e-ba40-4962-8b8d-a9a022b7c11e.png">
</p>


<p align="center">
  <img width="1037" alt="image" src="https://user-images.githubusercontent.com/64501760/146687154-7bd1e7c9-fa22-4322-aaa0-324f947c68f6.png">
</p>


### Continuous integration (optional)
Consider using GitHub Actions (or other) to establish a continuous integration pipeline. If you do so then please provide a link to the .yml and a screenshot of the results of a workflow run.

.yml Link:https://github.com/ucl-comp0035/coursework-1-MarcoLonardo/blob/cfb6b5ebf1ca85627a4cea0ba0966ad79315eb65/.github/workflows/python-app.yml 

Results with correct data for both methods
<p align="center">
  <img width="778" alt="image" src="https://user-images.githubusercontent.com/64501760/146846644-9b4e9f7e-866b-4bc4-b845-43bb001f859d.png">
>
</p>

Results with incorrect data only for the calculate_full_name method

<p align="center">
  <img width="785" alt="GitHub CI Failure" src="https://user-images.githubusercontent.com/64501760/146847022-fc0470c2-0dc2-4cc8-8bce-863db965b5bf.png">
>
</p>


## References

1. BABOK Page. n.d. Document Analysis. [online] Available at: <https://babokpage.wordpress.com/techniques/document-analysis/> [Accessed 20 December 2021].
2. BABOK Page. n.d. Brainstorming. [online] Available at: <https://babokpage.wordpress.com/techniques/brainstorming/> [Accessed 20 December 2021].
3. Digite. n.d. User Stories: What They Are And Why And How To Use Them. [online] Available at: <https://www.digite.com/agile/user-stories/> [Accessed 20 December 2021].
4. Wick, A., 2017. Forced ranking prioritization - Agile Product Owner Role: Techniques Video Tutorial | LinkedIn Learning, formerly Lynda.com. [online] LinkedIn. Available at:    <https://www.linkedin.com/learning/agile-product-owner-role-techniques/forced-ranking-prioritization?autoAdvance=true&autoSkip=false&autoplay=true&resume=false&u=69919578>      [Accessed 20 December 2021].
5. Adojutelegan, J., 2021. Why you should add Wireframing to your design process | Marvel Blog. [online] Marvel Blog. Available at: https://marvelapp.com/blog/why-you-should-      add-wireframing-to-your-design-process/> [Accessed 20 December 2021].
6. Brainvire.com. n.d. Six Benefits Of Using MVC Model For Effective Web Application Development. [online] Available at: <https://www.brainvire.com/six-benefits-of-using-mvc-model-for-effective-web-application-development/> [Accessed 21 December 2021].
7. Gao, X., 2020. Understand 5 Scopes of Pytest Fixtures. [online] Medium. Available at: <https://betterprogramming.pub/understand-5-scopes-of-pytest-fixtures-1b607b5c19ed>        [Accessed 21 December 2021].



