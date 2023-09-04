from sqlalchemy import select

from fastapi import APIRouter, Depends
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.schemas import RoleCreate
from app.database import get_async_session
from app.auth.models import role, user

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post('/add/role')
async def set_role(new_role: RoleCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(role).values(**new_role.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.get('/users')
async def get_users(session: AsyncSession = Depends(get_async_session)):
    query = select(user.c['id', 'username', 'email', 'registered_at', 'role_id'])
    result = await session.execute(query)
    return {
        "status": "success",
        "data": result.mappings().all(),
        "details": None
    }
