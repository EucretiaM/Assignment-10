import unittest
from creational_patterns import (
    AssessmentFactory,
    QuizAssessment,
    WrittenAssessment,
    EmailNotificationSender,
    EmailSender,
    InAppNotificationSender,
    InAppSender,
    EducatorUIFactory,
    EducatorDashboard,
    EducatorButton,
    LearnerUIFactory,
    LearnerDashboard,
    LearnerButton,
    ReportBuilder,
    AssessmentTemplate,
    DatabaseConnection
)

# --------------------------------------------
# 1. Simple Factory
# --------------------------------------------
class TestSimpleFactory(unittest.TestCase):
    def test_quiz_assessment_creation(self):
        factory = AssessmentFactory()
        assessment = factory.create_assessment("quiz")
        self.assertIsInstance(assessment, QuizAssessment)
        self.assertEqual(assessment.display(), "Quiz Assessment")

    def test_written_assessment_creation(self):
        factory = AssessmentFactory()
        assessment = factory.create_assessment("written")
        self.assertIsInstance(assessment, WrittenAssessment)
        self.assertEqual(assessment.display(), "Written Assessment")

    def test_invalid_assessment_creation(self):
        factory = AssessmentFactory()
        with self.assertRaises(ValueError):
            factory.create_assessment("invalid")

# --------------------------------------------
# 2. Factory Method
# --------------------------------------------
class TestFactoryMethod(unittest.TestCase):
    def test_email_sender_creation(self):
        sender_factory = EmailNotificationSender()
        sender = sender_factory.create_sender()
        self.assertIsInstance(sender, EmailSender)
        self.assertEqual(sender.send(), "Sending Email Notification")

    def test_inapp_sender_creation(self):
        sender_factory = InAppNotificationSender()
        sender = sender_factory.create_sender()
        self.assertIsInstance(sender, InAppSender)
        self.assertEqual(sender.send(), "Sending In-App Notification")

# --------------------------------------------
# 3. Abstract Factory
# --------------------------------------------
class TestAbstractFactory(unittest.TestCase):
    def test_educator_ui_creation(self):
        ui_factory = EducatorUIFactory()
        dashboard = ui_factory.create_dashboard()
        button = ui_factory.create_button()
        self.assertIsInstance(dashboard, EducatorDashboard)
        self.assertIsInstance(button, EducatorButton)
        self.assertEqual(dashboard.render(), "Educator Dashboard")
        self.assertEqual(button.render(), "Educator Button")

    def test_learner_ui_creation(self):
        ui_factory = LearnerUIFactory()
        dashboard = ui_factory.create_dashboard()
        button = ui_factory.create_button()
        self.assertIsInstance(dashboard, LearnerDashboard)
        self.assertIsInstance(button, LearnerButton)
        self.assertEqual(dashboard.render(), "Learner Dashboard")
        self.assertEqual(button.render(), "Learner Button")

# --------------------------------------------
# 4. Builder
# --------------------------------------------
class TestBuilder(unittest.TestCase):
    def test_report_builder(self):
        builder = ReportBuilder()
        report = builder.add_top_performers().add_average_scores().build()
        self.assertEqual(report.show(), ["Top Performers", "Average Scores"])

    def test_empty_report(self):
        builder = ReportBuilder()
        report = builder.build()
        self.assertEqual(report.show(), [])

# --------------------------------------------
# 5. Prototype
# --------------------------------------------
class TestPrototype(unittest.TestCase):
    def test_assessment_template_clone(self):
        template = AssessmentTemplate("Math Quiz", "Solve all questions")
        clone = template.clone()
        self.assertIsNot(template, clone)
        self.assertEqual(template.title, clone.title)
        self.assertEqual(template.instructions, clone.instructions)

# --------------------------------------------
# 6. Singleton
# --------------------------------------------
import threading

class TestSingleton(unittest.TestCase):
    def test_singleton_instance(self):
        instance1 = DatabaseConnection()
        instance2 = DatabaseConnection()
        self.assertIs(instance1, instance2)
        self.assertEqual(instance1.get_connection(), "Connected to DB")

    def test_thread_safety(self):
        instances = []

        def create_instance():
            instances.append(DatabaseConnection())

        threads = [threading.Thread(target=create_instance) for _ in range(10)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        for instance in instances:
            self.assertIs(instance, instances[0])

if __name__ == '__main__':
    unittest.main()
