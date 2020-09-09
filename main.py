from bs4 import BeautifulSoup
import requests
import sys

BASE_URL = 'https://www.research.net/r/LQKKZDK'

def initialRequest():
    response = requests.get(BASE_URL)
    if (response.status_code != 200):
        print('ERROR: status_code' + response.status_code)
        sys.exit()
    return response

def getFormData(response):
    parsedResponse = BeautifulSoup(response.text, 'html.parser')
    form = parsedResponse.form
    inputs = {}
    for inputData in form.findAll('input'):
        inputs[inputData.get('name')] = inputData.get('value')
    return inputs

def getHeaders(response):
    responseHeaders = response.headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        'Cookie': responseHeaders['Set-Cookie'],
    }
    return headers

if __name__ == '__main__':
    initialResponse = initialRequest()

    headers = getHeaders(initialResponse)
    formData = getFormData(initialResponse)

    stepResponse = requests.post(BASE_URL, data=formData, headers=headers)
