from elasticsearch import Elasticsearch

# Устанавливаем подключение к Elasticsearch
es = Elasticsearch(['localhost:9200'])

# Определяем индекс и тип документа
index_name = 'my_index'
doc_type = 'my_document'

# Пример поискового запроса
search_query = {
    "query": {
        "match": {
            "title": "example"
        }
    }
}

# Выполняем поиск в Elasticsearch
search_results = es.search(
    index=index_name, doc_type=doc_type, body=search_query)

# Обрабатываем результаты поиска
for hit in search_results['hits']['hits']:
    print(hit['_source'])
