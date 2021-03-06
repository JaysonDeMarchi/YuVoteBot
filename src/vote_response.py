from .model.session import Session
import \
    json, \
    random, \
    time

session = Session()

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

def buildResponseQualityData(step, question, startTime, questionId):
    step = int(step)
    steps = session.getData('steps')
    sessionResponseData = steps[str(step)]['response_quality_data']
    # simulate human like response timing
    time.sleep(random.uniform(5, 7))
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
    else:
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
