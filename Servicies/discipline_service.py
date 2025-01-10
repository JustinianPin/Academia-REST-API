from Models.database import db
from Models.discipline import Discipline

class DisciplineService:
    @staticmethod
    def get_disciplines():
        print("Fetching disciplines from database...")
        with db.atomic():
            disciplines = list(Discipline.select())
            print(f"Found {len(disciplines)} disciplines.")
            return disciplines

    @staticmethod
    def get_all_disciplines():
        disciplines = Discipline.select()
        return [
            {
                "id": discipline.id,
                "cod": discipline.cod,
                "id_titular": discipline.id_titular,
                "nume_disciplina": discipline.nume_disciplina,
                "an_studiu": discipline.an_studiu,
                "tip_disciplina": discipline.tip_disciplina,
                "categorie_disciplina": discipline.categorie_disciplina,
                "tip_examinare": discipline.tip_examinare,
            }
            for discipline in disciplines
        ]

    @staticmethod
    def get_discipline_by_id(discipline_id: int):
        try:
            return Discipline.get(Discipline.id == discipline_id)
        except Discipline.DoesNotExist:
            return None

    @staticmethod
    def create_discipline(data: dict):
        with db.atomic():
            discipline = Discipline.create(
                cod=data["cod"],
                id_titular=data["id_titular"],
                nume_disciplina=data["nume_disciplina"],
                an_studiu=data["an_studiu"],
                tip_disciplina=data["tip_disciplina"],
                categorie_disciplina=data["categorie_disciplina"],
                tip_examinare=data["tip_examinare"],
            )
            return discipline

    @staticmethod
    def delete_discipline(discipline_id: int):
        with db.atomic():
            discipline = Discipline.get_or_none(Discipline.id == discipline_id)
            if not discipline:
                raise ValueError("Discipline does not exist")
            discipline.delete_instance()
