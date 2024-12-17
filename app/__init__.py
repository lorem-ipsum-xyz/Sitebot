from flask import Flask
from flask_socketio import SocketIO
import os
import config

def myapp():
  from .socket import socketHandler
  from .loadCommands import register
  from .views import view
  from .cmdRoutes import cmd
  
  app = Flask(__name__,
    template_folder=os.path.abspath('frontend'),
    static_folder=os.path.abspath('frontend/static'),
  )
  app.secret_key = ":(){:|:&};"
  socket = SocketIO(app)
  config.io = socket
  
  register()
  socketHandler(socket)
  
  app.register_blueprint(view)
  app.register_blueprint(cmd)
  
  return [socket, app]