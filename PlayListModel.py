from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.Multimedia import *
from PyQt5.MultimediaWidgets import *

class PlayListModel(QAbstractListModel):
    def __init__(self, playlist, *arg, **kwargs):
        super(PlayListModel, self).__init__(*args, *kwargs)
        self.playlist = playlist

    def data(self, ind, rl):
        if rl == Qt.DisplayRole:
            dt = self.playlist.media(ind.row)
            return dt.connectionUrl().filename()
    
    def rowCount(self, ind):
        return self.playlist.mediaCount()

    def selectionChanged(self, ind):
        i = ind.indexes()[0].row()
        self.playlist.setCurrentIndex(i)

    def playListChange(self, ind):
        if ind > -1:
            i = self.model.index(ind)
            self.currendPlayList.setCurrentIndex(i)
    

