from MAS.application import db
from MAS.models.Agreements.RentalAgreement import RentalAgreement


class OccasionalAgreement(RentalAgreement):
    __tablename__ = 'occasional_agreement'
    __mapper_args__ = {
        'polymorphic_identity': 'occasional_agreement'
    }

    id = db.Column(db.Integer, db.ForeignKey('rental_agreement.id'), primary_key=True, nullable=False)
    notary_confirmation = db.Column(db.String(100))
