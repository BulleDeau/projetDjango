FROM python:3

RUN pip install django mysqlclient  django-bootstrap5  django-debug-toolbar django_extensions ipython

COPY entrypoint /entrypoint

ENTRYPOINT ["/entrypoint"]