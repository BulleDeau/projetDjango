FROM python:3

RUN pip install django mysqlclient
RUN pip django-bootstrap5

COPY entrypoint /entrypoint

ENTRYPOINT ["/entrypoint"]