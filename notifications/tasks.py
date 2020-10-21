from django.conf import settings

from jobs.celery import app as celery_app


@celery_app.task(queue=settings.CELERY_LOW_QUEUE_NAME)
def dispatch_event(event_name: str, model_class_name: str, instance_pk: int):
    print(event_name)
