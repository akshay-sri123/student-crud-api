"""
Main app
"""
import json
from datetime import datetime
from flask import request
from .models import Students

from . import create_app, database

app = create_app()

@app.route('/getall', methods=['GET'])
def get():
    """
    Function to fetch info for all students
    """
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
    """
    Function to add a student
    """
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


@app.route('/get/<student_id>', methods=['GET'])
def get_by_id(student_id):
    """
    Function to fetch a student by their id
    """
    student = database.get_by_id(Students, student_id)
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

    return json.dumps(student_info, default=str), 200

@app.route('/del/<student_id>', methods=['DELETE'])
def delete_by_id(student_id):
    """
    Function to delete a student by their id
    """
    database.delete_by_id(Students, student_id)
    return json.dumps("Deleted"), 200

@app.route('/update/<student_id>', methods=['PUT'])
def update_by_id(student_id):
    """
    Function to update a student by their id
    """
    request_data = request.get_json()

    name = request_data['name']
    date_of_birth = datetime.strptime(str(request_data['date_of_birth']), '%Y-%m-%d')
    gender = request_data['gender']
    email_id= request_data['email_id']
    address = request_data['address']

    database.update_by_id(Students, student_id, name = name,
                                    date_of_birth = date_of_birth,
                                    gender = gender,
                                    email_id = email_id,
                                    address = address,
                                    created_at = datetime.now(),
                                    updated_at = datetime.now())

    return json.dumps("Updated"), 200
