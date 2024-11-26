FROM python:3.11-bookworm


ENV PYTHONBUFFERED = 1

WORKDIR /chat_app


COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD python manage.py runserver 0.0.0.0:8000