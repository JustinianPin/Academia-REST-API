from pydantic import BaseModel, Field
from typing import List, Optional

class Discipline(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    cod: str
    nume_disciplina: str
    an_studiu: int
    tip_disciplina: str
    categorie_disciplina: str
    tip_examinare: str
    id_titular: Optional[int] = None  
    course_material: Optional[str] = None
    lab_material: Optional[str] = None

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "cod": "SD104",
                "nume_disciplina": "Sisteme de Operare",
                "an_studiu": 3,
                "tip_disciplina": "impusa",
                "categorie_disciplina": "specialitate",
                "tip_examinare": "examen",
                "id_titular": 1
            }
        }
