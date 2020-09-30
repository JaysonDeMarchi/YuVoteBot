from .model.session import Session
import requests
import sys

session = Session()
baseUrl = session.getData('base_url')

def pageLoad():
    response = requests.get(baseUrl)
    if (response.status_code != 200):
        print('ERROR: status_code ' + str(response.status_code))
        print('Requested URL: ' + baseUrl)
    return response

def executeStep(data=[], headers=[]):
    response = requests.post(baseUrl, data=data, headers=headers)
    if (response.status_code != 200):
        print('ERROR: status_code ' + str(response.status_code))
        print('Requested URL: ' + baseUrl)
    return response
