from prompt_toolkit import prompt
from session import Session
import parser
import requests

session = Session()

def requestHomepage(url):
    return requests.get(url)

def baseUrl():
    newBaseUrl = ''
    if not session.getData().has_key('base_url') or session.getData('base_url') == '':
        print('Missing Poll URL.')
        newBaseUrl = prompt(u'New Poll URL: ')

    response = requestHomepage(
        newBaseUrl
        if newBaseUrl != ''
        else session.getData('base_url')
    )

    while ('CREATE-A-CARD' not in parser.getTitle(response)):
        print('Invalid Poll URL Provided.')
        newBaseUrl = prompt(u'New Poll URL: ')
        response = requestHomepage(newBaseUrl)

    if newBaseUrl != '':
        session.setData('base_url', newBaseUrl)
        session.save()
