Full run command on remote server for development:
```console
ssh://stefan@indoorsman.ee:22/home/stefan/stefan/venv/bin/python -u /home/stefan/stefan/manage.py runserver_plus 0.0.0.0:8002 --cert-file fullchain.crt --key-file privkey.key
```

```console
uwsgi --ini /home/stefan/stefan/uwsgi.ini
```

On the server venv:
```console
pip install wheel uwsgi Werkzeug pyOpenSSL psycopg2-binary
```