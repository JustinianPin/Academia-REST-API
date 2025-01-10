from fastapi import APIRouter, HTTPException
from Servicies.discipline_service import DisciplineService

router = APIRouter()

@router.get("/lectures/{id}")
async def get_discipline(id: int):
    print(f"GET discipline with ID {id}")
    discipline = DisciplineService.get_discipline_by_id(id)
    if not discipline:
        raise HTTPException(status_code=404, detail="Discipline not found")
    return {
        "id": discipline.id,
        "cod": discipline.cod,
        "id_titular": discipline.id_titular,
        "nume_disciplina": discipline.nume_disciplina,
        "an_studiu": discipline.an_studiu,
        "tip_disciplina": discipline.tip_disciplina,
        "categorie_disciplina": discipline.categorie_disciplina,
        "tip_examinare": discipline.tip_examinare,
    }

@router.get("/lectures")
def get_disciplines():
    print("GET all disciplines")
    disciplines = DisciplineService.get_all_disciplines()
    return {"disciplines": disciplines}

@router.post("/lectures")
async def create_discipline(discipline_data: dict):
    print("Creating a new discipline...")
    discipline = DisciplineService.create_discipline(discipline_data)
    return {
        "id": discipline.id,
        "cod": discipline.cod,
        "id_titular": discipline.id_titular,
        "nume_disciplina": discipline.nume_disciplina,
        "an_studiu": discipline.an_studiu,
        "tip_disciplina": discipline.tip_disciplina,
        "categorie_disciplina": discipline.categorie_disciplina,
        "tip_examinare": discipline.tip_examinare,
    }

@router.delete("/lectures/{id}")
async def delete_discipline(id: int):
    print(f"Try to delete discipline with ID {id}")
    discipline = DisciplineService.get_discipline_by_id(id)
    if not discipline:
        raise HTTPException(status_code=404, detail="Discipline not found")
    
    try:
        DisciplineService.delete_discipline(id)
        return {
            "message": f"Discipline with ID {id} has been successfully deleted.",
            "status": 200
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
