
import sqlite3

connection = sqlite3.connect('musics.db')

first = connection.cursor() 

first.execute("""CREATE TABLE music (
        id integer primary key autoincrement,
        song_name text , 
        artist text , 
        publish_year integer , 
        album text , 
        address text , 
        gener text
        )""")

first.execute("""CREATE TABLE playlist ( 
        id integer primary key autoincrement  ,
        playlist_name text
        )""") 

first.execute("""CREATE TABLE playlist_song (
        track_number integer ,
        track_id integer , 
        playlist_id integer
    )""")


