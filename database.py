
import sqlite3

connection = sqlite3.connect('musics.db')

first = connection.cursor() 


def insert_song(song_name , artist , publish_year , album , address , gener) :

    first.execute("INSERT INTO music VALUES (? , ? , ? , ? , ? , ? ) ", 
        (song_name , artist , publish_year , album , address , gener )  ) 

def delete_song_by_id(id ) :
    first.execute("DELETE from music WHERE rowid = ?" , (id) ) 


def get_album(album ) :
    
    first.execute("SELECT * FROM music WHERE album  = ?" , (album ) )
    new_list = first.fetchall()
    
    return new_list

def get_artist(artist ) :

    first.execute("SELECT * FROM music WHERE artist = ?" , (artist) ) 
    new_list = first.fetchall() 
    
    return new_list

def get_gener(gener) :

    first.execute("SELETC * from music WHERE gener = ? " , (gener) ) 
    new_list = first.fetchall() 
    
    return new_list


