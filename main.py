from fastapi import FastAPI
from Controllers.professor_controller import router as professor_router
from Controllers.student_controller import router as student_router
from Controllers.discipline_controller import router as discipline_router
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)

@app.on_event("startup")
async def startup_event():
    logging.info("Aplicatia a pornit corect!")
    logging.info("Rutele inregistrate:")
    for route in app.router.routes:
        logging.info(f"Path: {route.path}, Methods: {route.methods}")

app.include_router(professor_router, prefix="/api/academia", tags=["Professors"])
app.include_router(student_router, prefix="/api/academia", tags=["Students"])
app.include_router(discipline_router, prefix="/api/academia", tags=["Lectures"])
