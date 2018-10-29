Для развёртывания проекта у вас должен быть установлен "docker-compose"
1) docker-compose build
2) docker-compose up --remove-orphans
3) docker-compose run --rm django_project python ./manage.py createsuperuser --email admin@example.com --username admin
4) после старта  докера приложение будет доступно  http://127.0.0.1:8000
