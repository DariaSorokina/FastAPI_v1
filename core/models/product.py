from datetime import date
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column
from .base import Base

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .show import Show
    from .ticket import Ticket


class Product(Base):
    name_show: Mapped[str]
    data: Mapped[date]
    price: Mapped[int]

    # show_id: Mapped[int] = mapped_column(
    #     ForeignKey('shows.id'), nullable=True)
    # show: Mapped["Show"] = relationship(back_populates="product")
    #
    # tickets: Mapped[list["Ticket"]] = relationship(back_populates="product")