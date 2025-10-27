from contextlib import asynccontextmanager

from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import _init_db
import requests as rq

@asynccontextmanager
async def lifespan(app_: FastAPI):
    await _init_db()
    print('Bot is ready')
    yield


app = FastAPI(title="CHIRISAN REGISTRATION" , lifespan= lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get("/api/sportsmams/{tg_id}")
async def sportsmans(tg_id: int):
    user = await rq.add_user(tg_id)
    return await rq.get_sportsmans(user.id)

@app.get("/api/main/{tg_id}")
async def profile(tg_id: int):
    user - await rq.add_user(tg_id)
    completed_sportsmans_count = await rq.get_completed_sportsmans_count(user.id)
    return {'completedSportsmans' : completed_sportsmans_count}












