from fastapi import APIRouter, HTTPException
from app.Models.discipline import Discipline
from app.Services.discipline_service import (
    create_discipline, get_all_disciplines, get_discipline_by_id, update_discipline, delete_discipline
)

router = APIRouter()

@router.post("/disciplines/")
def add_discipline(discipline: Discipline):
    return {"id": create_discipline(discipline)}

@router.get("/disciplines/")
def list_disciplines():
    return get_all_disciplines()

@router.get("/disciplines/{discipline_id}")
def read_discipline(discipline_id: str):
    discipline = get_discipline_by_id(discipline_id)
    if not discipline:
        raise HTTPException(status_code=404, detail="Discipline not found")
    return discipline

@router.put("/disciplines/{discipline_id}")
def modify_discipline(discipline_id: str, discipline: Discipline):
    if update_discipline(discipline_id, discipline):
        return {"message": "Discipline updated successfully"}
    raise HTTPException(status_code=404, detail="Discipline not found")

@router.delete("/disciplines/{discipline_id}")
def remove_discipline(discipline_id: str):
    if delete_discipline(discipline_id):
        return {"message": "Discipline deleted successfully"}
    raise HTTPException(status_code=404, detail="Discipline not found")
