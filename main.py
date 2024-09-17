from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database.schemas import Languages, Citation
from database.crud import get_citation
from database.models import Base
from database.database import SessionLocal, engine

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
