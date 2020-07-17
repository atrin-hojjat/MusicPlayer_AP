from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import database as db

class PlaylistListModel(QAbstractListModel):
    def __init__(self, *arg, **kwargs):
        super(PlayListModel, self).__init__(*args, *kwargs)
        self.playlist = playlist
        self.data = []

    def updData(self):
        self.layoutAboutToBeChanged.emit()
        self.data = db.get_playlists()
        self.layoutChanged.emit()


    def data(self, ind, rl):
        if rl == Qt.DisplayRole:


            # Access Database Here

            return self.data[ind.row()][1]

    
    def rowCount(self):

        return len(self.data)


