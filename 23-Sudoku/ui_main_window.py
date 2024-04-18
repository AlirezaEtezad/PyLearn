# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(744, 659)
        self.menu_new = QAction(MainWindow)
        self.menu_new.setObjectName(u"menu_new")
        self.menu_openfile = QAction(MainWindow)
        self.menu_openfile.setObjectName(u"menu_openfile")
        self.menu_solve = QAction(MainWindow)
        self.menu_solve.setObjectName(u"menu_solve")
        self.menu_help = QAction(MainWindow)
        self.menu_help.setObjectName(u"menu_help")
        self.menu_exit = QAction(MainWindow)
        self.menu_exit.setObjectName(u"menu_exit")
        self.light_mode = QAction(MainWindow)
        self.light_mode.setObjectName(u"light_mode")
        self.dark_mode = QAction(MainWindow)
        self.dark_mode.setObjectName(u"dark_mode")
        self.difficulty_easy = QAction(MainWindow)
        self.difficulty_easy.setObjectName(u"difficulty_easy")
        self.difficulty_normal = QAction(MainWindow)
        self.difficulty_normal.setObjectName(u"difficulty_normal")
        self.difficulty_hard = QAction(MainWindow)
        self.difficulty_hard.setObjectName(u"difficulty_hard")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 10, 741, 591))
        self.grid_layout = QGridLayout(self.gridLayoutWidget)
        self.grid_layout.setObjectName(u"grid_layout")
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 744, 22))
        self.menuGame = QMenu(self.menubar)
        self.menuGame.setObjectName(u"menuGame")
        self.menumode = QMenu(self.menubar)
        self.menumode.setObjectName(u"menumode")
        self.menuDiffculty = QMenu(self.menubar)
        self.menuDiffculty.setObjectName(u"menuDiffculty")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuGame.menuAction())
        self.menubar.addAction(self.menumode.menuAction())
        self.menubar.addAction(self.menuDiffculty.menuAction())
        self.menuGame.addAction(self.menu_new)
        self.menuGame.addAction(self.menu_openfile)
        self.menuGame.addAction(self.menu_solve)
        self.menuGame.addAction(self.menu_help)
        self.menuGame.addAction(self.menu_exit)
        self.menumode.addAction(self.light_mode)
        self.menumode.addAction(self.dark_mode)
        self.menuDiffculty.addAction(self.difficulty_easy)
        self.menuDiffculty.addAction(self.difficulty_normal)
        self.menuDiffculty.addAction(self.difficulty_hard)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sudoku Game", None))
        self.menu_new.setText(QCoreApplication.translate("MainWindow", u"New Game", None))
        self.menu_openfile.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.menu_solve.setText(QCoreApplication.translate("MainWindow", u"Solve", None))
        self.menu_help.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menu_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.light_mode.setText(QCoreApplication.translate("MainWindow", u"light_mode", None))
        self.dark_mode.setText(QCoreApplication.translate("MainWindow", u"dark_mode", None))
        self.difficulty_easy.setText(QCoreApplication.translate("MainWindow", u"Easy", None))
        self.difficulty_normal.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.difficulty_hard.setText(QCoreApplication.translate("MainWindow", u"Hard", None))
        self.menuGame.setTitle(QCoreApplication.translate("MainWindow", u"Game", None))
        self.menumode.setTitle(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.menuDiffculty.setTitle(QCoreApplication.translate("MainWindow", u"Difficulty", None))
    # retranslateUi

