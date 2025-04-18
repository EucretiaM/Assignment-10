from user import User
from datetime import datetime
from uuid import UUID

class Learner(User):
    def __init__(self, id: UUID, name: str, email: str, password_hash: str, role: str, last_login: datetime, grade_level: str):
        super().__init__(id, name, email, password_hash, role, last_login)
        self.__grade_level = grade_level

    def submit_assessment(self):
        pass

    def edit_submission(self):
        pass

    def view_marks(self):
        pass

    def chat_with_educator(self):
        pass
