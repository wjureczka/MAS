from dataclasses import dataclass

from sqlalchemy.orm import validates

from MAS.application import db


@dataclass
class User(db.Model):
    __tablename__ = 'user'
    __mapper_args = {
        'polymorphic_identity': 'user',
        'polymorphic_on': type
    }

    id: int = db.Column(db.Integer, primary_key=True, nullable=False)
    pesel: str = db.Column(db.String(11), unique=True, nullable=False)
    name: str = db.Column(db.String(50), nullable=False)
    surname: str = db.Column(db.String(50), nullable=False)
    email: str = db.Column(db.String(50), unique=True, nullable=False)

    @validates('email')
    def validate_email(self, key, email):
        assert '@' in email, "Not valid email: email should contain '@'"
        return email

    @validates('pesel')
    def validate_pesel(self, key, pesel):
        assert len(pesel) is 11, "Bad pesel's length"
        return pesel

    @validates('name')
    def validate_name(self, key, name):
        assert name is not None, "Name can not be empty"
        return name

    @validates('surname')
    def validate_surname(self, key, surname):
        assert surname is not None, "Surname can not be empty"
        return surname
