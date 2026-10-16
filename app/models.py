from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class Incident(Base):
    __tablename__ = "incidents"

    id : Mapped[int] = mapped_column(primary_key= True)
    title : Mapped[str] = mapped_column(String(50))
    description : Mapped[str] = mapped_column(String(500))
    severity : Mapped[int]
    status : Mapped[str] = mapped_column(String(50))