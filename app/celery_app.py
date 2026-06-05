from celery import Celery

celery = Celery(
    "url_tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)