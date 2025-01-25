from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .dependencies import ticket_by_id
from .schemas import Ticket, TicketCreate, TicketUpdate

router = APIRouter(tags=["Билеты"])


@router.get("/", response_model=list[Ticket])
async def get_tickets(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_tickets(session=session)


@router.post(
    "/",
    response_model=Ticket,
    status_code=status.HTTP_201_CREATED,
)
async def create_ticket(
    ticket_in: Annotated[TicketCreate, Depends()],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    return await crud.create_ticket(session=session, ticket_in=ticket_in)


@router.get("/{ticket_id}/", response_model=Ticket)
async def get_ticket(
    ticket: Ticket = Depends(ticket_by_id),
):
    return ticket


@router.put("/{ticket_id}/")
async def update_ticket(
    ticket_update: Annotated[TicketUpdate, Depends()],
    ticket: Ticket = Depends(ticket_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_ticket(
        session=session,
        ticket=ticket,
        ticket_update=ticket_update,
    )
