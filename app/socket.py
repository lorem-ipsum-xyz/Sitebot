from .handleMessage import messageHandler
from flask_socketio import SocketIO, join_room

def socketHandler(io):
  @io.on('join')
  def Join(data):
    join_room(data)
    io.emit('sendMessage',{"data":""}, to=data)
  
  @io.on('recieveMessage')
  def handleMessage(data):
    room = data["room"]
    message = {
      "text": data['text'],
      "id": data['id']
    }
    messageHandler(message, room)