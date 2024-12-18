from fastapi import FastAPI
from login import login_router
from users import user_router
from students import student_router
from course import course_router

app = FastAPI(title="Student management system",description="This app for course registration and lecturer, student")

@app.get("/")
def heaalth_check():
    return {'Message':"Health check is succesfull"}

app.include_router(course_router)

app.include_router(student_router)

app.include_router(user_router)

app.include_router(login_router)