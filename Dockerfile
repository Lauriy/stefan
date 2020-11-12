FROM python:3.9

ENV PYTHONUNBUFFERED=1

RUN apt-get -qq update

RUN apt-get install --yes apache2 apache2-dev

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

#CMD mod_wsgi-express start-server /code/stefan/wsgi.py --user www-data --group www-data

CMD python manage.py collectstatic --noinput && python manage.py runmodwsgi --reload-on-changes --user www-data --group www-data

#RUN cat httpd-extra.conf >> /tmp/mod_wsgi-localhost:8000/httpd.conf

#RUN /tmp/mod_wsgi-localhost:8000/apachectl restart
