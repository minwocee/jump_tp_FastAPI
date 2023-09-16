# game_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from domain.game import game_schema, game_crud
from models import Game
from starlette.requests import Request

router = APIRouter(
    prefix="/game",
)

@router.post('/new')  # 응답 모델을 지정합니다.
async def create_game(game: game_schema.Game, db: Session = Depends(get_db)):  
    # GameCreate 스키마에 따라 요청 본문에서 게임 정보를 파싱하고 이 결과로 생성된 객체(game)와 데이터베이스 세션(db)을 매개변수로 받습니다.
    db_game = game_crud.get_game_by_id(db, id=game.id)
    if db_game:
        raise HTTPException(status_code=400, detail="Game already registered")
    
    return {"message": "Db add complete"}