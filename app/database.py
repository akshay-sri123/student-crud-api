"""
Database operations for the model
"""
from .models import db

def get_all(model):
    """
    Return all students
    """
    data = model.query.all()
    return data


def get_by_id(model, student_id):
    """
    Get student by id
    """
    data = model.query.filter_by(id=student_id).first()
    return data


def update_by_id(model, student_id, **kwargs):
    """
    Update student by id
    """
    model.query.filter_by(id=student_id).update(dict(**kwargs))
    commit_changes()


def delete_by_id(model, student_id):
    """
    Delete student by id
    """
    model.query.filter_by(id=student_id).delete()
    commit_changes()


def add_students(model, **kwargs):
    """
    Add a student
    """
    student = model(**kwargs)
    db.session.add(student)
    commit_changes()


def commit_changes():
    """
    Commit the changes to the database
    """
    db.session.commit()
    