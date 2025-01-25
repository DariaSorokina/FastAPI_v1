from datetime import datetime, date
from sqlalchemy import func, DATE, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .acter import Acter

class Poster(Base):
    name_poster: Mapped[str]
    data: Mapped[date]
    acter: Mapped[str]

    acter_id: Mapped[int] = mapped_column(ForeignKey("acters.id")) #nullable=True
    acter_m: Mapped["Acter"] = relationship(back_populates="posters")
