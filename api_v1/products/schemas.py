from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    name_show: str
    data: date
    price: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductCreate):
    name_show: Optional[str] = None
    data: Optional[date] = None
    price: Optional[int] = None


class ProductUpdatePartial(ProductCreate):
    name_show: Optional[str] = None
    data: Optional[date] = None
    price: Optional[int] = None


class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    id: int