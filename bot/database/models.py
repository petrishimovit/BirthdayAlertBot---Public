from sqlalchemy.orm import Mapped , mapped_column
from sqlalchemy import LargeBinary

from database.base import Base

class Human(Base):

    __tablename__ = "human"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    name: Mapped[str]

    surname : Mapped[str]

    birthday_date : Mapped[str]

    photo: Mapped[bytes] = mapped_column(LargeBinary)