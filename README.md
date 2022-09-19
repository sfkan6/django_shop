# Интерент-магазин на Django

## [Docker](https://docs.docker.com/get-docker/):

1. Создайте и запустите контейнер:
```sh
make docker
```

<details>
<summary>Запуск вручную</summary>

1. Создайте контейнер:
```sh
docker build -t shop .
```

2. Запустите контейнер:
```sh
docker run --rm -p 8000:8000 -it shop
```

</details>

## Установка:

1. Клонировать репозиторий и перейти в него в командной строке:
```sh
git clone https://github.com/sfkan6/django_shop.git
```
```sh
cd django_shop
```

2. Выполните в консоли:
```sh
make fast-run
```

<details>
<summary>Запуск вручную</summary>

1. Войдите в виртуальное окружение:
```sh
python -m venv venv
```

```sh
source venv/Scripts/activate
```
или
```sh
source venv/bin/activate
```

2. Установите зависимости:
```sh
pip install -r requirements.txt
```

3. Выполните миграции:
```sh
python manage.py migrate
```

4. Загрузите данные в базу данных:
 ```sh
 python manage.py loaddata db.json
 ```

5. Запустите:
  ```sh
 python manage.py runserver 0.0.0.0:8000
 ```
 
</details>

Перейдите по ссылке: (http://0.0.0.0:8000)

### Админ:

Логин: admin@gmail.ru
Пароль: admin

<hr>

![home](demo/home.png)

--------
![cart](demo/cart.png)

--------
![nav-menu](demo/nav-menu.png)