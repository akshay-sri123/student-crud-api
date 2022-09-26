import json

from . import create_app, database
from .models import Students

from flask import request

from datetime import datetime


app = create_app()

@app.route('/', methods=['GET'])
def get():
    students = database.get_all(Students)
    print("students")
    all_students = []
    for student in students:
        student_info = {
          "id" : student.id,
          "name" : student.name,
          "date_of_birth" : student.date_of_birth,
          "gender" : student.gender,
          "email_id" : student.email_id,
          "address" : student.address,
          "created_at" : student.created_at,
          "updated_at" : student.updated_at
        }

        all_students.append(student_info)

    return json.dumps(all_students, default=str), 200
 
@app.route('/add', methods=['POST'])
def add():
    request_data = request.get_json()
    
    name = request_data['name']
    date_of_birth = datetime.strptime(str(request_data['date_of_birth']), '%Y-%m-%d')
    gender = request_data['gender']
    email_id= request_data['email_id']
    address = request_data['address']
    
    database.add_students(Students, name = name,
                                    date_of_birth = date_of_birth,
                                    gender = gender,
                                    email_id = email_id,
                                    address = address,
                                    created_at = datetime.now(),
                                    updated_at = datetime.now())
    
    return json.dumps("Added"), 200
