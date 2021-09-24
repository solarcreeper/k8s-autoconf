from elasticsearch import Elasticsearch





if __name__ == '__main__':
    es = Elasticsearch(['192.168.101.201:32588'], http_auth="elastic:ov320RJ77lBg152VumN3lir8")
    # result = es.indices.create(index='test', ignore = 400)
    # print(result)
    for i in range(10010):
        data = {'name': 'testuser%d' %i, 'age': '%d' %i}
        result = es.create(index='test2', doc_type='politics', id=i, body=data)
        print(result)
