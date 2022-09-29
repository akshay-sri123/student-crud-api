from .models import db


def get_all(model):
    data = model.query.all()
    return data

def get_by_id(model, id):
    data = model.query.filter_by(id=id).first()
    return data

def delete_by_id(model, id):
    model.query.filter_by(id=id).delete()
    commit_changes()

def add_students(model, **kwargs):
    student = model(**kwargs)
    db.session.add(student)
    commit_changes()

def commit_changes():
    db.session.commit()