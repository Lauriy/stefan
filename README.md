![Python application](https://github.com/Lauriy/stefan/workflows/Python%20application/badge.svg)
[![codecov](https://codecov.io/gh/Lauriy/stefan/branch/master/graph/badge.svg)](https://codecov.io/gh/Lauriy/stefan)

# Tests
```console
pytest
```

# Fixtures
```console
python manage.py loaddata stefan/fixtures/stefan_vote.json
```

Full run command on remote server for development:
```console
ssh://stefan@indoorsman.ee:22/home/stefan/stefan/venv/bin/python -u /home/stefan/stefan/manage.py runserver_plus 0.0.0.0:8002 --cert-file fullchain.crt --key-file privkey.key
```

```console
uwsgi --ini /home/stefan/stefan/uwsgi.ini --py-autoreload 1
```

On the server venv:
```console
pip install wheel uwsgi Werkzeug pyOpenSSL
```

