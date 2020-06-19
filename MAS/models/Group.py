from dataclasses import dataclass

from MAS.application import db
from MAS.models.User_Group import User_Group

@dataclass
class Group(db.Model):
    __tablename__ = 'group'
    __table_args__ = {'extend_existing': True}

    users: list = db.relationship('Tenant', secondary=User_Group, backref='Group')

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(100), nullable=False)
    preferred_locations: str = db.Column(db.String(100))
    preferred_room_quantity: int = db.Column(db.Integer)
    preferred_size: int = db.Column(db.Integer)
    budget: int = db.Column(db.Integer)


