from . import \
    cookieBuilder, \
    parser, \
    validate, \
    vote_request, \
    vote_response
from .model.session import Session
import \
    time, \
    requests

session = Session()

steps = [
    '0',
    '1',
    '2'
]

def execute(voteCount = 1):
    validate.baseUrl()
    print('Executing {:d} vote(s) . . .'.format(voteCount))
    for currentVote in range(0, voteCount):
        response = vote_request.pageLoad()
        for step in steps:
            startTime = int(time.time() * 1000)
            question = parser.parseResponseToQuestion(response)
            requestData = vote_response.buildData(
                parser.getFormData(response),
                step,
                question,
                startTime
            )
            cookies = cookieBuilder.build(response)
            response = requests.post(
                session.getData('base_url'),
                cookies=cookies,
                files=requestData
            )
