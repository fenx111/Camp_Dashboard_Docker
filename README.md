docker-compose up -d --build
docker-compose exec web python manage.py makemigrations vitacamp --noinput
docker-compose exec web python manage.py migrate --noinput
docker-compose exec web python manage.py createsuperuser