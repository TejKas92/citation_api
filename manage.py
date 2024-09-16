import sys

from schemas import Languages
from models import Citation
from database import SessionLocal

from french_citations import citations as french_citations
from english_citations import citations as english_citations
from spanish_citations import citations as spanish_citations

def init_french_citations():
    db = SessionLocal()
    try:
        db_citations = [
            Citation(text=cit["citation"], autor=cit["autor"], language=Languages.french)
            for cit in french_citations
        ]
        db.bulk_save_objects(db_citations)
        db.commit()
    finally:
        db.close

def init_english_citations():
    db = SessionLocal()
    try:
        db_citations = [
            Citation(text=cit["citation"], autor=cit["autor"], language=Languages.english)
            for cit in english_citations
        ]
        db.bulk_save_objects(db_citations)
        db.commit()
    finally:
        db.close

def init_spanish_citations():
    db = SessionLocal()
    try:
        db_citations = [
            Citation(text=cit["citation"], autor=cit["autor"], language=Languages.spanish)
            for cit in spanish_citations
        ]
        db.bulk_save_objects(db_citations)
        db.commit()
    finally:
        db.close

def delete_all_citations():
    db = SessionLocal()
    try:
        db.query(Citation).delete()
        db.commit()
    finally:
        db.close

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "init_french_citations":
            init_french_citations()
        elif sys.argv[1] == "init_english_citations":
            init_english_citations()
        elif sys.argv[1] == "init_spanish_citations":
            init_spanish_citations()
        elif sys.argv[1] == "delete_all_citations":
            delete_all_citations()
        else:
            print("unknow command")
    else:
        print("you should indicate a command")
