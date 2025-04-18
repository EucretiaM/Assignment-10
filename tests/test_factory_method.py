import unittest
from creational_patterns.factory_method import EmailNotificationSender, EmailSender, InAppNotificationSender, InAppSender

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

