from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.Multimedia import *
from PyQt5.MultimediaWidgets import *

from MainWindow import Ui_MainWindow


class MainView(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainView, self).__init__(*args, **kwargs)
        self.setupUi(self)


        # Player

        # Library List

        # Playlist list

        # Queue


if __name__ == "__main__":
    app = QApplication([])
    app.setApplicationName("Music Player : AP Final Project")
    app.setStyle("Fusion")

    window = MainView()
    app.exec_()
