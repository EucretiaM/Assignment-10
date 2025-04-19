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
