from .. import socketio
from flask_socketio import emit


messages = [{'user': 'Greg', 'msg': 'hello world kedu'},
            {'user': 'Austine', 'msg': 'hello world keekwanu'}]


def message_received():
    print('message was received!!!')


@socketio.on('connect', namespace='/room')
def handle_event():
    print('Hello New user')
    for msg in messages:
        emit('message', msg)


@socketio.on('chat', namespace='/room')
def handle_my_custom_event(json):
    print('recived my event: ' + str(json))
    socketio.emit('message', json, callback=message_received)
