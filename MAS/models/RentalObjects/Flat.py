from MAS.application import db
from MAS.models.RentalObjects.RentalObject import RentalObject


class Flat(RentalObject):
    __tablename__ = 'flat'
    __mapper_args__ = {
        'polymorphic_identity': 'rental_object'
    }

    id: int = db.Column(db.Integer, db.ForeignKey('rental_object.id'), primary_key=True, nullable=False)
    rooms: list = db.relationship('Room', back_populates='flat')
