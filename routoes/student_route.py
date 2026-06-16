from fastapi import APIRouter , HTTPException
from database.student_repository import StudentsDB
from service.student_service import DefinitioStudent
from log.logger1 import logger

student = StudentsDB() 

router = APIRouter(prefix="/studets")


@router.post("/")
def create_student(body:DefinitioStudent):
    return student.create_student(body)



@router.get("/")
def get_all_students():
    return student.get_all_students()



@router.get("/count-all")
def count_students():
    return student.count_students()



@router.get("/{id}")
def get_student(id:int):
    data_student = student.get_student_by_id(id)
    if data_student:
        logger.info("seuccess: The sql fond the student")
        return data_student
    raise HTTPException(404, f"There is no such thing id={id}")




@router.patch("/{id}")
def update_student_name(id:int, new_name:str):
    data = student.update_name_by_id(new_name, id)
    if data != 0:
        return {"seuccess": True}
    raise HTTPException(404, f"There is no such thing id={id}")






@router.delete("/{id}")
def delete_student(id:int):
    data = student.delete_student_by_id(id)
    if data != 0:
        return {"delete seusccess": True} 
    raise HTTPException(404, f"There is no such thing id={id}")
