## Разворачивание проекта
- cp example.env .env
- заполнить .env файл(необязательно)
- docker-compose build
- docker-compose up
- docker exec -it <название контейнера заканчивающееся на _web_1 или -web-1> python manage.py migrate

## запуск тестов
- docker exec -it <название контейнера заканчивающееся на _web_1 или -web-1> python manage.py test

## админка
- docker exec -it <название контейнера заканчивающееся на _web_1 или -web-1> python manage.py createsuperuser
- заходим на свой хост (по дефолту 127.0.0.1:8000)+/admin/

