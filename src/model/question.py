from abstract_model import AbstractModel

class Question(AbstractModel):
    data = {
        'answer': '',
        'question': '',
        'options': []
    }
