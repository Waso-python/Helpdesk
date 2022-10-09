# Helpdesk
Программа учета заявок на обслуживание клиентов

python3.10 -m venv venv

source venv/bin/activate

python3 -m pip install -r requirements.txt

pip3 install django

pip3 install psycopg2-binary

source venv/bin/activate python3 manage.py runserver

pip3 freeze > requirements.txt

python3 manage.py migrate

python3 manage.py makemigrations

python3 manage.py migrate

python manage.py createsuperuser superuser - ******, pass - ******

docker build -t helpdesk .
docker run -d -p 8000:8000 -it helpdesk
docker update --restart=always <container_id>
