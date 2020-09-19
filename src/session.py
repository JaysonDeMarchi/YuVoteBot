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
                sessionData.close()

    instance = None

    def __init__(self):
        if not Session.instance:
            Session.instance = Session.__Session()
    
    def __str__(self):
        return json.dumps(self.instance.data)

    def save(self):
        with open(Session.dataFilePath, 'w') as filepath:
            data = json.dumps(
                self.instance.data,
                indent=4,
                sort_keys=True
            )
            filepath.write(data)
            filepath.close()

    def getData(self, key=''):
        if key == '':
            return self.instance.data
        return self.instance.data[key]

    def setData(self, key, value):
        self.instance.data[key] = value
        return self
