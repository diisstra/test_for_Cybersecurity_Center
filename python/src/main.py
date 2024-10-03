from fastapi import FastAPI
from database import insert_student, selet_all_student, delete_student, update_stud
 
app = FastAPI()

@app.get('/')
def start():
    return "http://localhost:1908/docs"
    
    
@app.get("/insert/{name, second_name, date_bd, course}")
def insert(name, second_name, date_bd, course):
    return insert_student(name, second_name, date_bd, course)


@app.get("/delete_student/{id}")
def delete_students(id):
    return delete_student(id)


@app.get("/update_student/{std_id, name, second_name, date_bd, course}")
def update_student(std_id, name, second_name, date_bd, course):
    return update_stud(std_id, name, second_name, date_bd, course)


@app.get("/selet_all_student/")
def selet_all_students():
    return selet_all_student()