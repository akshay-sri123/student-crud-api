from .models import db
from datetime import datetime

def get_all(model):
    data = model.query.all()
    return data

def get_by_id(model, id):
    data = model.query.filter_by(id=id).first()
    return data

def update_by_id(model, id, **kwargs):
    updated_student = model(**kwargs)
    db.session.query(model).filter_by(id=id).update(dict(**kwargs))
    commit_changes()

def delete_by_id(model, id):
    model.query.filter_by(id=id).delete()
    commit_changes()

def add_students(model, **kwargs):
    student = model(**kwargs)
    db.session.add(student)
    commit_changes()

def commit_changes():
    db.session.commit()