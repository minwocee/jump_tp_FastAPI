# 테이블 저장소
from sqlalchemy import Column, Integer, String, Text, DateTime, TupleType, JSON, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# 유저
class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False)
    student_num = Column(Integer, nullable=True)
    name = Column(String(255), nullable=True)
    phone_num = Column(String(255), nullable=True)
    is_admin = Column(Boolean, nullable=False, default=False)
    games = Column(JSON, nullable=True)
    
# 게임
class Game(Base):
    __tablename__ = 'game'
    
    id = Column(Integer, primary_key=True)
    start_time = Column(DateTime, nullable=False)
    result = Column(Boolean, nullable=True)
    video_url = Column(String(255), nullable=False)           
    score_A = Column(Integer)    
    score_B = Column(Integer)  
    place = Column(String(255), nullable=False)
    team_A = Column(String(255), nullable=False)
    team_B = Column(String(255), nullable=False)
    category = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    
    user = relationship("User", backref="game")
    
# 전공
class Major(Base):
    __tablename__ = 'major'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    slogan = Column(Text, nullable=False)
    image = Column(Text, nullable=False) # How to show the image(by statics?)