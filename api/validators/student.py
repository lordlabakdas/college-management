from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class RegistrationPayload(BaseModel):
    first_name: str
    family_name: str
    date_of_birth: datetime
    email_address: str


class RegistrationResponse(BaseModel):
    id: UUID
