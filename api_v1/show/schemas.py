from datetime import date
from typing import Optional, Literal

from pydantic import BaseModel, ConfigDict


class ShowBase(BaseModel):
    mane_show: Optional[str] = None
    acter: Optional[str] = None
    data: Optional[date] = None


class ShowCreate(ShowBase):
    pass


class ShowUpdate(ShowCreate):
    pass


class Show(ShowBase):
    model_config = ConfigDict(from_attributes=True)

    id: int

