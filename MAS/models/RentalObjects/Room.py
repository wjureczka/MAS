from MAS.application import db
from MAS.models.RentalObjects.RentalObject import RentalObject


class Room(RentalObject):
    __tablename__ = 'room'
    __mapper_args__ = {
        'polymorphic_identity': 'room',
        'inherit_condition': id == RentalObject.id
    }

    id: int = db.Column(db.Integer, db.ForeignKey('rental_object.id'), primary_key=True, nullable=False)