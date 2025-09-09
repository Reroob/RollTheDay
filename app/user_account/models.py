from sqlmodel import SQLModel, Field
from pydantic import EmailStr
from datetime import date
from uuid import uuid4, UUID


class UserAccount(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    public_id : UUID = Field(default_factory=lambda: str(uuid4()))
    email: EmailStr
    hashedpassword: str
    is_validated: bool = Field(default=False)
    is_admin: bool = Field(default=False)
    is_paid: bool = Field(default=False)
    subscriptionenddate: date


