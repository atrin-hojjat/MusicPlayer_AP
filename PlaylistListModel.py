from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

class PlaylistListModel(QAbstractListModel):
    def __init__(self, *arg, **kwargs):
        super(PlayListModel, self).__init__(*args, *kwargs)
        self.playlist = playlist

    def data(self, ind, rl):
        if rl == Qt.DisplayRole:


            # Access Database Here


            return dt.connectionUrl().filename()
    
    def rowCount(self, ind):

        # Access Database Here

        return 0

