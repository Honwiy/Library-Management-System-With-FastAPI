from decimal import Decimal
from pydantic import BaseModel, Field
from datetime import datetime, timezone

  
class CreateUserRequest(BaseModel):
    account_number: str = Field(min_length=3, max_length=45)
    name: str = Field(min_length=3, max_length=100)
    password: str = Field(min_length=6, max_length=100)
    email: str = Field(min_length=12, max_length=45)
    account_balance: Decimal = Field(gt=0, max_digits=10, decimal_places=2)
    is_admin: int = Field(default=0)
    is_deleted: int = Field(default=0)
    created_date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
