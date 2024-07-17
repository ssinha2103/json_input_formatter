#!/bin/bash

# Stop and remove existing containers
docker stop web
docker stop db
docker rm web
docker rm db

# Build the Docker image
docker build -t json_input_formatter .

# Run the PostgreSQL container
docker run -d --name db -e POSTGRES_DB=django -e POSTGRES_USER=django -e POSTGRES_PASSWORD=django -v postgres_data:/var/lib/postgresql/data postgres:13

# Run the Django application container
docker run -d -p 8000:8000 --name web --link db:db -e DATABASE_URL=postgres://django:django@db:5432/django json_input_formatter

docker-compose run web python manage.py migrate