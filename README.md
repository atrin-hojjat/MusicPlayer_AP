# MusicPlayer_AP
Python music player/ AP final project #1

## Requirements
PyQt5, sqlite, sip, TinyTag
You have to run migrate.py before you run the program 

## Descritpion

This is a simple music player using qt QMediaPlayer and QMediaPlaylist modules for queueing and playing the songs. The database module is responsible for saving song info for imported songs and saving songs for different playlists. 

## Gui
GUI uses pyqt library. it uses a QTableView for song information with a sort proxy model with lets you sort the songs based on Artist/Year/Album/Name.The playlist and queue views use QListView with QAbstractListModel for handling data updates. You can import songs using the file menu. the imported songs will automaticly be added to database and current queue. You can change song positions on the current queue using `^` and 'v' buttons. You can also use `>` button to import songs/playlists from the songs/playlist lists. You can also clear the current queue or save it as a playlist.


![Main Window](/images/MainWindow.png)


## Database
Database module uses sqlite with three tables:
* music: the table saves metadata and address for previously imported music
* playlists: the table saves ids and names for created playlists
* playlist_song: this table is a turntable for saving songs in each playlist

![Database Scheme](/images/Database.png)


[Diagram](https://dbdiagram.io/d/5f11922c74ca2227330d7b25)


## Bugs
QMediaPlayer doesn't load media properly on PyQt5.18, if thats the case downgrade PyQt to 5.8.
QMediaPlayer uses gstreamer libraries on ubuntu and perhaps other linux based systems(only tested on ubuntu)
