from MAS.application import db
from MAS.models.RentalObjects.RentalObject import RentalObject


class Room(RentalObject):
    __tablename__ = 'room'
    __mapper_args__ = {
        'polymorphic_identity': 'rental_object'
    }

    id: int = db.Column(db.Integer, db.ForeignKey('rental_object.id'), primary_key=True, nullable=False)
    flat = db.relationship("Flat", back_populates='rooms')
    flat_id = db.Column(db.Integer, db.ForeignKey('flat.id'), nullable=True)

