from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, relationship, mapped_column

from .base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .poster import Poster
    from .show import Show

class Acter(Base):

    name: Mapped[str]
    show: Mapped[str]
    gender: Mapped[str]
    part: Mapped[str]

    posters: Mapped[list["Poster"]] = relationship(back_populates="acter_m")

    #show: Mapped[list["Show"]] = relationship(back_populates="acter_m")
