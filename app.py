import os
import psycopg2
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

conn = psycopg2.connect(host='127.0.0.1',
                        database='student_crud_api',
                        user=os.environ['DB_USERNAME'],
                        password=os.environ['DB_PASSWORD'])

def execute_query(stmt):
     cur =  conn.cursor()
     cur.execute(stmt)
     conn.commit()
     return cur
     
 
@app.route('/api/v1/students', methods=['POST'])
def add_student():
    request_data = request.get_json()

    insert_query = "INSERT INTO students (name, date_of_birth, gender, email_id, address, created_at, updated_at) VALUES ('{name}', '{date_of_birth}', '{gender}', '{email_id}', '{address}', current_timestamp, current_timestamp);".format(
        name = str(request_data['name']),
        date_of_birth = datetime.strptime(str(request_data['date_of_birth']), '%Y-%m-%d'),
        gender = str(request_data['gender']),
        email_id= str(request_data['email_id']),
        address = str(request_data['address'])
        )
    
    result_cur = execute_query(insert_query)
    result_cur.close()
    
    return "200"

@app.route('/api/v1/students', methods=['GET'])
def get_all():
    query = 'SELECT row_to_json(row) from (SELECT * FROM students) row;'
    result_cur = execute_query(query)
    result = []
    for i in result_cur.fetchall():
        result.append(i[0])
    result_cur.close()
    return result
    
if __name__ == '__main__':
        app.run(debug=True)