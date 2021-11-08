from sqlalchemy import Column, Integer, String, Text
from models.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(128), unique=True)
    hashed_password = Column(String(128))
    point = Column(Text)

    def __init__(self, user_name=None, hashed_password=None, point=None):
        self.user_name = user_name
        self.hashed_password = hashed_password
        self.point = point

    def __repr__(self):
        return '<Name %r>' % (self.user_name)