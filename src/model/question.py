from .abstract_model import AbstractModel
from prompt_toolkit.shortcuts import radiolist_dialog

class Question(AbstractModel):
    data = {
        'answer': '',
        'question': '',
        'options': []
    }

    def solve(self):
        options = self.getData('options')
        radioOptions = list(map(
            lambda option: (option, option),
            options
        ))
        answer = radiolist_dialog(
            values=radioOptions,
            title=self.getData('self'),
            text='Answer: ',
        ).run()
        self.setData('answer', answer)
        return self
