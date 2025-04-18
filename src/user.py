from datetime import datetime
from uuid import UUID

class User:
    def __init__(self, id: UUID, name: str, email: str, password_hash: str, role: str, last_login: datetime):
        self.__id = id
        self.__name = name
        self.__email = email
        self.__password_hash = password_hash
        self.__role = role
        self.__last_login = last_login

    def login(self):
        pass

    def logout(self):
        pass

    def update_profile(self):
        pass
