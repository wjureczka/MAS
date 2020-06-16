from MAS.application import db
from MAS.models.Users.User import User
from MAS.models.User_Group import User_Group


class Tenant(User):
    __tablename__ = 'tenant'
    __mapper_args__ = {
        'polymorphic_identity': 'tenant'
    }

    id: int = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True, nullable=False)
    groups: list = db.relationship('Group', secondary=User_Group, backref='Tenant')
