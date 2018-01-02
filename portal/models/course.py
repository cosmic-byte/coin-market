from .. import db


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    unit = db.Column(db.Integer)

    def __repr__(self):
        return "<Course '{}'>".format(self.name)
