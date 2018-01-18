from sqlalchemy import desc
import datetime

from app.portal import db

from app.portal.models.message import Message
from app.portal.models.user import User


def save_new_message(data):
    new_user = User.query.filter_by(id=1).first()
    new_message = Message(
        message=data['message'],
        created_on=datetime.datetime.utcnow(),
        user=new_user
    )
    save_changes(new_message)
    response_object = {
        'status': 'success',
        'message': 'message saved.'
    }
    return response_object, 201


def get_all_message():
    return Message.query.all()


def save_changes(data):
    db.session.add(data)
    db.session.commit()

