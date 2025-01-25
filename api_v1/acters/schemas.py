from typing import Optional, Literal

from pydantic import BaseModel, ConfigDict


class ActerBase(BaseModel):
    name: str
    show: str
    gender: Literal["Мужской", "Женский"] = "Женский"
    part: Literal["Главная роль", "Роль второго плана", "Групповка", "Массовка"] = "Главная роль"


class ActerCreate(ActerBase):
    pass


class ActerUpdate(ActerCreate):
    pass


class ActerUpdatePartial(ActerCreate):
    name: Optional[str] = None
    show: Optional[str] = None
    gender: Literal["Мужской", "Женский"] = "Женский"
    part: Literal["Главная роль", "Роль второго плана", "Групповка", "Массовка"] = "Главная роль"


class Acter(ActerBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
