from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from tinytag import TinyTag
import sys

from PlayListModel import *
from SongListModel import *
from PlaylistListModel import *

import database as db

from MainWindow import Ui_MainWindow


class MainView(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainView, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.timeLabelText, self.timeTot, self.timePos = "", "", ""


        # Player
        self.player = QMediaPlayer()
#        self.player.error.connect(self.erroralert)

        self.pauseButton.pressed.connect(self.player.pause)
        self.playButton.pressed.connect(self.player.play)

        self.timeSlider.valueChanged.connect(self.player.setPosition)
        self.player.durationChanged.connect(self.updateDuration)
        self.player.positionChanged.connect(self.updatePosition)


        # PlayList
        self.playlist = QMediaPlaylist(self.player)


        self.playlist.addMedia(QMediaContent(QUrl(
            "file:/Volumes/Atrin/Musics/My Musics/Bliss/No one built this moment/11 The Hope.wav")))


        self.player.setPlaylist(self.playlist)

        self.nextButton.pressed.connect(self.playlist.next)
        self.previousButton.pressed.connect(self.playlist.previous)

        self.playlistModel = PlayListModel(self.playlist)
        self.currentPlayList.setModel(self.playlistModel)
        self.playlist.currentIndexChanged.connect(self.playListChange)

        playlist_sel_mod = self.currentPlayList.selectionModel()
        playlist_sel_mod.selectionChanged.connect(self.selectionChanged)


        self.player.mediaStatusChanged.connect(self.updateMetaData)
        self.player.mediaStatusChanged.connect(lambda: print("TEST"))



        # Library List

        self.songListModel = SongListModel()
        self.songList.setModel(self.songListModel)
        self.songList.set
        

        # Playlist list

        # Queue



        self.actionOpen_Files.triggered.connect(self.open_files)
        self.setAcceptDrops(True)

        self.show()

    def addFileToDatabase(self, address):
       if len(db.get_song_by_address(address)) == 0:
           metadata = TinyTag.get(address)

           db.insert_song(metadata.title,
                   metadata.artist , metadata.year,
                   metadata.album, address,
                   metadata.genre)

    def addSongToPlaylist(self, playlist):
        self.p

    def open_files(self): 
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setNameFilters(["Mp3 (*.mp3)", "WAV (*.wav)"])

        files = []

        if dialog.exec_():
            files = dialog.selectedFiles()

        for f in files:
            print(f)

            self.addFileToDatabase(f)


            self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(f)))

        self.playlistModel.layoutChanged.emit()


    def updateMetaData(self, status): 
        print(status)
        print(QMediaPlayer.LoadedMedia)
        print("Status Update")
        if status == QMediaPlayer.LoadedMedia or status == QMediaPlayer.LoadingMedia:
            self.musicNameLabel.setText(self.player.metaData("Title"))

            artist = self.player.metaData("Author")
            if artist == "": artist = self.player.metaDatat("Artist")
            if artist == "": artist = self.player.metaDatat("Composer")
            if artist == "": artist = self.player.metaDatat("AlbumArtist")

            self.musicArtistLabel.setText(artist)

            self.musicAlbumLabel.setText(self.player.metaData("Album"))
            self.musicGenerLabel.setText(self.player.metaData("Gener"))
        else:
            print("Media not loaded")

    def convertTime(self, time):
        if not time: time = 0
        s = int(time / 1000)
        m, s = divmod(s, 60)
        h, m = divmod(m, 60)
        return "{}:{}:{}".format(h, m, s)

    def updateDuration(self, duration):
        self.timeSlider.setMaximum(duration)

        self.timeTot = self.convertTime(duration)
        self.timeLabelText = "{} / {}".format(self.timePos, self.timeTot)
        self.timeLabel.setText(self.timeLabelText)

        self.timeSlider.blockSignals(True)
        self.timeSlider.setValue(timeLabelText)
        self.timeSlider.blockSignals(False)

    def updatePosition(self, position):
        self.timePos = self.convertTime(position)
        self.timeLabelText = "{} / {}".format(self.timePos, self.timeTot)
        self.timeLabel.setText(self.timeLabelText)

        self.timeSlider.blockSignals(True)
        self.timeSlider.setValue(position)
        self.timeSlider.blockSignals(False)

    def selectionChanged(self, ind):
        i = ind.indexes()[0].row()
        self.playlist.setCurrentIndex(i)

    def playListChange(self, ind):
        if ind > -1:
            i = self.playlistModel.index(ind)
            self.currentPlayList.setCurrentIndex(i)
    







if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Music Player : AP Final Project")

    window = MainView()
    app.exec_()
