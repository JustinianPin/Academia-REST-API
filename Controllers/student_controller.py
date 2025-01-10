from fastapi import APIRouter, HTTPException
from Servicies.student_service import StudentService

router = APIRouter()

@router.get("/students/{id}")
async def get_student(id: int):
    print(f"GET student with ID {id}")
    student = StudentService.get_student_by_id(id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return {
        "id": student.id,
        "nume": student.nume,
        "prenume": student.prenume,
        "email": student.email,
        "ciclu_studii": student.ciclu_studii,
        "an_studiu": student.an_studiu,
        "grupa": student.grupa,
    }

@router.get("/students")
def get_students():
    print("GET all students")
    students = StudentService.get_all_students()
    return {"students": students}

@router.post("/students")
async def create_student(student_data: dict):
    print("Creating a new student...")
    student = StudentService.create_student(student_data)
    return {
        "id": student.id,
        "nume": student.nume,
        "prenume": student.prenume,
        "email": student.email,
        "ciclu_studii": student.ciclu_studii,
        "an_studiu": student.an_studiu,
        "grupa": student.grupa,
    }

@router.delete("/students/{id}")
async def delete_student(id: int):
    print(f"Try to delete student with ID {id}")
    student = StudentService.get_student_by_id(id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    try:
        StudentService.delete_student(id)
        return {
            "message": f"Student with ID {id} has been successfully deleted.",
            "status": 200
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
