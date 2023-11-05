# Book Collection Project - <a heaf = "https://drive.google.com/file/d/1w7_NEWz_kk9VfX4JPiIZYj6JqWzrsDta/view?usp=sharing" > Video Link </a>

This GitHub repository hosts a Django project with *Django Rest Framework* that creates a **RESTful API** for managing books. It meets the following project requirements:
<br> &ensp; &#9745; offering operations to list all books, 
<br> &ensp; &#9745; retrieve books by ID,
<br> &ensp; &#9745; add new books,
<br> &ensp; &#9745; update existing ones,
<br> &ensp; &#9745; and delete entries. 
<br> Furthermore, it extends functionality to allow:
<br> &ensp; &#9745; partial updates of book records. 
<br> This includes endpoints for specific field updates with thorough **validation, ensuring data integrity**. 
<br> Error responses are provided for invalid input. 
<br> This repository serves as a practical demonstration of building a **robust RESTful API** using Django and Django Rest Framework, showcasing features like partial updates and data validation.

# Table of Contents

- [Prerequisites](#pre-req)
- [Getting Started](#gettinStart)
- [Running the Application](#run-app)
- [API](#api-endpoints)
- [Error Handling](#error-hand)
- [Dependencies](#depen)
- [Conclusion](#conc)


<a id="pre-req"></a>
## Prerequisites
Before you begin, ensure you have the following installed:
- Python: <a href = "https://www.python.org/downloads/"> Download and install Python </a>
- Git: <a href = "https://git-scm.com/downloads"> Download and install Git </a>

<a id="gettinStart"></a>
## Getting Started
1. Clone the repository to your local machine, and navigate into it,
```
git clone git@github.com:prabhxjottsingh/book-api.git
cd .\book-api\
```
2.Create a .env file in the project root directory using the following terminal command and enter the virtual enviroment,  
```
virtualenv venv
venv/scripts/activate
```
3. Install project dependencies by running, 
```
pip install -r requirements.txt
```
4. Activate the database and make the migrations,
```
python manage.py makemigrations
python manage.py migrate
```
5. In the end, don't forget to get out of the virtual environment using the command,
```
deactivate
```

<a id="run-app"></a>
## Running the application
To start the Bookstore Management System on local system, use the following command: 
```
python manage.py runserver
```
This will start the server, and you should see a message indicating that the server is running on the specified port.

<a id = "api-endpoints"> </a>
## API endpoints
The system provides the following API endpoints for managing CRUD operation, along with validation:

```
GET    /books                       : Retrieve all books
GET    /books/{id}                  : Retrieve single book by id
POST   /books/                      : Create a new Book
DELETE /books/{id}                  : DELETE an existing book
PUT    /books/{id}/partial-update/  : Partially update an existing book
```

<a id = "error-hand"> </a>
## Error Hadnling
Creating or updating a book with wrong information will give an error.

<a id = "depen"></a>
## Dependencies
The system uses the following main dependencies:
```
Python: A versatile and high-level programming language.
Django: A Python web framework for building web applications.
Django Rest Framework: A powerful tool for creating RESTful APIs in Django.
```

<a id = "conc"></a>
## Conclusion
```
You now have the Bookstore Management System up and running on your local machine. Use the provided API endpoints to manage book records in your bookstore. 
Customize and extend the system according to your needs.
```
