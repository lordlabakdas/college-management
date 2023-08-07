import uuid
from datetime import date, datetime
from typing import Optional

from pydantic import validator
from sqlmodel import Field, SQLModel


class Student(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    first_name: str
    family_name: str
    date_of_birth: datetime
    email_address: str = Field(max_length=100, regex=r"^[\w\.-]+@[\w\.-]+\.\w+$")
    is_deleted: bool = False

    @validator("date_of_birth")
    def validate_age(cls, v):
        today = date.today()
        age = today.year - v.year
        if age <= 10:
            raise ValueError("Age must be greater than 10 years.")
        return v

    def get_fullname_of_student(self):
        return f"{self.first_name} {self.family_name}"

    def get_student_given_fullname(self, fullname):
        return Student.query.filter_by(first_name=fullname.split(" ")[0]).first()
