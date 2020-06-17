from dataclasses import dataclass

from MAS.application import db


@dataclass
class RentalObject(db.Model):
    __tablename__ = 'rental_object'
    __mapper_args = {
        'polymorphic_identity': 'rental_object',
        'polymorphic_on': type
    }

    id: int = db.Column(db.Integer, primary_key=True, nullable=False)
    description: str = db.Column(db.String(200))
    area_description: str = db.Column(db.String(200))
    equipment: str = db.Column(db.String(200))
    address: str = db.Column(db.String)
    price: float = db.Column(db.Float)
