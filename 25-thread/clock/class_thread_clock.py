import pytz
import datetime
from PySide6.QtCore import QThread, Signal



class ClockThread(QThread):
    signal_show = Signal(dict)
    signal_alarm = Signal(dict)

    def __init__(self):
        super().__init__()
        self._running = True


    def run(self):
        while self._running:
            gmt_time = datetime.datetime.now(pytz.timezone('GMT'))            
            iran_time_zone = pytz.timezone('Asia/Tehran')
            germany_time_zone = pytz.timezone('Europe/Berlin')
            usa_time_zone = pytz.timezone('America/New_York')
            times = {
            "gmt_time" : gmt_time.strftime("%H:%M"),
            "iran_time" : gmt_time.astimezone(iran_time_zone).strftime("%H:%M"), 
            "germany_time" : gmt_time.astimezone(germany_time_zone).strftime("%H:%M"),
            "usa_time" : gmt_time.astimezone(usa_time_zone).strftime("%H:%M"),
            "seconds" : gmt_time.astimezone(iran_time_zone).strftime("%S")
            }
            self.signal_show.emit(times)
            self.sleep(1)
            if times["seconds"] == "00":
                self.signal_alarm.emit(times)



    def stop(self):
        self._running = False
        self.quit()
        self.wait()
