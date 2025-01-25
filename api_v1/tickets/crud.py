"""
Create
Read
Update
Delete
"""

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Ticket

from .schemas import TicketCreate, TicketUpdate


async def get_tickets(session: AsyncSession) -> list[Ticket]:
    stmt = select(Ticket).order_by(Ticket.id)
    result: Result = await session.execute(stmt)
    tickets = result.scalars().all()
    return list(tickets)


async def get_ticket(session: AsyncSession, ticket_id: int) -> Ticket:
    return await session.get(Ticket, ticket_id)


async def create_ticket(session: AsyncSession, ticket_in: TicketCreate) -> Ticket:
    ticket = Ticket(**ticket_in.model_dump())
    session.add(ticket)
    session.new
    await session.commit()
    return ticket


async def update_ticket(
    session: AsyncSession,
    ticket: Ticket,
    ticket_update: TicketUpdate,
    partial: bool = False,
) -> Ticket:
    for name, value in ticket_update.model_dump(exclude_unset=partial).items():
        setattr(ticket, name, value)
    await session.commit()
    return ticket


async def delete_ticket(
    session: AsyncSession,
    ticket: Ticket,
) -> None:
    await session.delete(ticket)
    await session.commit()