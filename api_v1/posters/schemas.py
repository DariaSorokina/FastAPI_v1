from dataclasses import Field
from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class PosterBase(BaseModel):
    name_poster: Optional[str] = None
    data: Optional[date] = None
    acter: Optional[str] = None


class PosterCreate(PosterBase):
    pass


class PosterUpdate(PosterCreate):
    pass


class PosterUpdatePartial(PosterCreate):
    name_poster: Optional[str] = None
    data: date = None
    acter: Optional[str] = None


class Poster(PosterBase):
    model_config = ConfigDict(from_attributes=True)
    id: int