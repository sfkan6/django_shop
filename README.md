# Интерент-магазин на Django

## Установка

### Docker:

1. Если у вас не установлен Docker: Установите [Docker](https://docs.docker.com/get-docker/).

2. Создайте контейнер:
```sh
docker build -t shop .
```

3. Запустите контейнер:
```sh
docker run -p 8000:8000 -it shop
```

### Простая установка:

1. Клонировать репозиторий и перейти в него в командной строке:
```sh
git clone https://github.com/sfkan6/ConsoleAppDadata.git
```
```sh
cd ConsoleAppDadata
```

2. Cоздать и активировать виртуальное окружение:
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

3. Установите зависимости:
```sh
python pip install -r requirements.txt
```

4. Выполните миграции:
```sh
python manage.py migrate
```

5. Загрузите тестовые данные в базу:
 ```sh
 python manage.py loaddata fixtures.json
 ```

6. Запустите тестовый сервер:
  ```sh
 python manage.py runserver
 ```

7. Перейдите по ссылке: (http://127.0.0.1:8000)

#### Тестовый суперпользователь:

Логин: admin@gmail.ru
Пароль: admin
