import json
from elasticsearch import Elasticsearch
import os

with open('rakuten_books.json') as f:
    books = json.load(f)

es = Elasticsearch(
    hosts=os.environ["ELASTICSEARCH_URL"],
    http_auth=('elastic', os.environ["ELASTIC_PASSWORD"])
)

for book in books:
    book_item = book["Item"]
    try:
        es.create(index="book", id=book_item["isbn"], body=book_item)
    except Exception as e:
        print(f"Failed to index book {book_item['title']}: {e}")
        continue

    print(f"Indexed {book_item['title']}")
