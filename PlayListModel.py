from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

class PlayListModel(QAbstractListModel):
    def __init__(self, playlist, *args, **kwargs):
        super(PlayListModel, self).__init__(*args, *kwargs)
        self.playlist = playlist

    def data(self, ind, rl):
        if rl == Qt.DisplayRole:
            dt = self.playlist.media(ind.row())
            return dt.canonicalUrl().fileName()
    
    def rowCount(self):
        return self.playlist.mediaCount()

