from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .dependencies import show_by_id
from .schemas import Show, ShowCreate, ShowUpdate

router = APIRouter(tags=["Спектакли"])


@router.get("/", response_model=list[Show])
async def get_shows(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_shows(session=session)


@router.post(
    "/",
    response_model=Show,
    status_code=status.HTTP_201_CREATED,
)
async def create_show(
    show_in: Annotated[ShowCreate, Depends()],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    return await crud.create_show(session=session, show_in=show_in)


@router.get("/{show_id}/", response_model=Show)
async def get_show(
    show: Show = Depends(show_by_id),
):
    return show


@router.put("/{show_id}/")
async def update_show(
    show_update: Annotated[ShowCreate, Depends()],
    show: Show = Depends(show_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_show(
        session=session,
        show=show,
        show_update=show_update,
    )
