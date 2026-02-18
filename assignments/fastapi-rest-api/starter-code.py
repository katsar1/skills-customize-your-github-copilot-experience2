"""
FastAPI REST API Starter Code

This starter file provides the basic structure for building a REST API.
Implement the tasks to create a fully functional API.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

# Initialize the FastAPI application
app = FastAPI(
    title="Student API",
    description="REST API for managing student records",
    version="1.0.0"
)

# TODO: Define a Pydantic model for Student data
# class Student(BaseModel):
#     id: int
#     name: str
#     email: str
#     grade: str


# TODO: Create an in-memory database (list of students)
# students_db = []


# TODO: Implement GET endpoint to retrieve all students
# @app.get("/students", response_model=List[Student])
# async def get_students():
#     pass


# TODO: Implement GET endpoint to retrieve a specific student by ID
# @app.get("/students/{student_id}", response_model=Student)
# async def get_student(student_id: int):
#     pass


# TODO: Implement POST endpoint to create a new student
# @app.post("/students", response_model=Student, status_code=status.HTTP_201_CREATED)
# async def create_student(student: Student):
#     pass


# TODO: Implement PUT endpoint to update a student
# @app.put("/students/{student_id}", response_model=Student)
# async def update_student(student_id: int, student: Student):
#     pass


# TODO: Implement DELETE endpoint to remove a student
# @app.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_student(student_id: int):
#     pass


# Root endpoint for testing
@app.get("/")
async def root():
    return {"message": "Welcome to the Student API"}


# Run with: uvicorn starter-code:app --reload
