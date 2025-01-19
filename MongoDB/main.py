from fastapi import FastAPI
from app.Controllers import discipline_controller
from app.Services.discipline_service import delete_discipline_by_null_id
import config as config

app = FastAPI()

app.include_router(discipline_controller.router)

#deleted_count = delete_discipline_by_null_id()
#print(f"Number of deleted documents: {deleted_count}")

@app.get("/")
def read_root():
    return {"message": "Welcome to Moodle Simulation API"}
