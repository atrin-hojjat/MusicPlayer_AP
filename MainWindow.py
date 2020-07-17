# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainView.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1054, 434)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(600, 330, 441, 32))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.previousButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.previousButton.setObjectName("previousButton")
        self.horizontalLayout.addWidget(self.previousButton)
        self.playButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.playButton.setObjectName("playButton")
        self.horizontalLayout.addWidget(self.playButton)
        self.pauseButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pauseButton.setObjectName("pauseButton")
        self.horizontalLayout.addWidget(self.pauseButton)
        self.nextButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout.addWidget(self.nextButton)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(600, 280, 441, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.timeLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.timeLabel.setObjectName("timeLabel")
        self.horizontalLayout_2.addWidget(self.timeLabel)
        self.timeSlider = QtWidgets.QSlider(self.horizontalLayoutWidget_2)
        self.timeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.timeSlider.setObjectName("timeSlider")
        self.horizontalLayout_2.addWidget(self.timeSlider)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(280, 10, 307, 361))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.clearPlayListButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.clearPlayListButton.setObjectName("clearPlayListButton")
        self.horizontalLayout_5.addWidget(self.clearPlayListButton)
        self.savePlayListButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.savePlayListButton.setObjectName("savePlayListButton")
        self.horizontalLayout_5.addWidget(self.savePlayListButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.currentPlayList = QtWidgets.QListView(self.verticalLayoutWidget_2)
        self.currentPlayList.setObjectName("currentPlayList")
        self.verticalLayout_3.addWidget(self.currentPlayList)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(610, 10, 431, 261))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.musicAlbumLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.musicAlbumLabel.setText("")
        self.musicAlbumLabel.setObjectName("musicAlbumLabel")
        self.gridLayout.addWidget(self.musicAlbumLabel, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.musicArtistLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.musicArtistLabel.setText("")
        self.musicArtistLabel.setObjectName("musicArtistLabel")
        self.gridLayout.addWidget(self.musicArtistLabel, 1, 1, 1, 1)
        self.musicNameLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.musicNameLabel.setText("")
        self.musicNameLabel.setObjectName("musicNameLabel")
        self.gridLayout.addWidget(self.musicNameLabel, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.musicGenerLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.musicGenerLabel.setText("")
        self.musicGenerLabel.setObjectName("musicGenerLabel")
        self.gridLayout.addWidget(self.musicGenerLabel, 3, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 261, 371))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.removePlaylist = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.removePlaylist.setObjectName("removePlaylist")
        self.horizontalLayout_4.addWidget(self.removePlaylist)
        self.insertPlaylist = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.insertPlaylist.setObjectName("insertPlaylist")
        self.horizontalLayout_4.addWidget(self.insertPlaylist)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.songs = QtWidgets.QTableView(self.gridLayoutWidget_2)
        self.songs.setObjectName("songs")
        self.gridLayout_2.addWidget(self.songs, 1, 0, 1, 1)
        self.playlistList = QtWidgets.QListView(self.gridLayoutWidget_2)
        self.playlistList.setObjectName("playlistList")
        self.gridLayout_2.addWidget(self.playlistList, 3, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.removeSong = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.removeSong.setObjectName("removeSong")
        self.horizontalLayout_6.addWidget(self.removeSong)
        self.insertSong = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.insertSong.setObjectName("insertSong")
        self.horizontalLayout_6.addWidget(self.insertSong)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1054, 22))
        self.menubar.setObjectName("menubar")
        self.menuFiles = QtWidgets.QMenu(self.menubar)
        self.menuFiles.setObjectName("menuFiles")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Files = QtWidgets.QAction(MainWindow)
        self.actionOpen_Files.setObjectName("actionOpen_Files")
        self.menuFiles.addAction(self.actionOpen_Files)
        self.menubar.addAction(self.menuFiles.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.previousButton.setText(_translate("MainWindow", "<<"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.pauseButton.setText(_translate("MainWindow", "Pause"))
        self.nextButton.setText(_translate("MainWindow", ">>"))
        self.timeLabel.setText(_translate("MainWindow", "00:00:00/00:00:00"))
        self.clearPlayListButton.setText(_translate("MainWindow", "Clear"))
        self.savePlayListButton.setText(_translate("MainWindow", "Save as playlist"))
        self.label_5.setText(_translate("MainWindow", "Album"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.label_3.setText(_translate("MainWindow", "Artist"))
        self.label_7.setText(_translate("MainWindow", "Gener"))
        self.removePlaylist.setText(_translate("MainWindow", "Remove Playlist"))
        self.insertPlaylist.setText(_translate("MainWindow", ">"))
        self.removeSong.setText(_translate("MainWindow", "Remove Song"))
        self.insertSong.setText(_translate("MainWindow", ">"))
        self.menuFiles.setTitle(_translate("MainWindow", "Files"))
        self.actionOpen_Files.setText(_translate("MainWindow", "Open Files"))
