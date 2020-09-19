import json
import os

class Session:
    dataFilePath = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '../data/session.json'
    )
    
    class __Session:
        def __init__(self):
            with open(Session.dataFilePath) as sessionData:
                self.data = json.load(sessionData)

    instance = None

    def __init__(self):
        if not Session.instance:
            Session.instance = Session.__Session()
    
    def __str__(self):
        return json.dumps(self.instance.data)
