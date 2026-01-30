from sqlalchemy import Column, Integer, String
from db import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    time = Column(String, nullable=False)
    status = Column(Integer, nullable=False)
