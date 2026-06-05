from celery import Celery




celery = Celery(
    "app",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
    include=["app.tasks"]   
)

print("BROKER:", celery.conf.broker_url)
print("BACKEND:", celery.conf.result_backend)