from fastapi import APIRouter
from database.student_repository import StudentsDB
from service.student_service import DefinitioStudent

student = StudentsDB() 

router = APIRouter(prefix="/studets")


@router.post("/")
def create_student(body:DefinitioStudent):
    return student.create_student(body)
