# RosCos_Task
Test task for roscos.

# Запускаем через Docker
## Клонируем репозиторий:
```
git clone https://github.com/RussianProgram/RosCos_Task.git
```

## Билдим образы в docker-compose
```
cd /RosCoc_Task
docker-compose up
```
## Создаем миграции и суперюзера
```
docker-compose exec backend python manage.py makemigrations music
docker-compose exec backend python manage.py migrate
```
## Заполним бд тестовыми данными из to_postgres.json
```
docker-compose exec backend python manage.py makemigrations loaddata to_postgres.json
```

## Готово! 
Фронт-клиент: http://localhost:8080/
Бэк: http://127.0.0.1:8000/api/albums
