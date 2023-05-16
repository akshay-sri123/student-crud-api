# student-crud-api

Simple CRUD (Create, Read, Update, Delete) REST API implementation.

## How to run

### Setup and configure postgresql on local

- Follow this [guide](https://techviewleo.com/how-to-install-postgresql-database-on-ubuntu/) to setup and configure postgresql on local
- Connect to psql and execute the following queries to create the database and set of credentials for this exercise
```
CREATE DATABASE student_crud_api;
CREATE USER app_user WITH PASSWORD 'app_pass123';
GRANT ALL PRIVILEGES ON DATABASE student_crud_api TO app_user;
```

### Initial python setup
- Install `make` utility: `sudo apt-get update && sudo apt-get install make`
- Run `make virtualenv` to setup python [virtual env](https://pypi.org/project/virtualenv/)
- Run `source .venv/bin/activate` to activate the virtualenv
- Run `make requirements` to install the python libraries


### Run the application
- To run on local: `make app_run_local`
- To run via docker: `make app_run_docker`
- To run via docker-compose: `app_run_docker_compose`

### Access the API

- Get
```
curl -s --location --request GET 'http://127.0.0.1:5000/get'
```

- Add
```
curl --location --request POST '127.0.0.1:5000/add' \ 
--header 'Content-Type: application/json' \
--data-raw '{
    "address": "Mon Cala",
    "email_id": "elder_squid@moncala.marai",
    "gender": "Male",
    "name": "Admiral Ackbar",
    "date_of_birth": "3028-09-11"
}'

```

