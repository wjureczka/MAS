from MAS.application import db
from MAS.models.Users.User import User


class LandLord(User):
    __tablename__ = 'landlord'
    __mapper_args__ = {
        'polymorphic_identity': 'landlord',
    }

    id: int = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True, nullable=False)
    bank_account_number: str = db.Column(db.String(16), unique=True)