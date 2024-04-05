import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from ui_main_window import Ui_MainWindow
from database import Database


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.db = Database()
        self.read_database()

        self.ui.btn_newtask.clicked.connect(self.new_task)

    def new_task(self):
        new_title = self.ui.txtbox_newtask_title.text()
        new_desc = self.ui.txtbox_newtask_desc.toPlainText()
        new_time = self.ui.date_newtask.dateTime()
        time_str = new_time.toString(Qt.ISODate)
        new_priority = self.ui.priorities_box.currentText()
        feedback = self.db.add_new_task(new_title, new_desc, time_str, new_priority)
        if feedback == True:
            self.read_database()
            self.ui.txtbox_newtask_desc.setText("")
            self.ui.txtbox_newtask_title.setText("")
        else:
            msg_box = QMessageBox()
            msg_box.setText("There is a problem writing in database")
            msg_box.exec()

    def delete_task(self, index):
        task_id = self.db.get_tasks()[index][0]
        if self.db.remove_task(task_id):
            self.read_database()
        else:
            QMessageBox.warning(self, "Error", "Failed to delete task.")

    def add_done(self, index):
        task_id = self.db.get_tasks()[index][0]
        if self.db.task_done(task_id):
            self.read_database()
        else:
            QMessageBox.warning(self, "Error", "Failed to add to done tasks.")



    # def show_task_details(self, task_id,tasks):
    #     description = tasks[task_id][0]
    #     time = tasks[task_id][1]
    #     QMessageBox.information(self, "Task Details", f"Description: {description}\nTime: {time}")


    def read_database(self):
        while self.ui.grid_tasks.count():
            item = self.ui.grid_tasks.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()        
        
        tasks = self.db.get_tasks()
       # print(tasks)
        for i in range(len(tasks)):
            checkbx = QCheckBox()
            new_label = QLabel()
            new_time = QLabel()
            new_label.setText(tasks[i][1])
            new_time.setText(tasks[i][3]) 

            new_btn = QPushButton()
            new_btn.setText("X")
            new_btn.clicked.connect(lambda dummy=None, idx=i: self.delete_task(idx))
            checkbx.clicked.connect(lambda dummy=None, idx=i: self.add_done(idx))

            # new_label.mousePressEvent = lambda event, idx=i: self.show_task_details(tasks[idx][0])



            new_desc = QLabel()
            new_desc.setText(tasks[i][2])
            priority = tasks[i][4]
            if priority == "High":
                new_label.setStyleSheet("background-color: red;")
            elif priority == "Medium":
                new_label.setStyleSheet("background-color: yellow;")
            elif priority == "Low":
                new_label.setStyleSheet("background-color: green;")

            self.ui.grid_tasks.addWidget(checkbx, i, 0)
            self.ui.grid_tasks.addWidget(new_label, i, 1)
            self.ui.grid_tasks.addWidget(new_desc, i, 2)
            self.ui.grid_tasks.addWidget(new_btn, i , 4)
            self.ui.grid_tasks.addWidget(new_time, i , 3)


        while self.ui.grid_tasks_done.count():
            item = self.ui.grid_tasks_done.takeAt(0)
            widget_done = item.widget()
            if widget_done:
                widget_done.deleteLater()        
        
        tasks_done = self.db.get_tasks_done()
        for j in range(len(tasks_done)):
            label = QLabel()
            desc = QLabel()
            time = QLabel()
            label.setText(tasks_done[j][1])
            desc.setText(tasks_done[j][2])
            time.setText(tasks_done[j][3]) 

            self.ui.grid_tasks_done.addWidget(label, j, 0)
            self.ui.grid_tasks_done.addWidget(desc, j, 1)
            self.ui.grid_tasks_done.addWidget(time, j, 2)

        



if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec()
    