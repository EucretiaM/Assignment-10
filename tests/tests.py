import unittest
import threading
from creational_patterns import *

class TestSimpleFactory(unittest.TestCase):
    def test_valid_creation(self):
        car = UserFactory.create_user("learner")
        self.assertIsInstance(car, Learner)

    def test_invalid_creation(self):
        with self.assertRaises(ValueError):
            UserFactory.create_user("invalid")

class TestFactoryMethod(unittest.TestCase):
    def test_educator_creation(self):
        creator = EducatorCreator()
        user = creator.create_user()
        self.assertIsInstance(user, Educator)

class TestAbstractFactory(unittest.TestCase):
    def test_learner_notification_factory(self):
        factory = LearnerNotificationFactory()
        notification = factory.create_notification("Test message")
        self.assertIsInstance(notification, LearnerNotification)
        self.assertEqual(notification.message, "Test message")

class TestBuilderPattern(unittest.TestCase):
    def test_full_submission_build(self):
        builder = SubmissionBuilder()
        director = SubmissionDirector(builder)
        submission = director.construct_submission("L1", "A1", "Work")
        self.assertEqual(submission.learnerId, "L1")
        self.assertEqual(submission.status, "Pending")

    def test_invalid_content(self):
        builder = SubmissionBuilder()
        builder.set_content("")
        self.assertEqual(builder.submission.content, "")

class TestPrototypePattern(unittest.TestCase):
    def test_clone_submission(self):
        original = Submission("S1", "L1", "A1", "Work", "2024-01-01", "Submitted", 100)
        clone = original.clone()
        self.assertIsNot(original, clone)
        self.assertEqual(clone.content, "Work")

class TestSingletonPattern(unittest.TestCase):
    def test_single_instance(self):
        a = AppSettings()
        b = AppSettings()
        self.assertIs(a, b)

    def test_thread_safety(self):
        instances = []

        def create_instance():
            instances.append(AppSettings())

        threads = [threading.Thread(target=create_instance) for _ in range(10)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        self.assertTrue(all(i is instances[0] for i in instances))

if __name__ == '__main__':
    unittest.main()

