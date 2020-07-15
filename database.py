
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
        )""")

first.execute("""CREATE TABLE playlist ( 
        playlist_name text ,
        list_name text 
        )""") 

#first.execute("""CREATE TABLE 

def insert_song(song_name , artist , publish_year , album , address , gener) :

    first.execute("INSERT INTO music VALUES (? , ? , ? , ? , ? , ? ) , 
        (song_name , artist , publish_year , album , address , gener ) " ) 

def delete_song_by_id(id ) :
    first.execute("DELETE from music WHERE rowid = id ") 


def get_album(album ) :
    first.execute("SELECT * FROM music WHERE album = album 
