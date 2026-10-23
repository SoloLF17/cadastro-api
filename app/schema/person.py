from pydantic import BaseModel, ConfigDict, Field, EmailStr
from typing import Literal, Optional 
from enum import Enum
from uuid import UUID, uuid4

# camelCase = TestNome
# snake_case = test_nome

class UserStatus(Enum):
    ATIVO = True
    INATIVO = False

class PersonCreate(BaseModel):
    id: Optional[UUID] = Field(default_factory=uuid4)
    is_active: UserStatus = UserStatus.ATIVO   
    name: str
    age: int
    email: EmailStr


class PersonResponse(PersonCreate):
    model_config = ConfigDict(from_attributes= True)
    