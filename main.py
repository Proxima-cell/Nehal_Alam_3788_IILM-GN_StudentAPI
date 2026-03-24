from fastapi import FastAPI
from sqlalchemy.orm import Session
from database import engine, SessionLocal
from model import Base, Student

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Student API is running"}
@app.post("/students")
def create_student(name: str, age: int, course: str):
    db: Session = SessionLocal()
    student = Student(name=name, age=age, course=course)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

@app.get("/students")
def get_students():
    db: Session = SessionLocal()
    return db.query(Student).all()