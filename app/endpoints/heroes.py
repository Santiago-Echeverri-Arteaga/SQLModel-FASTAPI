from fastapi import APIRouter
from ..models.heroes import Hero
from ..database.heroes import create_hero, delete_heroe, get_hero, get_heroes, delete_heroe, update_heroe

router = APIRouter()

@router.post("/create", response_model=Hero)
def create(hero: Hero):
    return create_hero(hero.dict())

@router.get("/get/{id}")
def get_by_id(id: str):
    return get_hero(id)

@router.get("/all")
def get_all():
    return get_heroes()

@router.delete("/delete")
def delete(hero: Hero):
    return delete_heroe(hero.dict())

@router.patch("/update")
def update(hero: Hero):
    return update_heroe(hero.dict())