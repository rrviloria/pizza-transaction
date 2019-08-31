# pizza-transaction

This is the main repository for Raymund's Pizza Transactions

## Development environment


This was initially created using:

* MacOs version 10.12.6
* Docker version 17.12.0
* docker-compose version 1.18.0

## Setup environment
1) Clone this repo
```
git clone https://github.com/rrviloria/pizza-transaction.git
```
2) In the main directory (`manage.py` current directory) create a `.env` file with the following contents:

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
DB_USER=postgres
DB_HOST=db
DB_PORT=5432
```

3) run `docker-compose up`
4) visit `http://localhost:8080`

## Running seed
Instructions on how to set initial data can be seen here:

https://github.com/rrviloria/pizza-transaction/wiki/Setting-initial-data

## Running PEP8 check
Instructions on how to run PEP8 check(lint):

https://github.com/rrviloria/pizza-transaction/wiki/Running-PEP8-lint

## Running tests
Instructions on how to run tests:

https://github.com/rrviloria/pizza-transaction/wiki/Running-tests


## REST APIs
Instructions on how to query REST APIs can be seen here:

https://github.com/rrviloria/pizza-transaction/wiki/REST-APIs


## Additional information

Package versions are specified in Dockerfile / Pipfile and this is just for refference, but containerised application is using:

| Name                   | Version   |
| ---                    | ---       |
| Python                 | 3.7.7     |
| PostgreSQL             | 11.3      |
| Django                 | 2.2.2     |
