from datetime import datetime
from uuid import UUID

class Assessment:
    def __init__(self, id: UUID, title: str, instructions: str, deadline: datetime, educator_id: UUID, created_at: datetime):
        self.__id = id
        self.__title = title
        self.__instructions = instructions
        self.__deadline = deadline
        self.__educator_id = educator_id
        self.__created_at = created_at

    def is_deadline_passed(self):
        pass

    def notify_learners(self):
        pass
