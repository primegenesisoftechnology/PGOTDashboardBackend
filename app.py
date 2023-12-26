from flask import Flask, render_template
from flask_socketio import SocketIO
import threading
import time
import websocket
import json
import pickle
import numpy as np
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
kline_data_1m=None
kline_data_5m=None
kline_data_15m=None
kline_data_3m=None
model_1m = pickle.load(open('model_1m.pkl', 'rb'))
model_3m = pickle.load(open('model_3m.pkl', 'rb'))
model_5m = pickle.load(open('model_5m.pkl', 'rb'))
model_15m = pickle.load(open('model_15m.pkl', 'rb'))
@socketio.on('connect')
def Live_stream():
    def One_Minute_Function():
        symbol = "btcusdt" 
        interval ="1m"
        def on_message(ws_app, message):
            global kline_data_1m
            data = json.loads(message)
            open_val = float(f"{float(data['k']['o']): .2f}")
            high_val = float(f"{float(data['k']['h']): .2f}")
            low_val = float(f"{float(data['k']['l']): .2f}")
            volume_val = float(f"{float(data['k']['v']): .2f}")
            values = [open_val, high_val, low_val, volume_val]
            arr = [np.array(values)]
            prediction_1m=model_1m.predict(arr)  
            kline_data_1m={"predict": prediction_1m.tolist()}
            ws_app.close()
        def on_error(_, error):
            print(f"WebSocket Error: {error}")
        def on_close(_, close_status_code, close_msg):
            print("WebSocket Closed")
        def on_open(ws_app):
            print('WebSocket opened')
        websocket_url = 'wss://stream.binance.com:9443/ws/' + symbol + '@kline_' + interval
        ws_app = websocket.WebSocketApp(websocket_url, on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close)
        ws_app.run_forever()
        while True:
            socketio.emit('data_1m', {'message': kline_data_1m})
            # time.sleep(1)
    def Third_Minute_Function():
        symbol = "btcusdt" 
        interval ="3m"
        def on_message(ws_app, message):
            global kline_data_3m
            data = json.loads(message)
            open_val = float(f"{float(data['k']['o']): .2f}")
            high_val = float(f"{float(data['k']['h']): .2f}")
            low_val = float(f"{float(data['k']['l']): .2f}")
            volume_val = float(f"{float(data['k']['v']): .2f}")
            values = [open_val, high_val, low_val, volume_val]
            arr = [np.array(values)]
            prediction_3m=model_3m.predict(arr)  
            kline_data_3m={"predict": prediction_3m.tolist()}
            ws_app.close()
        def on_error(_, error):
            print(f"WebSocket Error: {error}")
        def on_close(_, close_status_code, close_msg):
            print("WebSocket Closed")
        def on_open(ws_app):
            print('WebSocket opened')
        websocket_url = 'wss://stream.binance.com:9443/ws/' + symbol + '@kline_' + interval
        ws_app = websocket.WebSocketApp(websocket_url, on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close)
        ws_app.run_forever()
        while True:
            socketio.emit('data_3m', {'message': kline_data_3m})
            # time.sleep(1)        
    def Five_Minute_Function():
        symbol = "btcusdt" 
        interval ="5m"
        def on_message(ws_app, message):
            global kline_data_5m
            data = json.loads(message)
            open_val = float(f"{float(data['k']['o']): .2f}")
            high_val = float(f"{float(data['k']['h']): .2f}")
            low_val = float(f"{float(data['k']['l']): .2f}")
            volume_val = float(f"{float(data['k']['v']): .2f}")
            values = [open_val, high_val, low_val, volume_val]
            arr = [np.array(values)]
            # prediction_1m = model_1m.predict(arr[0])
            # prediction_5m=model_5m.predict(arr[1])
            prediction_5m=model_5m.predict(arr)  
            kline_data_5m={"predict": prediction_5m.tolist()}
            ws_app.close()
        def on_error(_, error):
            print(f"WebSocket Error: {error}")
        def on_close(_, close_status_code, close_msg):
            print("WebSocket Closed")
        def on_open(ws_app):
            print('WebSocket opened')
        websocket_url = 'wss://stream.binance.com:9443/ws/' + symbol + '@kline_' + interval
        ws_app = websocket.WebSocketApp(websocket_url, on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close)
        ws_app.run_forever()
        while True:
            socketio.emit('data_5m', {'message': kline_data_5m})
            # time.sleep(1)
    def Fifteen_Minute_Function():
        symbol = "btcusdt" 
        interval ="15m"
        def on_message(ws_app, message):
            global kline_data_15m
            data = json.loads(message)
            open_val = float(f"{float(data['k']['o']): .2f}")
            high_val = float(f"{float(data['k']['h']): .2f}")
            low_val = float(f"{float(data['k']['l']): .2f}")
            volume_val = float(f"{float(data['k']['v']): .2f}")
            values = [open_val, high_val, low_val, volume_val]
            arr = [np.array(values)]
            prediction_15m=model_15m.predict(arr)  
            kline_data_15m={"predict": prediction_15m.tolist()}
            ws_app.close()
        def on_error(_, error):
            print(f"WebSocket Error: {error}")
        def on_close(_, close_status_code, close_msg):
            print("WebSocket Closed")
        def on_open(ws_app):
            print('WebSocket opened')
        websocket_url = 'wss://stream.binance.com:9443/ws/' + symbol + '@kline_' + interval
        ws_app = websocket.WebSocketApp(websocket_url, on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close)
        ws_app.run_forever()
        while True:
            socketio.emit('data_15m', {'message': kline_data_15m})
            # time.sleep(1)                
    One_Minute_Thread = threading.Thread(target=One_Minute_Function)
    Third_Minute_Thread = threading.Thread(target=Third_Minute_Function)
    Five_Minute_Thread = threading.Thread(target=Five_Minute_Function)
    Fifteen_Minute_Thread = threading.Thread(target=Fifteen_Minute_Function)
    
    One_Minute_Thread.start()
    Third_Minute_Thread.start()
    Five_Minute_Thread.start()
    Fifteen_Minute_Thread.start()
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    socketio.run(app, debug=True)
