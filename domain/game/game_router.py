# 라우트들
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from domain.game import game_schema, game_crud
from models import Game
from starlette.requests import Request

router = APIRouter(
    prefix="/game",
)


# # 전체 경기 조회 라우트 (경기 결과, 승리 비율 가져오기)
# @router.get("/")
# def Single_game_list(request: Request, db: Session = Depends(get_db)):
#     return
    






# # 택원 라우트 참고용
# @router.get('/info')
# async def user_info(request: Request, db: Session = Depends(get_db)):#, response_model=list[user_schema.User]):
#     user = request.session.get('user')
#     if not user:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="로그인안함")
#     userdb = db.query(User).filter_by(email=user["email"]).first()

#     if userdb:
#         return userdb.__dict__ # 모든 column 출력
#     else:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="사용자를 찾을 수 없음")


















# @router.get("/list")
# def game_list(db: Session = Depends(get_db), response_model=list[game_schema.Game]):
#     _game_list = game_crud.get_game_list(db)
#     return _game_list


# @router.get("/detail/{game_id}", response_model=game_schema.Game)
# def game_detail(game_id: int, db: Session = Depends(get_db)):
#     game = game_crud.get_game(db, game_id=game_id)
#     return game