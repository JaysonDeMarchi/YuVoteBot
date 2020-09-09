import requests
import sys

BASE_URL = 'https://www.research.net/r/LQKKZDK'

def initialRequest():
    response = requests.get(BASE_URL)
    if (response.status_code != 200):
        print('ERROR: status_code' + response.status_code)
        sys.exit()
    return response

if __name__ == '__main__':
    initialResponse = initialRequest()

    print(initialResponse.headers)
