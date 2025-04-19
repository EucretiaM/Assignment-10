import unittest
from creational_patterns.abstract_factory import EducatorUIFactory, EducatorDashboard, EducatorButton, LearnerUIFactory, LearnerDashboard, LearnerButton

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

