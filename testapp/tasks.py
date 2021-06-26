from testapp import celery

@celery.task
def delay_print(msg):
    print(msg)