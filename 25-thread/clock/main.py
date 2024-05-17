import sys
#import time
#from PySide6.QtCore import QObject
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
#from PySide6.QtCore import QThread, Signal, Slot
#from PySide6.QtUiTools import QUiLoader
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
#from PySide6.QtWidgets import QMessageBox, QPushButton


from class_thread_timer import TimerThread
from class_thread_stopwatch import StopWatchThread
from class_thread_clock import ClockThread
from class_time import MyTime
from class_database import Database


from ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.thread_stopwatch = StopWatchThread()
        self.thread_timer = TimerThread()
      #  self.time = MyTime(0, 0, 0)
        self.thread_clock = ClockThread()


        self.db = Database()
        self.read_database()

        self.ui.alarm_btn_add.clicked.connect(self.new_alarm)

        self.ui.label_stopwatch.setText("0:0:0")
        self.ui.stopwatch_start_btn.clicked.connect(self.stopwatch_start)
        self.ui.stopwatch_stop_btn.clicked.connect(self.stopwatch_stop)
        self.ui.stopwatch_reset_btn.clicked.connect(self.stopwatch_reset)

        self.ui.timer_start_btn.clicked.connect(self.timer_start)
        self.ui.timer_stop_btn.clicked.connect(self.timer_stop)
        self.ui.timer_reset_btn.clicked.connect(self.timer_reset)

        self.thread_stopwatch.signal_show.connect(self.stopwatch_show_time)
        self.thread_timer.signal_show.connect(self.timer_show_time)
        self.thread_clock.signal_show.connect(self.clock_show_time)
        self.thread_clock.signal_alarm.connect(self.check_alarms)
        self.thread_clock.start()

        self.alarm_sound = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.alarm_sound.setAudioOutput(self.audio_output)
        self.alarm_sound.setSource(QUrl.fromLocalFile("SunIsUp-Inna.mp3"))
        self.audio_output.setVolume(0.5)  # Set volume (0.0 to 1.0)

# stop_watch:
    def stopwatch_stop(self):
        self.thread_stopwatch.terminate()

    def stopwatch_start(self):
        self.thread_stopwatch.start()

    def stopwatch_reset(self):
        self.stopwatch_stop()
        self.thread_stopwatch.reset()
        time = MyTime(0, 0 ,0)
        self.stopwatch_show_time(time)

    def stopwatch_show_time(self, time):
        window.ui.label_stopwatch.setText(f"{time.hour}:{time.minute}:{time.second}")


    # timer:
    def timer_start(self):
        self.timer_set_from_input()
        self.thread_timer.start()

    def timer_show_time(self, time):
        window.ui.timer_hour_txtbox.setText(str(time.hour))
        window.ui.timer_minute_txtbox.setText(str(time.minute))
        window.ui.timer_second_txtbox.setText(str(time.second))


    def timer_set_from_input(self):
        hour = int(self.ui.timer_hour_txtbox.text())
        minute = int(self.ui.timer_minute_txtbox.text())
        second = int(self.ui.timer_second_txtbox.text())
        self.thread_timer.set_initial_time(hour, minute, second)

    
    def timer_stop(self):
         self.thread_timer.terminate()
        
    def timer_reset(self):
        self.timer_stop()
        self.thread_timer.reset()

    # clock:
    def clock_show_time(self, times):
        self.ui.clock_label_gmt_time.setText(times['gmt_time'])
        self.ui.clock_label_iran_time.setText(times['iran_time'])        
        self.ui.clock_label_germany_time.setText(times['germany_time'])
        self.ui.clock_label_usa_time.setText(times['usa_time'])
        self.ui.clock_label_seconds.setText(times['seconds'])



    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        
        if reply == QMessageBox.Yes:
            self.thread_clock.stop() 
            self.thread_stopwatch.stop()
            self.thread_timer.stop()
            event.accept()  # Accept the event to proceed with closing
        else:
            event.ignore()  # Ignore the event to prevent closing



    # alarm:

    def new_alarm(self):
            new_title = self.ui.alarm_txtbox.text()
            
            new_time = self.ui.alarm_time_edit.time()
            time_str = new_time.toString("HH:mm")
           
            feedback = self.db.add_new_alarm(new_title, time_str)
            if feedback == True:
                self.read_database()
                self.ui.alarm_txtbox.setText("")
            else:
                msg_box = QMessageBox()
                msg_box.setText("There is a problem writing in database")
                msg_box.exec()



    def delete_alarm(self, index):
        alarm_id = self.db.get_alarms()[index][0]
        if self.db.remove_alarm(alarm_id):
            self.read_database()
        else:
            QMessageBox.warning(self, "Error", "Failed to delete alarm.")



    def read_database(self):
        while self.ui.alarm_grid.count():
            item = self.ui.alarm_grid.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()        
        
        alarms = self.db.get_alarms()
       # print(alarms)
        for i in range(len(alarms)):
            new_label = QLabel()
            new_time = QLabel()
            new_label.setText(alarms[i][1])
            new_time.setText(alarms[i][2]) 

            new_btn = QPushButton()
            new_btn.setText("X")
            new_btn.clicked.connect(lambda dummy=None, idx=i: self.delete_alarm(idx))

            self.ui.alarm_grid.addWidget(new_label, i, 0)
            self.ui.alarm_grid.addWidget(new_btn, i , 2)
            self.ui.alarm_grid.addWidget(new_time, i , 1)


    def check_alarms(self, times):
        current_time = times["iran_time"]
       # print(current_time)
        alarms = self.db.get_alarms()
        for alarm in alarms:
            if alarm[2] == current_time:
                self.alarm_sound.play()  # Play the alarm sound
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Alarm")
                msg_box.setText(f"Alarm: {alarm[1]}")
                dismiss_button = msg_box.addButton("Dismiss", QMessageBox.AcceptRole)
                dismiss_button.clicked.connect(self.stop_alarm_sound)
                msg_box.exec()
                break


    def stop_alarm_sound(self):
        self.alarm_sound.stop()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())







# 

# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     window = MainWindow()
#     window.show()

#     thread_stopwatch = StopWatchThread()
#     thread_timer = TimerThread()
#     thread_clock = MyTime()


#     window.ui.label_stopwatch.setText("0:0:0")
#     window.ui.stopwatch_start_btn.clicked.connect(window.start_stopwatch)
#     window.ui.stopwatch_stop_btn.clicked.connect(window.stop_stopwatch)
#     window.ui.stopwatch_reset_btn.clicked.connect(window.reset_stopwatch)
    
#     window.ui.timer_start_btn.clicked.connect(window.start_timer)
#     window.ui.timer_stop_btn.clicked.connect(window.timer_stop)
#     window.ui.timer_reset_btn.clicked.connect(window.timer_reset)

#     thread_stopwatch.signal_show.connect(window.show_time_stopwatch)
#     thread_timer.signal_show.connect(window.show_time_timer)


#     app.exec_()









    # if __name__ == "__main__":
#     app = QApplication(sys.argv)


#     loader = QUiLoader()
#     window = loader.load("main_window.ui")
#     window.show()


#     thread_stopwatch = StopWatchThread()
#     thread_timer = TimerThread()
#     window.label_stopwatch.setText("0:0:0")
#     window.btn_start_stopwatch.clicked.connect(start_stopwatch)
#     window.btn_stop_stopwatch.clicked.connect(stop_stopwatch)
#     window.btn_reset_stopwatch.clicked.connect(reset_stopwatch)
#     window.btn_start_timer.clicked.connect(start_timer)
#     thread_stopwatch.signal_show.connect(show_time_stopwatch)
#     thread_timer.signal_show.connect(show_time_timer)

#     app.exec()