from . import \
    parser, \
    validate, \
    vote_request, \
    vote_response
import time

steps = [
    '0'
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
            headers = vote_response.buildHeaders(response)
            response = vote_request.executeStep(step, requestData, headers)
