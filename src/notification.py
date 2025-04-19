from datetime import datetime
from uuid import UUID

class Notification:
    def __init__(self, id: UUID, recipient_id: UUID, message: str, timestamp: datetime):
        self.__id = id
        self.__recipient_id = recipient_id
        self.__message = message
        self.__timestamp = timestamp

    def send(self):
        pass

    def mark_as_read(self):
        pass
