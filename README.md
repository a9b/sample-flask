poetry run python runserver.py
poetry run celery -A testapp.celery worker

poetry run uwsgi --http=0.0.0.0:5000 --manage-script-name --mount /=testapp:app
poetry run uwsgi --ini myapp.ini
poetry run celery -A testapp.celery worker