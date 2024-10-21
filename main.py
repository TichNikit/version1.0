import uvicorn
# uvicorn main:app --reload
# alembic revision --autogenerate -m "Initial migration"
# alembic upgrade head
from fastapi import FastAPI, status, Body, HTTPException, Request
from fastapi.responses import HTMLResponse

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db

from typing import Annotated
from fastapi.templating import Jinja2Templates

from app.models.game import Game
from app.models.user import User
from app.routers import user, game, user_game_feedback, user_game_rating

from sqlalchemy import insert, select, update, delete

app = FastAPI()
templates = Jinja2Templates(directory='templates')


@app.get("/")
async def get_(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('welcome.html', {"request": request})


@app.get("/list_user")
async def get_(request: Request, db: Annotated[Session, Depends(get_db)]) -> HTMLResponse:
    users = db.scalars(select(User)).all()
    return templates.TemplateResponse('list_user.html', {"request": request, "users": users})

@app.get("/list_game")
async def get_(request: Request, db: Annotated[Session, Depends(get_db)]) -> HTMLResponse:
    games = db.scalars(select(Game)).all()
    return templates.TemplateResponse('list_games.html', {"request": request, "games": games})



app.include_router(user.router_user)
app.include_router(game.router_game)
app.include_router(user_game_feedback.router_feedback)
app.include_router(user_game_rating.router_rating)
