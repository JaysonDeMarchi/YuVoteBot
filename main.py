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

if __name__ == '__main__':
    initialResponse = initialRequest()

    formData = getFormData(initialResponse)

    print(formData)
