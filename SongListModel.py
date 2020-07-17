from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import database as db

class SongListModel(QAbstractTableModel):
    def __init__(self, *args, **kwargs):
        super(PlayListModel, self).__init__(*args, *kwargs)
        self.playlist = playlist

    def updData(self):
        self.layoutAboutToBeChanged.emit()
        self.data = db.get_songs()
        self.layoutChanged.emit()

    def data(self, ind, rl):
        if rl == Qt.DisplayRole:
            row = ind.row()
            col = ind.column()

            return self.data[row][col + 1]
            
    
    def rowCount(self):
        return len(self.data)
    def columnCount(self):
        return len(self.data[0])

