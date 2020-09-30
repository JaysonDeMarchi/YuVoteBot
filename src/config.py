import json
import os

class Config:
    dataFilePath = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '../data/config.json'
    )
    
    class __Config:
        def __init__(self):
            with open(Config.dataFilePath) as configData:
                self.data = json.load(configData)
                configData.close()

    instance = None

    def __init__(self):
        if not Config.instance:
            Config.instance = Config.__Config()
    
    def __str__(self):
        return json.dumps(self.instance.data)

    def save(self):
        with open(Config.dataFilePath, 'w') as filepath:
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
