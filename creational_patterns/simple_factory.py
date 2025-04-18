class Assessment:
    def display(self):
        pass

class QuizAssessment(Assessment):
    def display(self):
        return "Quiz Assessment"

class WrittenAssessment(Assessment):
    def display(self):
        return "Written Assessment"

class AssessmentFactory:
    def create_assessment(self, type_):
        if type_ == "quiz":
            return QuizAssessment()
        elif type_ == "written":
            return WrittenAssessment()
        else:
            raise ValueError("Invalid assessment type")
