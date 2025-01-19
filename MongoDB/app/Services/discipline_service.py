from fastapi import HTTPException
from pymongo import MongoClient
from app.Models.discipline import Discipline
from bson.objectid import ObjectId

client = MongoClient("mongodb://localhost:27017")
db = client["moodle_simulation"]
collection = db["disciplines"]

def serialize_objectid(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    return obj

def create_discipline(discipline_data: Discipline):
    existing_discipline = collection.find_one({"cod": discipline_data.cod})
    if existing_discipline:
        raise HTTPException(status_code=409, detail="Discipline already exists")
    discipline_dict = discipline_data.dict(exclude_unset=True)  
    result = collection.insert_one(discipline_dict)  
    return str(result.inserted_id)

def get_all_disciplines():
    disciplines = collection.find()
    return [ {**discipline, "_id": serialize_objectid(discipline["_id"])} for discipline in disciplines]

def get_discipline_by_id(discipline_id: str):
    discipline = collection.find_one({"_id": ObjectId(discipline_id)})
    if discipline:
        return {**discipline, "_id": serialize_objectid(discipline["_id"])}
    return None

def update_discipline(discipline_id: str, discipline_data: Discipline):
    existing_discipline = collection.find_one({"_id": ObjectId(discipline_id)})
    if not existing_discipline:
        return False 
    discipline_dict = discipline_data.dict(exclude_unset=True)
    collection.update_one(
        {"_id": ObjectId(discipline_id)}, 
        {"$set": discipline_dict}
    )
    return True


def delete_discipline(discipline_id: str):
    collection.delete_one({"_id": ObjectId(discipline_id)})
    return True

def delete_discipline_by_null_id():
    result = collection.delete_many({"_id": None})
    return result.deleted_count
