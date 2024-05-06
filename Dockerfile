FROM python:3.10

WORKDIR /home

COPY src/app /home/app

COPY ./requirements.txt /home/requirements.txt

RUN pip install -U pip && pip install -r requirements.txt

EXPOSE 80

CMD ["fastapi", "run", "app/main.py", "--port", "80"]

