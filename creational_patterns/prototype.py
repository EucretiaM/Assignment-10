import copy

class AssessmentTemplate:
    def __init__(self, title, instructions):
        self.title = title
        self.instructions = instructions

    def clone(self):
        return copy.deepcopy(self)
