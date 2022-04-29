from pydantic import BaseModel, Field
from uuid import uuid4

def generate_id():
    return str(uuid4())

class Hero(BaseModel):
    id: str= Field(default_factory=generate_id)
    heroname: str
    age: int