import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class UserModel(Base):
    __tablename__ = "users"

    uuid: Mapped[str] = mapped_column(
        "uuid",
        sa.Uuid,
        primary_key=True,
    )
    name: Mapped[str]
    email: Mapped[str]