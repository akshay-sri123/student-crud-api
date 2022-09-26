import flask_sqlalchemy
import enum
from datetime import datetime

db = flask_sqlalchemy.SQLAlchemy()

class GenderEnum(enum.Enum):
    Male = 'Male' 
    Female = 'Female'
    Other = 'Other'

class Students(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    date_of_birth = db.Column(db.DateTime, nullable=True)
    gender = db.Column(db.Enum(GenderEnum), nullable=True)
    email_id = db.Column(db.String(100), unique=True)
    address = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())
