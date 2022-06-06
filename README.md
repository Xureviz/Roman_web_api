# Application introduction
This program receives a String type and returns the highest roman number found on that String

# Build project with docker
docker-compose build

docker-compose up

## Postman
After building the project, let's try consuming it via Postman. <br><br>
Send a form-data to localhost:8000/search/ <br><br>
The API is waiting for a key "text". Now type a random String and send it with Post Method

# Access docker bash if needed

docker-compose run --rm app /bin/sh

# Remove docker containers

docker-compose down --remove-orphans
