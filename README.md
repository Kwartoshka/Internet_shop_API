# Дипломный проект по курсу «Django: создание функциональных веб-приложений»

Вашему вниманию представляется API для интернет-магазина.
Реализовано API сервиса и интерфейс администрирования. В качестве фреймворка использованы Django и Django REST Framework.

В качестве решения предоставлен код и тесты.


## Описание API

Сущности:

### Товар

url: `/api/v1/products/`

Поля:

- название
- описание
- цена
- дата создания
- дата обновления

Доступные действия: retrieve, list, create, update, destroy.

Создавать товары могут только админы. Смотреть могут все пользователи.

Есть возможность фильтровать товары по цене и содержимому из названия / описания.

### Отзыв к товару

url: `/api/v1/reviews/`

- ID автора отзыва
- ID товара
- текст
- оценка от 1 до 5
- дата создания
- дата обновления

Доступные действия: retrieve, list, create, update, destroy.

Оставлять отзыв к товару могут только авторизованные пользователи. 1 пользователь не может оставлять более 1го отзыва.

Отзыв можно фильтровать по ID пользователя, дате создания и ID товара.

Пользователь может обновлять и удалять только свой собственный отзыв.

### Заказы

url: `/api/v1/orders/`

- ID пользователя
- позиции: каждая позиция состоит из товара и количества единиц
- статус заказа: NEW / IN_PROGRESS / DONE
- общая сумма заказа
- дата создания
- дата обновления

Доступные действия: retrieve, list, create, update, destroy.

Создавать заказы могут только авторизованные пользователи. Админы могут получать все заказы, остальное пользователи только свои.

Заказы можно фильтровать по статусу / общей сумме / дате создания / дате обновления и продуктам из позиций.

Менять статус заказа могут только админы.


### Подборки

url: `/api/v1/product-collections/`

- заголовок
- текст
- товары в подборке
- дата создания
- дата обновления

Доступные действия: retrieve, list, create, update, destroy

Создавать подборки могут только админы, остальные пользователи могут только их смотреть.


## Интерфейс администратора

* Редактирование и просмотр подборок.
* Редактирование и просмотр товаров.
* Просмотр списка заказов пользователей, отсортированных по дате создания, с указанием пользователя и количества товаров.
* Страница детализации заказа с просмотром списка заказанных товаров.
* Редактирование и просмотр отзывов.

## Тестирование

В качестве Test Runner'а использован `pytest`.

## Инструкции

Для запуска проекта необходимо:
1. Создать базу данных PostgreSQL:
   ```` sql
    CREATE USER basic with password basic1;
    CREATE DATABASE basic_db WITH OWNER basic;
    ALTER USER basic CREATEDB;
   
2. Установить зависимости:
   ````
    pip install -r requirements.txt
   
3. Произвести миграции:
   ````
   python manage.py migrate
   
4. Загрузить тестовые данные:
   ````
   python manage.py loaddata fixture.json

5. Для запуска сервера выполнить команду:
    ````
    python manage.py runserver

6. Для запуска тестов выполнить команду:
   ````
   pytest