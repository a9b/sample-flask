from flask import Flask
from testapp.celery_maker import make_celery

app = Flask(__name__)
# app.config.update(
#     CELERY_BROKER_URL='redis://localhost:6379',
#     CELERY_RESULT_BACKEND='redis://localhost:6379'
# )
celery = make_celery(app)

import testapp.route