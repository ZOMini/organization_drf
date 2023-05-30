```
Проект работает:
http://130.193.37.228:9003/
un: ee-2@ya.ru / pw: Vitaliya  -(superuser)
```
[![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](http://130.193.37.228:9003/api/docs/)
[![foodgram workflow](https://github.com/zomini/foodgram-project-react/actions/workflows/main.yml/badge.svg)](https://github.com/zomini/zomini/foodgram-project-react/actions/workflows/main.yml)

- "Пользователь должен состоять в организации" и "Доступ к созданию организации имеют только авторизованные пользователи", так как пользователя можно создать и авторизовать, если еще нет его организации... Решение: Создание организации возможно без авторизации.

## Запуск проекта:
  - docker-compose up --build
  - Далее все автоматом запустится - тестируем

## Тестирование ручек
  - Я использовал Rest Client (плагин для VSC) см. 
  - Можно тестировать через документацию(далее c базовыми настройками):
    - http://127.0.0.1:8000/swagger-ui/
    - {create_organization} - {post}/create_organization/ (не ограничена пермишенами, иначе не как) - создаем организацию - вернется id, он нужен для регистрации пользователя
    - {auth} - {post}/auth/users/ - регаем пользователя
    - {auth} - {post}/auth/jwt/create/ - получаем пару токенов, нам нужен access token
    - access token вставляем в Authorize(верхний правый угол на странице документации) в поле Value - "Bearer {access token}"
    - тестируем ручки по заданию, блок {auth} можно свернуть.

## Тестирование админки
  - При деплоее автоматичесуи создается superuser (admin@example.com/qwer1234)
  - Логинемся и тестируем.