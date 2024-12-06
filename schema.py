from pydantic import BaseModel

class UserCreateSchema(BaseModel):
    username : str
    password : str
    role : str
    is_deleted: bool = False
    class Config:
        extra = "forbid"

class StudentCreateSchema(BaseModel):
    name : str
    surname : str
    FIN : str
    birth_date : str
    is_deleted: bool = False
    class Config:
        extra = "forbid"

class CourseCreateSchema(BaseModel):
    lecturer_id : int
    lesson_name : str
    lesson_description : str
    is_deleted: bool = False
    class Config:
        extra = "forbid"

class RegistrationCreateSchema(BaseModel):
    course_name : str
    student_name : str
    final_mark : str
    is_deleted: bool = False
    class Config:
        extra = "forbid"

