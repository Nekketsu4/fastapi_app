from sqlalchemy.orm import Mapped

from .database import Base


class User(Base):

    email: Mapped[str]
    password: Mapped[str]
