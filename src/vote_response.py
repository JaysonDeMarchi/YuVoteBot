from .session import Session
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.shortcuts import radiolist_dialog
import json
import re
import time

session = Session()

def buildCookies(response):
    validCookies = [
        'attr_multitouch',
        'ep201',
        'ep202',
        'ep203'
    ]
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

def getRelativePosition(step, question):
    if (step == 0):
        return [[
            0,
            question.getData(
                'options'
            ).index(
                question.getData('answer')
            )
        ]]
    if (step == 1):
        return [[
            question.getData(
                'options'
            ).index(
                question.getData('answer')
            ),
            0
        ]]
    if (step == 2):
        return []

def solve(question):
    options = question.getData('options')
    radioOptions = list(map(
        lambda option: (option, option),
        options
    ))
    answer = radiolist_dialog(
        values=radioOptions,
        title=question.getData('question'),
        text='Answer: ',
    ).run()
    question.setData('answer', answer)
    return question


def buildResponseQualityData(step, question, startTime, questionId):
    step = int(step)
    steps = session.getData('steps')
    sessionResponseData = steps[str(step)]['response_quality_data']
    endTime = int(time.time() * 1000)
    return {
        'question_info': {
            'qid_' + questionId: {
                'number': step + 1,
                'type': sessionResponseData['type'],
                'option_count': len(question.getData('options')),
                'has_other': False,
                'other_selected': None,
                'relative_position': getRelativePosition(step, question),
                'dimensions': sessionResponseData['dimensions'],
                'input_method': None,
                'is_hybrid': False
            }
        },
        'start_time': startTime,
        'end_time': endTime,
        'time_spent': endTime - startTime,
        'previous_clicked': False,
        'has_backtracked': False,
        'bi_voice': {}
    }

def buildData(formData, step, question, startTime):
    data = formData
    questions = session.getData('questions')
    if (step in questions and question.getData('question') in questions[step]):
        question.setData('answer', questions[step][question.getData('question')])
    if not (question.getData('answer')):
        question = solve(question)
        if (step in questions and question.getData('question') not in questions[step]):
            questions[step][question.getData('question')] = question.getData('answer')
            session.setData('questions', questions)
            session.save()

    questionId = list(filter(
        lambda key: key[0].isdigit(),
        data.keys()
    )).pop()

    data['response_quality_data'] = json.dumps(buildResponseQualityData(
        step,
        question,
        startTime,
        questionId
    ))
    return data
