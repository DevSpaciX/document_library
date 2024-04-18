# Library
This test task is created for organizing a library with the ability to search for books by authors, titles, and library clients. It also includes functionality for tracking the return dates of borrowed materials, including color highlighting for those who have overdue returns, those with a week left until the deadline, and those whose returns are on schedule. Additionally, it provides the ability to view debtor data for communication purposes.

## Instructions for running the project
1. Project dependencies: All project dependencies are stored in the requirements.txt file. Make sure you have all the necessary libraries installed by installing them according to this file.

2. Django version: The project uses Django version 1.8.5. Make sure that this exact version of Django is installed.

3. Database: PostgreSQL database is used. Make sure you have PostgreSQL installed and configured.

4. Docker: The project can be run using Docker. Find the instructions below.

To run the project using Docker, follow these steps:
1. Clone the repository. 
2. Navigate to the project directory.
3. Run the following command to build the Docker image:
```docker-compose up```
4. Wait till the image is built and the project is running.
5. Main page of the project will be available at http://0.0.0.0:8000/books/

## Environment variables
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=postgres
SQL_USER=postgres
SQL_PASSWORD=postgres
SQL_HOST=db
SQL_PORT=5432