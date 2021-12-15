## Requirements
- Python 3.7.10
- postgres (optional)
## Installation 
- Create  virtual environment(optional)
- Install the dependencies and devDependencies  
```sh
$ pip install -r requirements.txt
```

- Set DataBase Connection in tboof/settings.py
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER': 'test',
        'PASSWORD': 'test@test',
        'HOST': '127.0.0.1',  # Or an IP Address that your DB is hosted on
        'PORT': '3306',
        'OPTIONS': {
            # Tell MySQLdb to connect with 'utf8mb4' character set
            'charset': 'utf8mb4',
        },
    }
}
```
- Create Table In DataBase  and mock data 
```sh
$ python manage.py migrate
```
- Create Super User
```sh
$ python manage.py createsuperuser
```
- Run Server and admin route  http://127.0.0.1:8000/admin 
```sh
$ python manage.py runserver
```

- Manual config in tboof/settings.py
 ```python
CELERY_BROKER_URL = "amqp://myuser:mypassword@localhost:5672/myvhost"

```
- Run celery
```sh
$ celery -A tboof worker
```


License
----
tazminchi

- If You want more info like rest api request file Such as Postman Contact Us
baharimahdi93@gmail.com

