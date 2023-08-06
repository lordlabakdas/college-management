import uuid
from typing import Optional


from sqlmodel import Field, SQLModel


class Course(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    