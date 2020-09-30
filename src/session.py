from .model.abstract_model import AbstractModel
import json
import os

class Session:
    dataFilePath = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '../data/session.json'
    )
    
    class __Session(AbstractModel):
        def __init__(self):
            with open(Session.dataFilePath) as sessionData:
                self.data = json.load(sessionData)
                sessionData.close()

    instance = None

    def __init__(self):
        if not Session.instance:
            Session.instance = Session.__Session()
    
    def __str__(self):
        return self.instance.__str__()

    def save(self):
        with open(Session.dataFilePath, 'w') as filepath:
            filepath.write(self.__str__())
            filepath.close()

    def getData(self, key=''):
        return self.instance.getData(key)

    def setData(self, key, value):
        return self.instance.setData(key, value)
