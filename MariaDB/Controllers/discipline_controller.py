from http import HTTPStatus
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from Servicies.discipline_service import DisciplineService
from Servicies.serialize_functions import serialize_discipline, serialize_student

router = APIRouter()

@router.get("/lectures/{id}")
async def get_discipline(id: int):
    print(f"GET discipline with ID {id}")
    discipline = DisciplineService.get_discipline_by_id(id)
    if not discipline:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Discipline not found")
    
    response = serialize_discipline(discipline)

    response["links"] = [
        {"rel": "self", "href": f"/api/academia/lectures/{discipline.id}"},
        {"rel": "students", "href": f"/api/academia/lectures/{discipline.id}/students"},
        {"rel": "professor", "href": f"/api/academia/professors/{discipline.id_titular}"},
        {"rel": "parent", "href": "/api/academia/lectures"}
    ]
    
    return JSONResponse(content=response, status_code=HTTPStatus.OK)

@router.get("/lectures")
def get_disciplines():
    print("GET all disciplines")
    disciplines = DisciplineService.get_all_disciplines()
    return {"disciplines": disciplines}

@router.post("/lectures")
async def create_discipline(discipline_data: dict):
    print("Creating a new discipline...")
    discipline = DisciplineService.create_discipline(discipline_data)
    return JSONResponse(
        content={
            "message": "Discipline created successfully",
            "id": discipline.id,
            "cod": discipline.cod,
            "id_titular": discipline.id_titular,
            "nume_disciplina": discipline.nume_disciplina,
            "an_studiu": discipline.an_studiu,
            "tip_disciplina": discipline.tip_disciplina,
            "categorie_disciplina": discipline.categorie_disciplina,
            "tip_examinare": discipline.tip_examinare,
        },
        status_code=HTTPStatus.CREATED
    )

@router.delete("/lectures/{id}")
async def delete_discipline(id: int):
    print(f"Try to delete discipline with ID {id}")
    discipline = DisciplineService.get_discipline_by_id(id)
    if not discipline:
        raise HTTPException(status_code=404, detail="Discipline not found")
    
    try:
        DisciplineService.delete_discipline(id)
        return JSONResponse(
            content={
                "message": f"Discipline with ID {id} has been successfully deleted.",
                "status": HTTPStatus.OK
            },
            status_code=HTTPStatus.OK
        )
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=f"Unexpected error: {str(e)}")

@router.get("/lectures/{id}/students")
async def get_lecture_students(id: int):
    discipline = DisciplineService.get_discipline_by_id(id)
    if not discipline:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Discipline not found"
        )

    students = DisciplineService.get_students_by_discipline(id)

    if not students:
        return JSONResponse(
            content={"message": "No students found for this discipline"},
            status_code=HTTPStatus.NOT_FOUND
        )

    students_data = [serialize_student(student) for student in students]

    return JSONResponse(
        content={"students": students_data},
        status_code=HTTPStatus.OK
    )