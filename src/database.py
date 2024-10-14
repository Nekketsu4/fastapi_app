from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    declared_attr,
)
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
)

from .config import settings


# engine = create_async_engine(
#     url=settings.db_url,
#     echo=settings.db_echo,
# )
#
# async_session_maker = async_sessionmaker(
#     bind=engine,
#     autoflush=False,
#     autocommit=False,
#     expire_on_commit=False,
# )


class DBHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(url=url, echo=echo)

        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True)


db_helper = DBHelper(url=settings.db_url, echo=settings.db_echo)
