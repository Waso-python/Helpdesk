FROM python

RUN mkdir /app
WORKDIR /app
COPY . .

RUN apt-get update &&\
	apt-get upgrade --assume-yes &&\
	apt-get install --assume-yes python3-pip &&\
	apt-get install --assume-yes screen &&\
	pip install -r requirements.txt

CMD ["python3","/app/manage.py","runserver","0.0.0.0:8000"]
