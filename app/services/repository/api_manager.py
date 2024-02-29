import requests
from json import loads, dumps

def get(url, headers = {}, payload = {}):
    return loads(requests.get(url=url, headers = headers, data=dumps(payload)).text)

def post(url, headers = {}, payload = {}):
    return loads(requests.post(url=url, headers = headers, data=dumps(payload)).text)
    
def put(url, headers = {}, payload = {}):
    return loads(requests.put(url=url, headers = headers, data=dumps(payload)).text)

def delete(url, headers = {}, payload = {}):
    res = (requests.delete(url=url, headers = headers, data=dumps(payload)).text)
    if(res == ''):
        print("La respuesta de la Api fue vacia")
        response = {
            "success":False,
            "status":204,
            "message":"Sin datos para enviar",            
            "data":None
        }
    else:
        response = res
    
    return response