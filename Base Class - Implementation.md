from datetime import datetime
import uuid
import json

# ===== Base Classes =====

class User:
    def __init__(self, name, email, password_hash, role):
        self.id = uuid.uuid4()
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.role = role
        self.last_login = None

    def login(self):
        self.last_login = datetime.now()

    def logout(self):
        print(f"{self.name} logged out.")

    def update_profile(self, name=None, email=None):
        if name: self.name = name
        if email: self.email = email


class Learner(User):
    def __init__(self, name, email, password_hash, grade_level):
        super().__init__(name, email, password_hash, role="Learner")
        self.grade_level = grade_level
        self.submissions = []

    def submit_assessment(self, assessment, content):
        submission = Submission(self.id, assessment.id, content)
        self.submissions.append(submission)
        return submission

    def edit_submission(self, submission_id, new_content):
        for s in self.submissions:
            if s.id == submission_id:
                s.content = new_content
                return True
        return False

    def view_marks(self):
        return {str(s.id): s.marks for s in self.submissions}

    def chat_with_educator(self):
        print("Starting chat...")


class Educator(User):
    def __init__(self, name, email, password_hash):
        super().__init__(name, email, password_hash, role="Educator")
        self.assessments = []

    def upload_assessment(self, title, instructions, deadline):
        assessment = Assessment(title, instructions, deadline, self.id)
        self.assessments.append(assessment)
        return assessment

    def mark_submission(self, submission, marks):
        submission.marks = marks
        submission.status = "Marked"

    def generate_report(self, criteria):
        report = Report(self.id, criteria)
        return report

    def send_notification(self, user, message):
        notif = Notification(user.id, message)
        notif.send()
        return notif

# ===== Supporting Classes =====

class Assessment:
    def __init__(self, title, instructions, deadline, educator_id):
        self.id = uuid.uuid4()
        self.title = title
        self.instructions = instructions
        self.deadline = deadline
        self.educator_id = educator_id
        self.created_at = datetime.now()
        self.submissions = []

    def is_deadline_passed(self):
        return datetime.now() > self.deadline

    def notify_learners(self):
        print("Learners notified about new assessment.")


class Submission:
    def __init__(self, learner_id, assessment_id, content):
        self.id = uuid.uuid4()
        self.learner_id = learner_id
        self.assessment_id = assessment_id
        self.content = content
        self.timestamp = datetime.now()
        self.status = "Submitted"
        self.marks = 0
        self.otp = OTP(self.learner_id)

    def verify_otp(self, code):
        return self.otp.validate(code)

    def update_status(self, new_status):
        self.status = new_status


class Report:
    def __init__(self, educator_id, criteria):
        self.id = uuid.uuid4()
        self.educator_id = educator_id
        self.criteria = criteria
        self.generated_at = datetime.now()
        self.report_data = {}

    def generate(self, data):
        self.report_data = data

    def download(self):
        return json.dumps(self.report_data, indent=4)


class OTP:
    def __init__(self, user_id):
        self.code = str(uuid.uuid4())[:6]
        self.user_id = user_id
        self.expires_at = datetime.now().timestamp() + 300  # 5 mins
        self.verified = False

    def generate(self):
        self.code = str(uuid.uuid4())[:6]

    def validate(self, code):
        if datetime.now().timestamp() <= self.expires_at and code == self.code:
            self.verified = True
            return True
        return False


class Notification:
    def __init__(self, recipient_id, message):
        self.id = uuid.uuid4()
        self.recipient_id = recipient_id
        self.message = message
        self.timestamp = datetime.now()
        self.read = False

    def send(self):
        print(f"Notification sent to user {self.recipient_id}: {self.message}")

    def mark_as_read(self):
        self.read = True
