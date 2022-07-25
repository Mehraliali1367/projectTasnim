FROM python:latest
#ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD /setup/requirements.txt /code/
RUN pip install -U pip
RUN pip install -r requirements.txt
#COPY scripts/start*.sh /
ADD . /code/
CMD ["gunicorn","setup.wsgi",":8000"]
