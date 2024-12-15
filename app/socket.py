from flask_socketio import SocketIO, emit
from .handleMessage import messageHandler

def socketHandler(io):
  @io.on('connected')
  def handle_connect(data):
    emit('sendMessage',data)
  
  @io.on('recieveMessage')
  def handleMessage(data):
    messageHandler(data)