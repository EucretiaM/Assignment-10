from datetime import datetime
from uuid import UUID

class Submission:
    def __init__(self, id: UUID, learner_id: UUID, assessment_id: UUID, content: str, timestamp: datetime, status: str, marks: int):
        self.__id = id
        self.__learner_id = learner_id
        self.__assessment_id = assessment_id
        self.__content = content
        self.__timestamp = timestamp
        self.__status = status
        self.__marks = marks

    def verify_otp(self):
        pass

    def update_status(self):
        pass
