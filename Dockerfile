FROM python:3.10.1-buster
MAINTAINER Lukasz Admin

EXPOSE 80
EXPOSE 8000
EXPOSE 8080
EXPOSE 8002

ENV PYTHONUNBUFFERED 1
ENV LISTEN_PORT=8000
ENV PATH="/scripts:${PATH}"

RUN apt-get install gcc
RUN apt-get update
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
RUN apt-get install -y g++ unixodbc-dev
RUN pip install pyodbc
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN useradd -ms /bin/bash admin
RUN mkdir /app

COPY ./app/ /app
COPY ./scripts /scripts
RUN chmod +x /scripts/*
WORKDIR /app
RUN chown -R admin:admin /app
RUN chmod 755 /app
USER admin

EXPOSE 8000

CMD ["entrypoint.sh"]