from pydantic import BaseModel , Field
from typing import Optional



class DefinitioStudent(BaseModel):
    id: int
    name: str =Field(max_length=50)
    age:int
    course: str = Field(max_length=100)
    email: Optional[str] = None
