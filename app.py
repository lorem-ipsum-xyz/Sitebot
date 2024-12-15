from app import myapp
socket, app = myapp()

if __name__ == '__main__':
  socket.run(app, debug=True, host='0.0.0.0')