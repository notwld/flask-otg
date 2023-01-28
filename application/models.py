from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from application.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(12))

    def __init__(self, name=None, fullname=None, password=None):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)
    
# more models here...