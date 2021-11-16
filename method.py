#! /bin/env python3


import request

def get(es_http, path, auth=None, json=body):
    res = requests.get(es_http + path, auth=auth)

