from .session import Session
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.shortcuts import radiolist_dialog
import time

session = Session()

def buildHeaders(response): 
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


def buildResponseQualityData(step, question, startTime):
    step = int(step)
    return {
        'question_info': {
            'qid_536755120': {
                'number': step + 1,
                'type': 'single_image_choice',
                'option_count': question.getData('options'),
                'has_other': False,
                'other_selected': None,
                'relative_position': [[
                    step,
                    question.getData(
                        'options'
                    ).index(
                        question.getData('answer')
                    )
                ]],
                'dimensions': [
                    step + 1,
                    3
                ],
                'input_method': None,
                'is_hybrid': False
            }
        },
        'start_time': startTime,
        'end_time': 1600573885405,
        'time_spent': 371193,
        'previous_clicked': False,
        'has_backtracked': False,
        'bi_voice': {}
    }

def buildData(formData, step, question, startTime):
    data = formData
    if not (question.getData('answer')):
        question = solve(question)
        questions = session.getData('questions')
        if (step in questions and question.getData('question') not in questions[step]):
            questions[step][question.getData('question')] = question.getData('answer')
            session.setData('questions', questions)
            session.save()

    data['response_quality_data'] = buildResponseQualityData(
        step,
        question,
        startTime
    )
