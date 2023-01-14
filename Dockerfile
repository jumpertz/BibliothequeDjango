FROM python:3.8

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y libpq-dev

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN pip install Pillow
RUN pip install psycopg2-binary

COPY . /code/

CMD ["python3", "manage.py", "runserver"]