from app.portal.api.util.dto import MessageDto
from .. import socketio
from flask_socketio import emit
from app.portal.service.messageService import get_all_message, save_new_message


def message_received():
    print('message was received!!!')


@socketio.on('connect', namespace='/room')
def handle_event():
    messages = get_all_message()
    for msg in messages:
        msgg = MessageDto(user_id=msg.user_id, message=msg.message, created_on=msg.created_on)
        emit('message', msgg.serialize())


@socketio.on('chat', namespace='/room')
def handle_my_custom_event(json):
    print('recived my event: ' + str(json))
    save_new_message(data=json)
    emit('message', json, broadcast=True)


