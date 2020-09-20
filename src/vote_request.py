from session import Session
import requests
import sys

session = Session()

paths = {
    '0': session.getData('base_url')
}

def requestStep(step):
    response = requests.get(paths.get(step, ''))
    if ():
        print('ERROR: No path for step ' + step)
        sys.exit()
    if (response.status_code != 200):
        print('ERROR: status_code' + response.status_code)
        print('Requested URL: ' + paths.get(step))
        sys.exit()
    return response
