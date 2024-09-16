from sqlalchemy.orm import Session

import random

from models import Citation
from schemas import Languages

def get_citation(db: Session, language: Languages):
    citations = db.query(Citation).filter(Citation.language == language)
    nb_citations = citations.count()
    
    if nb_citations > 0:
        rd_num = random.randint(0, nb_citations-1)
        return citations[rd_num]
    else:
        return None
