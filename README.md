Code is formatted with Black for clean style.

1-python -m ven env

2-pip install -r requirements.txt

3- install https://github.com/tporadowski/redis/releases 

4-open the redis-server.exe

5-python manage.py makemigrations

6-python manage.py migrate

7-create a madia folder

8-celery -A ptc worker -l info -P sol

9-python manage.py runserver

10-you are green to go 
