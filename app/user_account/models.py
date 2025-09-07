from sqlmodel import PrimaryKeyConstraint, SQLModel, Field, true
from pydantic import EmailStr
from sqlmodel.main import default_registry
from datetime import date

class UserAccount(SQLModel, table=true):
    id: int(Field(default=None, primary_key=True))
    email: EmailStr
    hashedpassword: str
    is_validated: bool = Field(default=False)
    is_admin: bool = Field(default=False)
    is_paid: bool = Field(default=False)
    subscriptionenddate: date

