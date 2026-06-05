from app.celery_app import celery
from app.scraper import extract_title

@celery.task
def process_urls(url_list):
    results = []

    for url in url_list:
        data = extract_title(url)
        results.append(data)

    return results