from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .dependencies import poster_by_id
from .schemas import Poster, PosterCreate, PosterUpdate, PosterUpdatePartial, PosterBase

router = APIRouter(tags=["Афиша"])


@router.get("/", response_model=list[Poster])
async def get_posters(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_posters(session=session)


@router.post(
    "/",
    response_model=Poster,
    status_code=status.HTTP_201_CREATED,
)
async def create_poster(
    poster_in: Annotated[PosterCreate, Depends()],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_poster(session=session, poster_in=poster_in)


@router.get("/{poster_id}/", response_model=Poster)
async def get_poster(
    poster: Poster = Depends(poster_by_id),
):
    return poster


@router.put("/{poster_id}/")
async def update_poster(
    poster_update: Annotated[PosterUpdate, Depends()],
    poster: Poster = Depends(poster_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_poster(
        session=session,
        poster=poster,
        poster_update=poster_update,
    )


@router.delete("/{poster_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_poster(
    poster: Poster = Depends(poster_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_poster(session=session, poster=poster)