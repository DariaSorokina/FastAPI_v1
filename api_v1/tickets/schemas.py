from datetime import date
from typing import Optional, Literal

from pydantic import BaseModel, ConfigDict


class TicketBase(BaseModel):
    data: date
    room: Literal["Партер", "Балкон", "Амфитеатр", "Бельэтаж", "Бенуар"] = "Партер"
    row: int
    seat: int
    price: int



class TicketCreate(TicketBase):
    pass


class TicketUpdate(TicketCreate):
    data: Optional[date] = None
    room: Literal["Партер", "Балкон", "Амфитеатр", "Бельэтаж", "Бенуар"] = "Партер"
    row: Optional[int] = None
    seat: Optional[int] = None
    price: Optional[int] = None


class Ticket(TicketBase):
    model_config = ConfigDict(from_attributes=True)

    id: int