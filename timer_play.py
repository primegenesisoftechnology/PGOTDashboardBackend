# timer.py

from datetime import datetime
import time

def emit_utc_time(sio):
    while True:
        utc_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
        sio.emit('update', {'time': utc_time})
        time.sleep(0)
