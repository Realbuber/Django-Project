# Django-Project

step:
if you are a Mac user and your chip is M1 or M2, then you need to enter this command first:
-> export DOCKER_DEFAULT_PLATFORM=linux/amd64

1.  build the Docker
    run command -> docker-compose -f local.yml up --build -d --remove-orphans

2.  make migration
    run command -> docker-compose -f local.yml run --rm api python manage.py makemigrations

3.  migrate
    run command -> docker-compose -f local.yml run --rm api python manage.py migrate

4.  create super user
    run command -> docker-compose -f local.yml run --rm api python manage.py createsuperuser
