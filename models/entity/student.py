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
    email_address: str = Field(max_length=100, regex=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    
    @validator("date_of_birth")
    def validate_age(cls, v):
        today = date.today()
        age = today.year - v.year
        if age <= 10:
            raise ValueError("Age must be greater than 10 years.")
        return v
    