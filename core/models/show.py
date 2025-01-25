from datetime import date
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .acter import Acter



class Show(Base):
    mane_show: Mapped[str]
    acter: Mapped[str]
    data: Mapped[date]

    # acter_id: Mapped[int] = mapped_column(ForeignKey('acters.id'), nullable=True)
    # acter_m: Mapped["Acter"] = relationship(back_populates="show")
    #
    # product: Mapped[list["Product"]] = relationship(back_populates="show")