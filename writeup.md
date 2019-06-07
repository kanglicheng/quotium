This is a document explaining the decisions that were made while building this application.

General Structure- Built in django, lots of great built in features and the web framework I have the most experience using.
Decided not to separate the frontend and backend codebases since I'm not using react, webpack. It's an application with only a few views so sticking to the django's template system seemed appropriate. The javascript bootstrap library and some custom css 
will provide all the styling I need. I treated building this application as building the basic foundation for a bigger more complex application. 

Accounts- Since this is a service that presumably is collecting data in exchange for a user taking the time to enter 
some information, I felt it would be best to not require signing up for an account in order to get an estimate. This 
should maximize the number of users willing to complete the process. For future development, I would probably redirect to a
page asking the user to sign up for an account so they can see and manage their own submissions and also just connect with 
the platform for various purposes. 

Admin accounts- Since we are collecting some personal data, I imagined the number of admin accounts should be pretty small and
strictly controlled. Therefore I did not create a registration view and will manually create admin accounts as needed.
I purposefully made the login icon somewhat discrete, since only a few people will need to access that. Perhaps it would be 
even better to let the admin login through a completely separate view, so I don't have a mysterious login page that's publicly
viewable. In django customizing the django-admin dashboard would accomplish this. 


API call- The prompt asked that the quote be produced by calling an API. This made sense, generating the quote is probably
a complex task in reality so it'd be best to have the "quote engine" be it's own application. The data being communicated
is of very small size so the network communication is not a concern. Also the api can be more easily shared by other 
potential applications.

API design and implementation - The API is a simple flask application that currently only supports a single POST request and without CORS enabled will not accept client side application calls. The api is responsible for producing the 3 pieces of data (airbnb yearly, full-home yearly, and renter-yearly) and also checks whether or not an estimate should be returned. I decided to have this check be performed on the api side so the implementation on the application side can be simpler. However, this restricts this route to be more tied to quotium. If there are potentially multiple applications calling this API, it would make more sense to add a route for each estimate, allowing the API's resources to be used more generally. 

This API currently has no authentication checks but in actual production I would add token based authentication over HTTPS only. 

Database and Schema- I chose postgresql because it is well-supported by Heroku and the structure of the data can be readily
modelled by relational databases. I have a schema for the submission form (PropertyData) and a schema for the submission record
(QuoteRecord), which is just all the information that was submitted plus the returned estimate and a creation date for better organization. It made sense to have PropertyData be a foreign key of QuoteRecord (1 to 1 relationship), since each Quote must be tied to an initial submission. I chose atomic transaction to ensure consistency between the two models. 

Form Validation- I did not think of a great way to perform address validation, which was the one difficult form validation. In production I would probably add geohashing or use an actual address validation API to filter out fake addresses.

