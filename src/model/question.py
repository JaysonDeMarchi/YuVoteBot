from .abstract_model import AbstractModel
from prompt_toolkit.shortcuts import radiolist_dialog

class Question(AbstractModel):
    data = {
        'answer': '',
        'question': '',
        'options': []
    }

    def solve(self, question = '', options = []):
        radioOptions = list(map(
            lambda option: (option, option),
            options
        ))
        answer = radiolist_dialog(
            values=radioOptions,
            title=question,
            text='Answer: ',
        ).run()
        return answer
