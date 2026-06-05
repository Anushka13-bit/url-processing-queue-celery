from fastapi import FastAPI
from app.tasks import process_urls
from app.models import URLRequest
from celery.result import AsyncResult
from app.celery_app import celery

app = FastAPI()

@app.post("/process")
def process(data: URLRequest):
    task = process_urls.delay(data.urls)

    return {
        "task_id": task.id,
        "status": "processing"
    }


@app.get("/status/{task_id}")
def status(task_id: str):
    task = AsyncResult(task_id, app=celery)

    return {
        "status": task.status,
        "result": task.result if task.ready() else None
    }