from .. import db


class Course(db.Model):
    """ Course Model for storing course related details """
    __tablename__ = "course"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), unique=True)
    unit = db.Column(db.Integer)

    def __init__(self, name, unit):
        self.name = name
        self.unit = unit

    def __repr__(self):
        return "<Course '{}'>".format(self.name)
