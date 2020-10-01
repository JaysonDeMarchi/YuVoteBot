import re

validCookies = [
    'attr_multitouch',
    'ep201',
    'ep202',
    'ep203'
]

def build(response):
    setCookies = re.split('[, ]', response.headers['Set-Cookie'])
    setCookies = list(filter(
        lambda setCookie: re.search('|'.join(validCookies), setCookie),
        setCookies
    ))
    cookies = {}
    for setCookie in setCookies:
        setCookie = re.sub(';$', '', setCookie)
        key,value = setCookie.split('=', maxsplit=1)
        cookies[key] = value
    return cookies
