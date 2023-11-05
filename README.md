# College Management System

-----

# The total set of APIs is provided below:
/home - returns the mail URLS for the above processes

POST `/student/register` - register a new student to the database

GET `/student/get-all-students` - get all students from the database

GET `/courses/get-all-courses` - get all courses from the database

POST `/courses/add-new-course` - add a new course to the database

DELETE `/courses/delete-course/{courseId}` - delete a course from the database

POST `results/add-score-matrix/` - adds score from a course for an individual from the database

DELETE `results/delete-score-matrix/` - delete s score from a course for an individual from the database

GET `/home` - set of links provided for th homepage

----
# Database

A postgres database has been used for our app. This is a hosted database on elephantsql.com with credentials stored in .env.

----

# Testing APIs:

A working version of the app can be found at `https://petco-assignment-46f2215afbed.herokuapp.com/docs`

----

# Local Install:

Instructions have been provided for a local install of the app

Assuming the operating system is Ubuntu:

Esure the following packages are installed to take advantage of psycopg package required for Postgres connector.
`$ sudo apt install build-essential`
`$ sudo apt-get install libpq-dev`

----

## A virtual environment venv is recommended to run the program:
```
`$ python3 -m venv venv`
`$ source venv/bin/activate`
```

----

## How to install depedencencies:
```
`$ pip3 install psycopg2-binary`
`$ pip3 install -r requirements.txt`
```
----
## Install environment variables
`$ set -a`

`$ source .env`

`$ set +a`

----

## How to run program:
```
$ python3 app.py
```
