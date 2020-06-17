from MAS.application import db
from MAS.models.Agreements.RentalAgreement import RentalAgreement


class CommonAgreement(RentalAgreement):
    __tablename__ = 'common_agreement'
    __mapper_args__ = {
        'polymorphic_identity': 'common_agreement'
    }

    id = db.Column(db.Integer, db.ForeignKey('rental_agreement.id'), primary_key=True, nullable=False)
