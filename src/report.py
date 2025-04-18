from datetime import datetime
from uuid import UUID

class Report:
    def __init__(self, id: UUID, educator_id: UUID, criteria: str, generated_at: datetime, report_data: dict):
        self.__id = id
        self.__educator_id = educator_id
        self.__criteria = criteria
        self.__generated_at = generated_at
        self.__report_data = report_data

    def generate(self):
        pass

    def download(self):
        pass
