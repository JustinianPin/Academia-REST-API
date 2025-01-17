from Models.database import db
from Models.student import Student

class StudentService:
    @staticmethod
    def get_students():
        print("Fetching students from database...")
        with db.atomic():
            students = list(Student.select())
            print(f"Found {len(students)} students.")
            return students

    @staticmethod
    def get_all_students():
        students = Student.select()
        return [
            {
                "id": student.id,
                "nume": student.nume,
                "prenume": student.prenume,
                "email": student.email,
                "ciclu_studii": student.ciclu_studii,
                "an_studiu": student.an_studiu,
                "grupa": student.grupa,
            }
            for student in students
        ]

    @staticmethod
    def get_student_by_id(student_id: int):
        try:
            return Student.get(Student.id == student_id)
        except Student.DoesNotExist:
            return None

    @staticmethod
    def create_student(data: dict):
        with db.atomic():
            student = Student.create(
                nume=data["nume"],
                prenume=data["prenume"],
                email=data["email"],
                ciclu_studii=data["ciclu_studii"],
                an_studiu=data["an_studiu"],
                grupa=data["grupa"],
            )
            return student

    @staticmethod
    def delete_student(student_id: int):
        with db.atomic():
            student = Student.get_or_none(Student.id == student_id)
            if not student:
                raise ValueError("Student does not exist")
            student.delete_instance()