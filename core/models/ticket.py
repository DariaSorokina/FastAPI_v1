from datetime import date
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column
from .base import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .product import Product

class Ticket(Base):
    data: Mapped[date]
    room: Mapped[str]
    row: Mapped[int]
    seat: Mapped[int]
    price: Mapped[int]

    # product_id: Mapped[int] = mapped_column(ForeignKey('products.id'), nullable=True)
    # product: Mapped["Product"] = relationship(
    #     back_populates="tickets")
