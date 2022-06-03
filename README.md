# Application introduction
This program receives a String type and returns the highest roman number found on that String

# Build project with docker
docker-compose build

docker-compose up

# Access docker bash

docker-compose run --rm app /bin/sh

# Pylint and test

docker-compose run --rm app pylint --load-plugins pylint_flask /romano_web_api/app

docker-compose run --rm app pytest -vvv --cov=.

# Remove docker containers

docker-compose down --remove-orphans
