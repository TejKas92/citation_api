from pydantic import BaseModel
from enum import Enum

class Languages(str, Enum):
    french = "fr"
    english = "en"
    spanish = "sp"

class Citation(BaseModel):
    text: str
    autor: str
    language: Languages