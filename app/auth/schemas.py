from typing import Optional
import re
from fastapi_users import schemas
from pydantic import BaseModel, field_validator, Field, EmailStr


class RoleCreate(BaseModel):
    id: int
    name: str

    @field_validator('name')
    def check_name(cls, v: str) -> str:
        if len(v) < 3 or len(v) > 15:
            raise ValueError('Role name must be greater than 3 and less than 15')
        return v



password_regex = "((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W]).{8,64})"


class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    username: str
    role_id: int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: EmailStr
    password: str
    role_id: int
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

    @field_validator('password')
    def check_password(cls, v: str) -> str:
        print(re.match(password_regex, v))
        return v
