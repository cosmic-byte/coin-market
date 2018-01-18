from .. import db


class Message(db.Model):
    """
    Message Model for storing messages
    """
    __tablename__ = 'message'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_on = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<id: message: {}'.format(self.message)

