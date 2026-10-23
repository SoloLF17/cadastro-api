from uuid import UUID, uuid4

from sqlalchemy import Enum as SAEnum, String, Integer, Uuid
from sqlalchemy.orm import Mapped, mapped_column 
from app.schema.person import UserStatus
from app.database.connection import Base



class Person(Base):
    __tablename__ = "people"

    id: Mapped[UUID] = mapped_column(Uuid(as_uuid= True),primary_key=True, default=uuid4)
    is_active: Mapped[UserStatus] = mapped_column(SAEnum(UserStatus,name="status"))
    name: Mapped[str] = mapped_column()
    age: Mapped[int] = mapped_column()
    email: Mapped[str] = mapped_column()

    

