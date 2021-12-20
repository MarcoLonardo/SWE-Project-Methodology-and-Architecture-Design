# Coursework 2

Most students will use the same repository for coursework 2. You may use this file to present the results of that
coursework if you wish. Alternatively you can use video or audio to provide the explanations instead of writing them.

## Requirements definition and analysis
The term 'requirements' is used in the broader sense, user stories and/or use cases may be used.

Working with our customer the EU Commission and considering the problem statement, the DataFirst has created a context diagram to agree and define the scope of the web app. 

<p align="center">
  <img width="727" alt="Context Diagram" src="https://user-images.githubusercontent.com/64501760/145560609-43bf0b4c-20a9-49ec-aad6-23656ed6632d.png">
</p>


From the context diagram,  we can see that the primary function of the web app is to provide inisghts to  the European Leadership Team with a visualization dashboard.
Nevertheless, twith the diagram, we could identify a few additional features relevant to EU Leadership Team's needs. The first one is a news feature displaying stories from relevant third-party Newspapers. News and articles from these newspapaers feed into the website, allowing the EU Team to assess the public sentiment over key deveopment areas. Moreover, another requested functionality is to allow users to tailor visualzations and save preferences. This means that it will be essential to allow users to access their accounts to access history of previous queries and articles.

### Requirements identification methods

To elicit requirements for this project, we decided to use the following methods: Document Analysis and Brainstorming. As the client has not been very specific in the deliverables, we believe that this combination is the best way to elict requirements because we can creatively think of the client's desired features while remaining pragmatic with real and comparable solutions. In fact, firstly, we would use document analysis to enrure that we capture with no ambiguity the main and most essential requirements from existing solutions. This is a great way to address the client's vague description becuase we can refer to existing examples. As a comparable example for document analysis, we would mainly levarage the World Bank Platform, to understand what requirements and details are relevant to the web application we are building. Reviewing and confirming these requirements with the client will be essential becuase we are able to capture requirements based on a real example. 
The second step is to build upon these essential requirements (elicited from the document analysis) using brainstorming. With the brainstorming method, we can eliciti new desired requirements creatively, helping the team provide can help us provide more value. The aim is to promote as many ideas as possible and selecting the most important through. One of the challenges of using brainstorming is that the quality of the sessions can be limited by the Organization Politics or the intersonal traits (reference, the EU Team in this case). Nevertheless, as a result of this combined choice, we have able to have a more balanced approach to eliciting requirements. 
In fact we can ensure that we creatively think of all the potential uselful requirements, yet remaining pragmatic with an agreed set of key existing requirements from comparable documents. 

https://babokpage.wordpress.com/techniques/document-analysis/
https://babokpage.wordpress.com/techniques/brainstorming/

### Requirement specification method

Considering the choice of our methodology, Scrum, the best specification method are User Stories, however, we will also be using Use Cases for the most crucial requirements. We choose to use User Stories because we want to understand and priorize well the needs of the European Leadership Team. With a simple format, user stories help us to understand requirements from a user perspective decribing crearly what the user would like to achieve. This would allow us to understand why users might want a particular requirement and priotise accordingly. With USer Stories, we can also reiterate frequently with the customers, describing our understanding of the requirements in a non'technical way. In other words, this method can help us assess and adapt easily to the changing requirements. 
One of the challenges as a result of this choice is that with user story we might  not capture the whole value of data and the insights. Neverthelss, given the changing requirements, meeting the expectations is our key prioroty and we can leverage the acceptence criteria as a way to be more specific about each functional requirement. Moreover, the most critical and data'oriented aspects of the requirements will be analysed with use cases to ensure that crucial data insights are not lost.

https://www.digite.com/agile/user-stories/

### Prioritisation method

To prioritise our requirements, we chose forced ranking prioritisation. This method involves looking at any two requirements at the time and choose which one is more important collectively. The main resons why this is the best method for our project is becuase with forced ranking prioritiation, we can prioritise based on a give user role or persona. Not only this alighs very well with user stories, but it also allows us to choose requirements empathazing with what users from the leadrship TEam want or need.

One advantage of this is that we can focus on two at the time, making it easier to rank what are the most importnant ranks. Similarly, this means that ranking the least importart will be more difficult  and therefore one potential challenge of this method is agreeing on the least importnat requirements. Nevertheless, as we assume that requirements change, the precise rank of the least important requirements is not very important as we aim to iterate this prioritisation often. Another way of dealing with this challenge would be to divide groups in smaller ones when making a ranking decision.

https://www.linkedin.com/learning/agile-product-owner-role-techniques/forced-ranking-prioritization?autoAdvance=true&autoSkip=false&autoplay=true&resume=false&u=69919578

### Documented and prioritised requirements
Link to the full list of documented and prioritised requirements.

[Requirements - Prioritised User Stories.pdf](https://github.com/ucl-comp0035/coursework-1-MarcoLonardo/files/7748576/Requirements.-.Prioritised.User.Stories.pdf)


<p align="center">
  <img width="762" alt="Use Case Diagram" src="https://user-images.githubusercontent.com/64501760/146814104-70deed63-b3d5-4eee-9bef-501faf7706c7.png">

</p>


## Design
### Structure and flow of the interface

To Model the User Interface, we decided to use Wireframing becuase they provide a prototype of the end product with the minimimal effort. In fact, without spending too many resources on the visual aspect, with Lo-Fi wireframes we can interate quickly to obtain feedback and refine existing requirements (https://marvelapp.com/blog/why-you-should-add-wireframing-to-your-design-process/). Thus, it is a great way to complement our Scrum Methology and address the customers' changing requirements. 
With the requirements and the ensuing use case diagram identified in the previous section, we decided to wireframe starting with the main goals of the users. Thus, we categorized all the goals and sub-goals in the following way:

1. Access Account
  - Log in
  - Create Account
2. Visualize Data
  - Filter for parameters (Years, Country)
  - Modify Chart (Bar Chart, Line Chart)
  - Save Prefrences
  - Export Reports Offline
3 . Read News
  - Click on the article
  - Save the article
4. Access History
  - Previous Preferences
  - My Saved Articles



At this point, before wireframing the main goals, it was necessary to understand the relationships among these goals. In other words, once we understood what the users would like to achieve using our web app, we needed to understand how the user would navigate from one goal to another. Using the goals above, we sketched the main user flows using the following flow chart. From the chart, we can observe that once the users signs in, there are three key goals he/she can achieve (in orange): Access Account, Visualize Data, Read News and Access History. Each of these goals would then allow the user to more advanced actions (in grey) defined as the sub-goals. 

<p align="center">
  <img width="808" alt="User Flow" src="https://user-images.githubusercontent.com/64501760/146827346-ba90daa1-84a2-4aaa-80dc-e540d52094ad.png">
</p>


Finally, we were able to wireframe focusing specifically on the main goals (Access Account, Visualize Data, Read News and Access History) and describing their relationships. When wireframing, we considered designing for desktop use. This is becuase, as identified in the target audience, the EU Leadership team has more familiary with PCs and laptops and these dashboard will have to be accessed at work. Each of the wireframes has a wireframe reference number allowing us to associate the wireframe with specific routes and controllers of our Model-View-Controller (MVC) application. The following Wireframes will, in fact, represent the views of our MVC Application described in the next section.

### Application structure

For our Flask web application, we are going to use the Model-View_Controller pattern. This model seprates the input, the processing and the output of the apps in three components: Models, Views and Controllers. This separation can be very helpful for our project becuase if requirements changes do not affect the whole architecture of the model https://www.brainvire.com/six-benefits-of-using-mvc-model-for-effective-web-application-development/.

The first step is to design the models using the Data Driven Design (DDD) approach, where nouns, adjectives and verbs suggest classes, attrtibutes and method, respectively. 
Thus, using User Stories, we selected the following 8 models for our app. Attributes and methods for each of the classes is defined in the with UML class diagrams below.

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


At this point given the many number of features and flows among them, we used the views (wireframes) to identify the URL and the associated controller function. From the table below, we can see that, excluding the landing page (index), there are 8 routes, each of the routes correspond to a particular view (and therefore, user goal) we have identified in the wireframe section. The 9 routes and the relating controller functions are described in the following table.

<p align="center">
  <img width="759" alt="Route and Controllers" src="https://user-images.githubusercontent.com/64501760/146827296-ed4eaf5a-7306-4f58-932a-5d010d3099b4.png">
</p>



### Relational database design


<p align="center">
  <img width="1014" alt="Relational Database Design" src="https://user-images.githubusercontent.com/64501760/146812275-d427ffdd-0600-4e33-8157-7fdea351a179.png">
</p>



## Testing
### Choice of unit testing library

### Tests
The tests have been performed in the tests directory: .

After installing the pytest library, two tests have been peformed for this project. From the sample user class code provided, we decided to focus on testing the following two methods for this project: create_full_name and calculate_age. We are assuming that perfoming unit trsting on this code will help us test part of the User Class identified in the design section. Both of the tests have been determined and described below using the GIVEN-WHEN-THEN Approach. With this approach, we realized that the set-up condition is the same for both tests. Indeed, both methods (create_full_name and calculate_age) required us to create a new user for unit testing. Therefore, we used fixtures to provide a common function (general_user) for both tests, allowing us to reduce common code. As we have to do one test for each of the text functions, we will be using the "function" scope. Finally, eahc of the functions have been tested twice: both with  the correct data and the incorrect data.

The first test function test_create_full_name aims to test whether the correct full name is returned for a new user. 
It can be, therefore, be described with the following GIVEN-WHEN-THEN Approach: 
   
   
    """
    GIVEN a new user (created as fixture) named James White
    WHEN his first_name and last_name are passed to the "create_full_name" function
    THEN the full_name should be James White

    """
  
The second function test_calculate_age aims to test whether the correct age is returned given the date of birth of a new user. It was necessary to convert the date of birth from string to date, in order to correctly test this function. It can be descibed with the following GIVEN-WHEN-THEN Approach: 
    
    """
    GIVEN a new user (created as fixture) born in 1998
    WHEN his date of birth (dob) is passed to the "calculate_age function"
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

BABOK Page. n.d. Document Analysis. [online] Available at: <https://babokpage.wordpress.com/techniques/document-analysis/> [Accessed 20 December 2021].

BABOK Page. n.d. Brainstorming. [online] Available at: <https://babokpage.wordpress.com/techniques/brainstorming/> [Accessed 20 December 2021].


Digite. n.d. User Stories: What They Are And Why And How To Use Them. [online] Available at: <https://www.digite.com/agile/user-stories/> [Accessed 20 December 2021].


Wick, A., 2017. Forced ranking prioritization - Agile Product Owner Role: Techniques Video Tutorial | LinkedIn Learning, formerly Lynda.com. [online] LinkedIn. Available at: <https://www.linkedin.com/learning/agile-product-owner-role-techniques/forced-ranking-prioritization?autoAdvance=true&autoSkip=false&autoplay=true&resume=false&u=69919578> [Accessed 20 December 2021].



Adojutelegan, J., 2021. Why you should add Wireframing to your design process | Marvel Blog. [online] Marvel Blog. Available at: <https://marvelapp.com/blog/why-you-should-add-wireframing-to-your-design-process/> [Accessed 20 December 2021].




