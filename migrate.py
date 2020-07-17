
import sqlite3

connection = sqlite3.connect('musics.db')

first = connection.cursor() 

first.execute("""CREATE TABLE music (
        song_name text , 
        artist text , 
        publish_year integer , 
        album text , 
        address text , 
        gener text , 
        id integer primary key autoincrement
        )""")

first.execute("""CREATE TABLE playlist ( 
        playlist_name text ,
        id integer primary key autoincrement  
        )""") 

first.execute("""CREATE TABLE playlist_song (
        track_number integer ,
        track_id integer , 
        playlist_id integer
    )""")


