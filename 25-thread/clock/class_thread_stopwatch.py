from class_time import MyTime
import time
from PySide6.QtCore import QThread, Signal



class StopWatchThread(QThread):
    signal_show = Signal(MyTime)
    def __init__(self):
        super().__init__()
        self.time = MyTime(0, 0, 0)
        self._running = True

    def run(self):
        while self._running:
            self.time.plus()
            self.signal_show.emit(self.time)
            time.sleep(1)

    def reset(self):
        self.time.hour = 0
        self.time.minute = 0
        self.time.second = 0


    def stop(self):
        self._running = False
        self.quit()
        self.wait()