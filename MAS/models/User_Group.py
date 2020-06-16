from MAS.application import db

User_Group = db.Table(
    'user_group',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('tenant_id', db.Integer, db.ForeignKey('tenant.id'), nullable=False),
    db.Column('group_id', db.Integer, db.ForeignKey('group.id'), nullable=False)
)
