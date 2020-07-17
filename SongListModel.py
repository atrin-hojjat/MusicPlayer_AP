from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import database as db

class SongListModel(QAbstractTableModel):
    def __init__(self, *args, **kwargs):
        super(PlayListModel, self).__init__(*args, *kwargs)
        self._data = db.get_songs()

    def updData(self):
        self.layoutAboutToBeChanged.emit()
        self._data = db.get_songs()
        self.layoutChanged.emit()

    def getId(self, ind):
        return self._data[ind.row()][0]
    def data(self, ind, rl):
        if rl == Qt.DisplayRole:
            row = ind.row()
            col = ind.column()

            return self._data[row][col + 1]

    header_labels = ["Song", "Artist", "Year",
    "Album", "Address", "Genre"]

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.header_labels[section]
    return QAbstractTableModel.headerData(self, section, orientation, role)
            
    
    def rowCount(self):
        return len(self._data)
    def columnCount(self):
        return len(self._data[0])

