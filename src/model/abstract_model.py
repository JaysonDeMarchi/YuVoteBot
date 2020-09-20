import json

class AbstractModel:
    data = {}

    def __init__(self, data):
        for key in data.keys():
            self.setData(key, data[key])

    def getData(self, key=''):
        if key == '':
            return self.data
        return self.data[key]

    def setData(self, key, value):
        self.data[key] = value
        return self
    
    def __str__(self):
        return json.dumps(
            self.data,
            indent=4,
            sort_keys=True
        )
