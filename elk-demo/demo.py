from elasticsearch import Elasticsearch





if __name__ == '__main__':
    es = Elasticsearch(['192.168.101.201:30123'], http_auth="elastic:7d2Rod9ySBHozixcxZBa")
    # result = es.indices.create(index='test', ignore = 400)
    # print(result)
    data = {'name': 'adf', 'age': '28'}
    result = es.create(index='test', doc_type='politics', id=5, body=data)
    print(result)
