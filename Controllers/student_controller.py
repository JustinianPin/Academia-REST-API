from http import HTTPStatus
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from Servicies.discipline_service import DisciplineService
from Servicies.student_service import StudentService
from Servicies.serialize_functions import serialize_discipline, serialize_student

router = APIRouter()

@router.get("/students/{id}")
async def get_student(id: int):
    print(f"GET student with ID {id}")
    student = StudentService.get_student_by_id(id)
    if not student:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Student not found")
    
    response = serialize_student(student)

    response["links"] = [
        {"rel": "self", "href": f"/api/academia/students/{student.id}"},
        {"rel": "lectures", "href": f"/api/academia/students/{student.id}/lectures"},
        {"rel": "parent", "href": "/api/academia/students"}
    ]

    return JSONResponse(content=response, status_code=HTTPStatus.OK)

@router.get("/students/{id}/lectures")
async def get_student_lectures(id: int):
    student = StudentService.get_student_by_id(id)
    if not student:
        raise HTTPException(HTTPStatus.NOT_FOUND, detail="Student not found")

    lectures = DisciplineService.get_disciplines_by_student(id)

    if not lectures:
        return JSONResponse(
            content={"message": "No lectures found for this student"},
            status_code=HTTPStatus.NOT_FOUND
        )

    lectures_data = [
        serialize_discipline(lecture)
        for lecture in lectures
    ]

    return JSONResponse(content={"lectures": lectures_data}, status_code=HTTPStatus.OK)

@router.get("/students")
def get_students():
    print("GET all students")
    students = StudentService.get_all_students()
    return {"students": students}

@router.post("/students")
async def create_student(student_data: dict):
    print("Creating a new student...")
    student = StudentService.create_student(student_data)
    return JSONResponse(
        content={
            "id": student.id,
            "nume": student.nume,
            "prenume": student.prenume,
            "email": student.email,
            "ciclu_studii": student.ciclu_studii,
            "an_studiu": student.an_studiu,
            "grupa": student.grupa,
        },
        status_code=HTTPStatus.CREATED
    )

@router.delete("/students/{id}")
async def delete_student(id: int):
    print(f"Try to delete student with ID {id}")
    student = StudentService.get_student_by_id(id)
    if not student:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Student not found")
    
    try:
        StudentService.delete_student(id)
        return {
            "message": f"Student with ID {id} has been successfully deleted.",
            "status": HTTPStatus.OK
        }
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=f"Unexpected error: {str(e)}")
