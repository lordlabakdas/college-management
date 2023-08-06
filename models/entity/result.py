import uuid
from typing import Optional


from sqlmodel import Field, SQLModel


class Course(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    student_id : uuid.UUID = Field(foreign_key="student.id")
    course_id : uuid.UUID = Field(foreign_key="course.id")
    score: str = Field(choices=["A", "B", "C", "D", "E", "F"])