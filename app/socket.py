from .handleMessage import messageHandler
from flask_socketio import SocketIO, join_room

def socketHandler(io):
  @io.on('join')
  def Join(data):
    join_room(data['room'])
    io.emit('sendMessage',{"data":data['data'],"id":data['id']}, to=data['room'])
  
  @io.on('recieveMessage')
  def handleMessage(data):
    text = data["text"]
    room = data["room"]
    messageHandler(text, room)