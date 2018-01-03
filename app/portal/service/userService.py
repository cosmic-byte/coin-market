import uuid

from app.portal import db

from app.portal.models.user import User


def save_new_user(data):
    new_user = User(
        public_id=str(uuid.uuid4()),
        email=data['email'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        username=data['username'],
        password=data['password']
    )
    save_changes(new_user)
    return new_user


def get_all_users():
    return User.query.all()


def get_student(public_id):
    return User.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
