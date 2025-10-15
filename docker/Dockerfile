FROM python:3

RUN pip install django mysqlclient

COPY entrypoint /entrypoint

ENTRYPOINT ["/entrypoint"]