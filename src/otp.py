from datetime import datetime
from uuid import UUID

class OTP:
    def __init__(self, code: str, user_id: UUID, expires_at: datetime, verified: bool):
        self.__code = code
        self.__user_id = user_id
        self.__expires_at = expires_at
        self.__verified = verified

    def generate(self):
        pass

    def validate(self):
        pass
