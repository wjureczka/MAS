from MAS.models.ObjectPlus import ObjectPlus


class Opinion(ObjectPlus):
    _max_comment_length = 200
    _comment = None
    _rate = None
    _available_rates = ("0", "1", "2", "3", "4", "5")

    def __init__(self, comment, rate):
        super().__init__()
        self.comment = comment
        self.rate = rate

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
