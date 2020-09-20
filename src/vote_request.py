from .session import Session
import requests
import sys

session = Session()

paths = {
    '0': session.getData('base_url')
}

def pageLoad():
    baseUrl = session.getData('base_url')
    response = requests.get(baseUrl)
    if (response.status_code != 200):
        print('ERROR: status_code ' + str(response.status_code))
        print('Requested URL: ' + baseUrl)
        sys.exit()
    return response

def executeStep(step, data=[], headers=[]):
    if (paths.get(step, '') == ''):
        print('ERROR: path does not exist for step ' + step)
    response = requests.post(paths.get(step), data, headers)
    if (response.status_code != 200):
        print('ERROR: status_code ' + str(response.status_code))
        print('Requested URL: ' + paths.get(step))
        sys.exit()
    return response
