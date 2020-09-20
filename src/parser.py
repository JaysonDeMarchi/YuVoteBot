from bs4 import BeautifulSoup
from .model.question import Question

def parseResponse(response):
    return BeautifulSoup(response.text, 'html.parser')

def getTitle(response):
    parsedResponse = parseResponse(response)
    results = parsedResponse.findAll('span', { 'class': 'title-text' })
    return '' if not results else results.pop().text

def parseResponseToQuestion(response):
    parsedResponse = parseResponse(response)

    question = parsedResponse.findAll(
        'h4',
        { 'class': 'question-title-container' }
    ).pop(
    ).findAll(
        'span',
        { 'class': 'user-generated' }
    ).pop().text

    options = list(map(
        lambda option: option.text.strip(),
        parsedResponse.findAll('span', { 'class': 'question-body-font-theme' })
    ))
    data = {
        'question': question,
        'options': options
    }
    return Question(data)
