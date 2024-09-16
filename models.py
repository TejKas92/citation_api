from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Citation(Base):
    __tablename__ = "citations"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, unique=True, index=True)
    autor = Column(String, index=True)
    language = Column(String, index=True)
