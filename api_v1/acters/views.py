from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .dependencies import acter_by_id
from .schemas import Acter, ActerCreate, ActerUpdate, ActerUpdatePartial

router = APIRouter(tags=["Актеры"])


@router.get("/", response_model=list[Acter])
async def get_acters(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_acters(session=session)


@router.post(
    "/",
    response_model=Acter,
    status_code=status.HTTP_201_CREATED,
)
async def create_acter(
        acters_in: Annotated[ActerCreate, Depends()],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_acter(session=session, acters_in=acters_in)


@router.get("/{acter_id}/", response_model=Acter)
async def get_acter(
        acter: Acter = Depends(acter_by_id),
):
    return acter


@router.put("/{acter_id}/")
async def update_acter(
        acter_update: Annotated[ActerUpdate, Depends()],
        acter: Acter = Depends(acter_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_acter(
        session=session,
        acter=acter,
        acter_update=acter_update,
    )


@router.delete("/{acter_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_acter(
        acter: Acter = Depends(acter_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_acter(session=session, acter=acter)

