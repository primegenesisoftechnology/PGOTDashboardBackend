from flask import Flask, render_template
from flask_socketio import SocketIO
import threading
import time

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('connect')
def start_hello_world_stream():
    def emit_hello_world():
        count = 0
        while True:
            socketio.emit('hello_world', {'message': f'Hello, World! {count}'})
            count += 1
            # time.sleep(1)  

    hello_thread = threading.Thread(target=emit_hello_world)
    hello_thread.start()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    socketio.run(app, debug=True)
