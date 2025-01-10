from Models.database import db
from Models.professor import Professor

class ProfessorService:
    @staticmethod
    def get_professors():
        print("Fetching professors from database...")
        with db.atomic():
            professors = list(Professor.select())
            print(f"Found {len(professors)} professors.")
            return professors

    @staticmethod
    def get_all_professors():
        professors = Professor.select()
        return [
            {
                "id": professor.id,
                "nume": professor.nume,
                "prenume": professor.prenume,
                "email": professor.email,
                "grad_didactic": professor.grad_didactic,
                "tip_asociere": professor.tip_asociere,
                "afiliere": professor.afiliere,
            }
            for professor in professors
        ]

    @staticmethod
    def get_professor_by_id(professor_id: int):
        try:
            return Professor.get(Professor.id == professor_id)
        except Professor.DoesNotExist:
            return None

    @staticmethod
    def create_professor(data: dict):
        with db.atomic():
            professor = Professor.create(
                nume=data["nume"],
                prenume=data["prenume"],
                email=data["email"],
                grad_didactic=data["grad_didactic"],
                tip_asociere=data["tip_asociere"],
                afiliere=data["afiliere"],
            )
            return professor
 