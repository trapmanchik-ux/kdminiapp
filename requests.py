from sqlalchemy import select , update ,delete , func
from models import async_session , User , Sportsman
from pydantic import BaseModel , ConfigDict
from typing import List

class SportsmansShema(BaseModel):
    id: int
    category: int
    name: str
    comanda: str
    sportorg: str
    dataage: int
    dan: str
    razrad: str
    FIOTren: str
    dso: str 
    vozrascategor: str
    user: int

    model_config=ConfigDict(from_attributes=True)


async def add_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if user:
            return user

            new_user = User(tg_id=tg_id)
            session.add(new_user)
            await session.commit()
            await sessiom.refresh(new_user)
            return new_user


async def get_sportsmans(user_id):
    async with async_session() as session:
        sportsmans = await sesion.scalars(
            select(Sportsman).where(Sportsman.user == user_id)
        )

        serialized_sportsmans = [
            SportsmanShema.model_validate(t).model_dump() for t in Sportsmans
        ]

        return serialized_sportsmans


async def get_completed_sportsmans_count(user_id):
    async with async_session() as session:
        return await session.scalar(select(func.count(Sportsman.id)))
