from MAS.application import db


class Opinion(db.Model):
    __tablename__ = 'opinion'

    _available_rates = ("0", "1", "2", "3", "4", "5")

    comment: str = db.Column(db.String(200))
    rate: float = db.Column(db.Float)
    author_id = db.Column(db.Integer, db.ForeignKey('tenant.id'), primary_key=True, nullable=False)
    author = db.relationship("Tenant", back_populates='opinions')
    rental_object = db.relationship("RentalObject", back_populates='opinions')
    rental_object_id = db.Column(db.Integer, db.ForeignKey('rental_object.id'), primary_key=True, nullable=False)
