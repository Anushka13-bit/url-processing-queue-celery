from fastapi import FastAPI
from tasks import process_urls
from celery.result import AsyncResult

app = FastAPI()

@app.post("/process")
def process(data: URLRequest):
    task = process_urls.delay(urls)

    return {
        "task_id": task.id,
        "status": "processing"
    }


@app.get("/status/{task_id}")
def get_status(task_id: str):
    task = AsyncResult(task_id)

    return {
        "status": task.status,
        "result": task.result if task.ready() else None
    }