#! /bin/env python3


#from elasticsearch import Elasticsearch
import requests

class Es(Elasticsearch):
    def connect(self, host, port, user=None, pwd=None):
        if user and pwd:
            es = Elasticsearch(host+':'+str(port), http_auth=(user, pwd), maxsize=15)
        else:
            es = Elasticsearch(host+':'+str(port), maxsize=15)
        return es

