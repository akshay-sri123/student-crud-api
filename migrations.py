import os
import psycopg2

conn = psycopg2.connect(
        host="127.0.0.1",
        database="student_crud_api",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS students;')
cur.execute('DROP TYPE IF EXISTS gender_type;')
cur.execute("CREATE TYPE gender_type AS ENUM('Male', 'Female', 'Other');")
cur.execute('CREATE TABLE students (id SERIAL PRIMARY KEY, '
                                 'name VARCHAR (50) NOT NULL, '
                                 'date_of_birth DATE NOT NULL, '
                                 'gender gender_type, '
                                 'email_id VARCHAR (50) UNIQUE, '
                                 'address TEXT, '
                                 'created_at date DEFAULT CURRENT_TIMESTAMP, '
                                 'updated_at date DEFAULT CURRENT_TIMESTAMP);'
                                 )
conn.commit()
cur.close()
conn.close()
