# Запуск
## Шаг 1
```docker-compose up -d --build```
## Шаг 2
```docker-compose exec web python manage.py createsuperuser```

Введите логин и пароль для входа в админскую панель

## Примеры запросов
1. http://127.0.0.1:8000/get_countries/
2. http://127.0.0.1:8000/get_leagues_by_country/?country=Spain
3. http://127.0.0.1:8000/get_teams_by_league/?league_name=Spanish+La+Liga+2


## Что можно улучшить
1. Написать тесты
2. Добавить обновление существующих данных
3. Сменить бд
4. Сделать модели snake case
5. Добавить логгирование
6. Улучшить обработку ошибок
