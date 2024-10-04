from sqlalchemy import  create_engine, delete, select
from sqlalchemy.orm import sessionmaker
from models import Students
from config import settings

engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
)

ses = sessionmaker(engine)

def insert_student(name, second_name, date_bd, course):
    with ses() as sess:
        student = Students(name=name, second_name=second_name, date_bd=date_bd, course=course)
        sess.add(student)
        sess.commit()
        return True
        
def selet_all_student():
    with ses() as sess:
        res = sess.query(Students).all()
        answ = []
        for item in res:
            answ.append(f"id : {item.id}, name : {item.name}, second_name : {item.second_name}, date_bd : {item.date_bd}, course : {item.course}")
        return answ

                
def delete_student(std_id:int):
    
    with ses() as sess:
        try:
            std_id = int(std_id)
            stud = sess.query(Students).filter(Students.id == std_id)
            stud.delete(synchronize_session=False)
            sess.commit()
            return True
        except Exception as ex:
            print(ex)
        
        
        
def update_stud(std_id, name, second_name, date_bd, course):
    with ses() as sess:
        stud = sess.get(Students, std_id)
        stud.name=name 
        stud.second_name=second_name
        stud.date_bd=date_bd
        stud.course=course
        sess.commit()
        return True  
