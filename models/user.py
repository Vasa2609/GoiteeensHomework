from .database import BASE
from sqlalchemy import Column, Integer, String, Text



class User(BASE):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    title = Column(String(300), nullable=False)
    text = Column(Text, nullable=False)


    def __init__(self, title: str, text: str):
        self.title = title
        self.text = text

    def __repr__(self):
        return "User %r" % self.id