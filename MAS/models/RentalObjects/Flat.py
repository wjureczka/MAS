from MAS.application import db
from MAS.models.RentalObjects.RentalObject import RentalObject


class Flat(RentalObject):
    __tablename__ = 'flat'
    __mapper_args__ = {
        'polymorphic_identity': 'flat',
        'inherit_condition': id == RentalObject.id
    }

    id: int = db.Column(db.Integer, db.ForeignKey('rental_object.id'), primary_key=True, nullable=False)
    rooms = db.relationship('Room')
