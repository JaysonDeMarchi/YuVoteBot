from bs4 import BeautifulSoup

def getTitle(response):
    parsedResponse = BeautifulSoup(response.text, 'html.parser')
    results = parsedResponse.findAll('span', { 'class': 'title-text' })
    return '' if not results else results.pop().text
