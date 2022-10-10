"""
Model class for students
"""
from datetime import datetime
import enum
import flask_sqlalchemy
from flask_migrate import Migrate

db = flask_sqlalchemy.SQLAlchemy()
migrate = Migrate()


class GenderEnum(enum.Enum):
    """
    Enum for the gender field
    """
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'


class Students(db.Model): # pylint: disable=too-few-public-methods
    """
    DB class for students
    """
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    date_of_birth = db.Column(db.DateTime, nullable=True)
    gender = db.Column(db.Enum(GenderEnum), nullable=True)
    email_id = db.Column(db.String(100), unique=True)
    address = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())
