from elasticsearch import Elasticsearch


if __name__ == '__main__':

    es = Elasticsearch(['192.168.101.201:30100'], http_auth="elastic:qjlvT5sg50T8RU053Y8k6V9x")
    # result = es.indices.create(index='test', ignore = 400)
    # print(result)
    for i in range(10010):
        data = {'name': 'testuser%d' % i, 'age': '%d' % i}
        result = es.index(index='mount_log', doc_type='test_type', body=data)
        print(result)
