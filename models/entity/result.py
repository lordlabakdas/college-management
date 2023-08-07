import uuid
from typing import Optional

from sqlalchemy import Enum as SQLAlchemyEnum
from sqlmodel import Field, SQLModel

from models.db import db_session

ALLOWED_CHOICES = ["A", "B", "C", "D", "E", "F"]


class Result(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    student_id: uuid.UUID = Field(foreign_key="student.id")
    course_id: uuid.UUID = Field(foreign_key="course.id")
    score: str = Field(sa_column=SQLAlchemyEnum(*ALLOWED_CHOICES))
    is_deleted: bool = False

    def update_deleted_status_given_id(self, id):
        result = Result.query.filter_by(id=id).first()
        result.is_deleted = True
        db_session.commit()
        db_session.refresh(result)
        return result.is_deleted
