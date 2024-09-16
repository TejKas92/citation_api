from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from schemas import Languages, Citation
from crud import get_citation
from models import Base
from database import SessionLocal, engine

Base.metadata.create_all(bind=engine)

#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()


@app.get("/citation/{language}", response_model=Citation)
def read_random_citation(language: Languages, db: Session = Depends(get_db)):
    return get_citation(db, language)
