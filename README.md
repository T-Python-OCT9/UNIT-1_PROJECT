# UNIT-1_PROJECT-ghadah

## Based on what you’ve learned until now , create a project of your choosing (impress us with your imagination) . This project must at least satisfy the following minimum requirements :

- Must be interactive on CLI. done 
- Use lists or dictionaries or tuples. done 
- Use loops. done 
- Use functions that return an output . done
- Use a Lambda function. done 
- Use at least 1 Class. done 
- Use some form of Error Handling . done
- Organize Your Code into modules & (or packages) done 

## Helper Bot : a chatbot for a website that provide IT_courses :

#### Overview : the helper bot is a chatbot for a courses website , that answers user questions by typing an option , the main actor in this chatbot is the student , 3 classes were created : courses , custserv(customer servise) , student 
#### this program enables the following tasks :
-list the most asked questions for the user. 
-list the avalible courses.
-complain or suggest student's opinion.
-rigster in a course.
-view courses prices.

The courses class have these methods:
-avalible_courses(): this method returns a list with the avalible courses 
-courses_price(): this method takes the name of the course and prints the price of the course 

the custserv(customer service) class have these methods:
-most_asked_QI():that prints the most asked questions from the most_askes.txt file 
-omplaints_suggestions():that enables the user to give a feedback , and write it in the omplaints and suggestions.txt file 
-service_rating(): that enables the user to rate the service. 
-get_rating() : that prints the mean of the rating the user has entered.

the student class have these methods:
-course_registration() : that enables the user to rigster in a course. 


#### Usage :
 Explain to the user how to use your project . 
 -type 1: to list most asked questions.
 -type 2: if you want to list the avalible courses
 -type 3: If you want to complain or suggest your opinion.
 -type 4: if you want to rigster in any course.
 -type 5: if you want to view a course price.
 -if you type exit you will be asked to rate the service from 1 to 5 , where 1 means that you didn't like us , and 5 means that our service was good. 

### For your project. Edit this README.md file to include your own project name,  overview, user stories, and usage. 
