from fastapi import APIRouter, HTTPException
from Servicies.professor_service import ProfessorService

router = APIRouter()

@router.get("/professors/{id}")
async def get_professor(id: int):
    print(f"GET professor with ID {id}")
    professor = ProfessorService.get_professor_by_id(id)
    if not professor:
        raise HTTPException(status_code=404, detail="Professor not found")
    return {
        "id": professor.id,
        "nume": professor.nume,
        "prenume": professor.prenume,
        "email": professor.email,
        "grad_didactic": professor.grad_didactic,
        "tip_asociere": professor.tip_asociere,
        "afiliere": professor.afiliere,
    }

@router.get("/professors")
def get_professors():
    print("GET all professors")
    professors = ProfessorService.get_all_professors()
    return {"professors": professors}

@router.post("/professors")
async def create_professor(professor_data: dict):
    print("Creating a new professor...")
    professor = ProfessorService.create_professor(professor_data)
    return {
        "id": professor.id,
        "nume": professor.nume,
        "prenume": professor.prenume,
        "email": professor.email,
        "grad_didactic": professor.grad_didactic,
        "tip_asociere": professor.tip_asociere,
        "afiliere": professor.afiliere,
    }

@router.delete("/professors/{id}")
async def delete_professor(id: int):
    print(f"Attempting to delete professor with ID {id}")
    professor = ProfessorService.get_professor_by_id(id)
    if not professor:
        raise HTTPException(status_code=404, detail="Professor not found")
    
    try:
        ProfessorService.delete_professor(id)
        return {
            "message": f"Professor with ID {id} has been successfully deleted.",
            "status": 200
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected erorr: {str(e)}")
