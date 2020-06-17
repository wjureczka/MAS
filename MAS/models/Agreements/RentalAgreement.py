from MAS.application import db


class RentalAgreement(db.Model):
    __tablename__ = 'rental_agreement'
    __mapper_args = {
        'polymorphic_identity': 'rental_agreement',
        'polymorphic_on': type
    }

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    start_date = db.Column(db.DATE)
    end_date = db.Column(db.DATE)
    rules_of_use = db.Column(db.String(300))

    rental_object = db.relationship('RentalObject')
