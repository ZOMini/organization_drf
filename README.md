# Организации(Тестовое задание)
  - текст задания [test task](https://github.com/ZOMini/organization_drf/blob/f759906f3f3332bdd7bef1e5754d0981d79537ee/test_task.txt)

## Нюансы
  - "Пользователь должен состоять в организации" и "Доступ к созданию организации имеют только авторизованные пользователи", так как пользователя можно создать и авторизовать, если еще нет его организации... Решение: Создание организации возможно без авторизации.

## Запуск проекта:
  - заполняем .env в корне проекта, см. .env.template
  - docker-compose up --build
  - Далее все автоматом запустится - тестируем

## Тестирование ручек
  - Я использовал [Rest Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)(плагин для VSC) см. [requests.http](https://github.com/ZOMini/organization_drf/blob/ec7b856d7f182b471b333851a876845805b69889/requests.http)
  - Можно тестировать через документацию(далее c базовыми настройками):
    - http://127.0.0.1/swagger-ui/
    - {create_organization} - {post}/create_organization/ (не ограничена пермишенами, иначе не как) - создаем организацию - вернется id, он нужен для регистрации пользователя
    - {auth} - {post}/auth/users/ - регаем пользователя
    - {auth} - {post}/auth/jwt/create/ - получаем пару токенов, нам нужен access token
    - access token вставляем в Authorize(верхний правый угол на странице документации) в поле Value - "Bearer {access token}"
    - тестируем ручки по заданию, блок {auth} можно свернуть.

## Тестирование админки
  - При деплоее автоматичесуи создается superuser (admin@example.com/qwer1234)
  - http://127.0.0.1/admin/ Логинемся и тестируем.

## Тестирование ws chat
  - http://127.0.0.1/ws/
    - логин/пароль
    - чатимся
    - если нужно 2-а пользователя - то разные логин/пароль и браузеры

  - ниже не актуально, но пока оставил.
  - docker-compose -f docker-compose_dev.yaml up
  - из папки приложения /events:
    - python script.py
    - python manage.py runserver
  - логинемся(например суперюзером admin@example.com/qwer1234):
    - 127.0.0.1:8000/ws/auth/login/   для cookie ws 
  - чатимся:
    - 127.0.0.1:8000/ws/ 
  - если нужен второй пользователь, запускаем ДРУГОЙ браузер, регаем 2-го пользователя(через админку), логинемся, чатимся.
  - [2-а пользователя](https://github.com/ZOMini/organization_drf/blob/769749cdf168b866c20b93782ec7c13f68ebb882/chat.jpg)
  - p.s. nginx & django+WS пока победить не удалось(.
