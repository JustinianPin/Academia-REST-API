from http import HTTPStatus
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from Servicies.discipline_service import DisciplineService
from Servicies.professor_service import ProfessorService
from Servicies.serialize_functions import serialize_professor

router = APIRouter()

@router.get("/professors/{id}")
async def get_professor(id: int):
    professor = ProfessorService.get_professor_by_id(id)
    if not professor:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Professor not found")
    
    response = serialize_professor(professor)
    response["links"] = [
        {"rel": "self", "href": f"/api/academia/professors/{professor.id}"},
        {"rel": "lectures", "href": f"/api/academia/professors/{professor.id}/lectures"},
        {"rel": "parent", "href": "/api/academia/professors"}
    ]
    
    return JSONResponse(content=response, status_code=HTTPStatus.OK)



@router.get("/professors/{id}/lectures")
async def get_professor_lectures(id: int):
    print(f"GET lectures for professor with ID {id}")
    professor = ProfessorService.get_professor_by_id(id)
    if not professor:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Professor not found")

    lectures = DisciplineService.get_disciplines_by_professor(id)
    if not lectures:
        return JSONResponse(
            content={"message": "No lectures found for this professor"},
            status_code=HTTPStatus.NOT_FOUND
        )
    lectures_data = [
        {
            "id": lecture.id,
            "nume_disciplina": lecture.nume_disciplina,
            "links": [
                {"rel": "self", "href": f"/api/academia/lectures/{lecture.id}"},
                {"rel": "parent", "href": f"/api/academia/professors/{id}/lectures"}
            ]
        }
        for lecture in lectures
    ]

    return JSONResponse(content={"lectures": lectures_data}, status_code=HTTPStatus.OK)


@router.get("/professors")
def get_professors():
    print("GET all professors")
    professors = ProfessorService.get_all_professors()
    return {"professors": professors}

@router.post("/professors")
async def create_professor(data: dict):
    try:
        professor = ProfessorService.create_professor(data)
        return JSONResponse(
            content={"message": "Professor created successfully", "id": professor.id},
            status_code=HTTPStatus.CREATED
        )
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))


@router.delete("/professors/{id}")
async def delete_professor(id: int):
    print(f"Attempting to delete professor with ID {id}")
    professor = ProfessorService.get_professor_by_id(id)
    if not professor:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Professor not found")
    
    try:
        ProfessorService.delete_professor(id)
        return JSONResponse(
            content={
                "message": f"Professor with ID {id} has been successfully deleted.",
                "status": HTTPStatus.OK
            },
            status_code=HTTPStatus.OK
        )
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=f"Unexpected error: {str(e)}")
