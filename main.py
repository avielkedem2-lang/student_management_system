from fastapi import FastAPI
from routoes import student_route
from database.db_management import DBConnector
from database.student_repository import StudentsDB


d1 = StudentsDB()
d1.create_table()

app = FastAPI()

app.include_router(student_route.router)