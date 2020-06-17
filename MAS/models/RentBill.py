from MAS.application import db


class RentBill(db.Model):
    __tablename__ = 'rent_bill'

    date_of_payment = db.Column(db.DATE)
    due_date = db.Column(db.DATE, nullable=False)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenant.id'), primary_key=True, nullable=False)
    tenant = db.relationship("Tenant", back_populates='bills')
    rental_agreement = db.relationship("RentalObject", back_populates='bills')
    rental_agreement_id = db.Column(db.Integer, db.ForeignKey('rental_object.id'), primary_key=True, nullable=False)
