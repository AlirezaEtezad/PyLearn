import time
from PySide6.QtCore import QThread, Signal, Slot
from class_time import MyTime


class TimerThread(QThread):
    signal_show = Signal(MyTime)

    def __init__(self):
        super().__init__()
        self._running = True
     #   self.time = MyTime(0, 15, 0)



    def run(self):
        while self._running and (self.time.hour > 0 or self.time.minute > 0 or self.time.second > 0):
            self.time.minus()
            self.signal_show.emit(self.time)
            time.sleep(1)



    def reset(self):
        self.time = MyTime(0, 15, 0)
        self.signal_show.emit(self.time)
    

    
    def set_initial_time (self, hour, minute, second):
        self.time = MyTime(hour, minute, second)
     #   self._running = True



    def stop(self):
        self._running = False
        self.quit()
        self.wait()