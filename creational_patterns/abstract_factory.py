class Dashboard:
    pass

class Button:
    pass

class EducatorDashboard(Dashboard):
    def render(self):
        return "Educator Dashboard"

class LearnerDashboard(Dashboard):
    def render(self):
        return "Learner Dashboard"

class EducatorButton(Button):
    def render(self):
        return "Educator Button"

class LearnerButton(Button):
    def render(self):
        return "Learner Button"

class UIFactory:
    def create_dashboard(self):
        pass
    def create_button(self):
        pass

class EducatorUIFactory(UIFactory):
    def create_dashboard(self):
        return EducatorDashboard()
    def create_button(self):
        return EducatorButton()

class LearnerUIFactory(UIFactory):
    def create_dashboard(self):
        return LearnerDashboard()
    def create_button(self):
        return LearnerButton()
