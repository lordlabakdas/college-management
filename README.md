# College Management System

-----

The total set of APIs is provided below:
/home - returns the mail URLS for the above processes

Post `/student/register` - register a new student to the database

Get `/student/get-all-students` - get all students from the database

GET `/courses/get-all-courses` - get all courses from the database

POST `/courses/add-new-course` - add a new course to the database

DELETE `/courses/delete-course/{courseId}` - delete a course from the database

DELETE `results/delete-entity/` - delete an entity or entities from the database

----

Documentation and testing:

Testing and documentation has been dont using `swagger` at 127.0.0.1:8001/docs

----

Database: 

Postgres has been used for the database. The service used for this purpose is elephantsql.com.

----

A virtual environment venv is recommended to run the program:
```
$ python3 -m venv venv
$ source venv/bin/activate
```

----

How to install depedencencies:
```
$ pip3 install -r requirements.txt
```

----

Logging:

`Loguru` was used for logging purposes. The logs are stored in the logs folder.

----

How to run program:
```
$ python app.py if in venv else python3 app.py
```
