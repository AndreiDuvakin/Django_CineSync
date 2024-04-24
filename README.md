# CineSync

Проект представляет собой интерфейс для работы с системой кинотеатра

## Краткое описание

На сайте отображаются фильмы, их сеансы и залы, в которых будут проходить показы. Можно выбирать места в зале,
заказывать их. Можно просматривать информацию о конкретном фильме. На его странице будет отображаться описание, дата
выхода, режиссер, жанры, ближайшие сеансы и другая информация. Также на сайте реализована возможность регистрации,
авторизации, редактирования профиля.
Сайт расположен по адресу: https://cinesync.numerum.site/

## Инструкция к локальному запуску

1) Скачать проект или склонировать репозиторий:

    ```bash
    git clone https://github.com/omixyy/MSU_aerosol_site
    ```

2) Создать виртуальное окружение:

    ```bash
    python3 -m venv venv
    ```

3) Активировать его:

    ```bash
    source venv/bin/activate
    ```

4) Установить зависимости:

    - Для разработки:

        ```bash
        pip3 install -r requirements/dev.txt
        ```

    - Для тестирования:

        ```bash
        pip3 install -r requirements/test.txt
        ```

    - Для продакшена:

        ```bash
        pip3 install -r requirements/prod.txt
        ```

5) Применить миграции:

    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

6) Запуск:

    ```bash
    cd CineSync
    python3 manage.py runserver
    ```

## База данных

На диаграмме ниже представлена схема базы данных
![alt text](ER.png)
