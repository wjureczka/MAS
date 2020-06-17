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

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        self._author = new_author
        self.author.add_object_opinion(self);

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        if len(value) < self._max_comment_length:
            self._comment = value
        else:
            raise Exception("Comment too long. Max length of comment is {}".format(self._max_comment_length))

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        if value in self._available_rates:
            self._rate = value
        else:
            raise Exception("No such rate: {}".format(value))
