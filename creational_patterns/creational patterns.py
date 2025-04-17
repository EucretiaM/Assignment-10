# Math Booster - Creational Design Patterns Implementation

# --------------------------------------------
# 1. Simple Factory
# Use Case: Submit Assessment (Quiz or Written)
# --------------------------------------------
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

# --------------------------------------------
# 2. Factory Method
# Use Case: Send Notifications (Email or InApp)
# --------------------------------------------
class NotificationSender:
    def create_sender(self):
        pass

class EmailSender:
    def send(self):
        return "Sending Email Notification"

class InAppSender:
    def send(self):
        return "Sending In-App Notification"

class EmailNotificationSender(NotificationSender):
    def create_sender(self):
        return EmailSender()

class InAppNotificationSender(NotificationSender):
    def create_sender(self):
        return InAppSender()

# --------------------------------------------
# 3. Abstract Factory
# Use Case: UI Theme Management for Educator and Learner
# --------------------------------------------
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

# --------------------------------------------
# 4. Builder
# Use Case: Generate Reports step-by-step
# --------------------------------------------
class Report:
    def __init__(self):
        self.sections = []

    def show(self):
        return self.sections

class ReportBuilder:
    def __init__(self):
        self.report = Report()

    def add_top_performers(self):
        self.report.sections.append("Top Performers")
        return self

    def add_average_scores(self):
        self.report.sections.append("Average Scores")
        return self

    def build(self):
        return self.report

# --------------------------------------------
# 5. Prototype
# Use Case: Clone Assessment Templates
# --------------------------------------------
import copy

class AssessmentTemplate:
    def __init__(self, title, instructions):
        self.title = title
        self.instructions = instructions

    def clone(self):
        return copy.deepcopy(self)

# --------------------------------------------
# 6. Singleton
# Use Case: Shared Database Connection
# --------------------------------------------
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection = "Connected to DB"
        return cls._instance

    def get_connection(self):
        return self.connection

