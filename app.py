from app import myapp
import os
socket, app = myapp()

if __name__ == '__main__':
  PORT = os.getenv('PORT', 5000)
  socket.run(app, host='0.0.0.0', port=PORT, debug=True)