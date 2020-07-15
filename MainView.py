from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.Multimedia import *
from PyQt5.MultimediaWidgets import *

from PlayListModel import *

from MainWindow import Ui_MainWindow


class MainView(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainView, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.timeLabelText, self.timeTot, self.timePos = "", "", ""


        # Player
        self.player = QMediaPlayer()
        self.player.error.connect(self.erroralert)

        self.pauseButton.pressed.connect(self.player.pause)
        self.playButton.pressed.connect(self.player.play)

        self.timeSlider.valueChanged.connect(self.player.setPosition)
        self.player.durationChanged.connect(self.updateDuration)
        self.player.positionChanged.connect(self.updatePosition)


        # PlayList
        self.playlist = QMediaPlaylist()

        self.player.setMediaPlaylist(self.playlist)

        self.nextButton.pressed.connect(self.playlist.next)
        self.previousButton.pressed.connect(self.playlist.previous)

        self.playlistModel = PlayListModel(self.playlist)
        self.currentPlayList.setModel(self.playlistModel)
        self.playlist.currentIndexChanged.connect(self.playlistModel.playListChange)

        self.currentPlayList.selectionModel().selectionChenged.connect(self.playlistModel.selectionChanged)





        # Library List

        # Playlist list

        # Queue

    def open_files(self): 
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter("Mp3 (*.mp3), WAV (*.wav)")

        files = QStringList()

        if dialog.exec_():
            files = dialog.selectedFiles()

        for f in files:
            print(f)
            self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(f)))

        self.model.layoutChanged.emit()


    def convertTime(self, time):
        s = int(s / 1000)
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



if __name__ == "__main__":
    app = QApplication([])
    app.setApplicationName("Music Player : AP Final Project")
    app.setStyle("Fusion")

    window = MainView()
    app.exec_()
