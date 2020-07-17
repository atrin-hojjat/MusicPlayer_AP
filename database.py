
import sqlite3

connection = sqlite3.connect('musics.db')

first = connection.cursor() 

#insert a song to our music table with song's information 

def insert_song(song_name , artist , publish_year , album , address , gener) :

    first.execute("INSERT INTO music VALUES (? , ? , ? , ? , ? , ? ) ", 
        (song_name , artist , publish_year , album , address , gener )  ) 
    
    connection.close()

#delete a song by it's id

def get_song_by_address(address):
    first.execute("SELECT * FROM music WHERE address=?", (address))
    ret = first.fetchall()
    return ret

def delete_song_by_id(id ) :
    first.execute("DELETE from music WHERE rowid = ?" , (id) ) 

    connection.close()

#gives the user all the songs in album which he wants

def get_album(album ) :
    
    first.execute("SELECT * FROM music WHERE album  = ?" , (album ) )
    new_list = first.fetchall()
    
    connection.close()

    return new_list

#gives the user all the songs from artist he wants

def get_artist(artist ) :

    first.execute("SELECT * FROM music WHERE artist = ?" , (artist) ) 
    new_list = first.fetchall() 
    
    connection.close()

    return new_list

#gives the user all the songs with the gener he wants

def get_gener(gener) :

    first.execute("SELETC * from music WHERE gener = ? " , (gener) ) 
    new_list = first.fetchall() 
    
    connection.close()

    return new_list

# gives the user list of all existing albums

def get_albums() :

    first.execute("SELECT DISTINCT album FROM music ")
    new_list = first.fetchall() 
    
    connection.close()

    return new_list

# gives the user list of all existing artists

def get_artists() :

    first.execute("SELECT DISTINCT artist FROM music ") 
    new_list = first.fetchall() 

    connection.close()

    return new_list 

#gives the user list of all geners

def get_gener() :

    first.execute("SELECT DISTINCT gener FROM music " ) 
    new_list = first.fetchall() 
    
    connection.close()

    return new_list

#gives the user all the songs from playlist which user wants

def get_playlist(id ) :
    
    first.execute("SELETC * FROM playlist_song WHERE playlist_id = ? " (id) )
    new_list = first.fetchall() 
    
    connection.close()

    return new_list 

#shows all the existing playlists

def get_playlists() :

    first.execute("SELECT DISTINCT playlist_id FROM playlist_song " )
    new_list = first.fetchall() 

    connection.close()

    return new_list

#add a new playlist with all songs user wants 

def add_playlist(playlist_name , song_list ) :

    first.execute("INSERT INTO playlist VALUES (?) " , (playlist_name) ) 
    first.execute("SELECT id , * FROM playlist LIMIT 1 ORDER BY DESC " ) 
    
    element = first.fetchall()

    new_list = []
    for i in range(len(song_list) ) :
        new_list.append(i + 1 , song_list[i] , element[1])
    first.execute("INSERT INTO Playlist_song VALUES (? , ? , ? ) " , new_list) 

    connection.close()

#delete a playlist by its name which user gives us

def delete_playlist(playlist_name ) :

    first.execute("DELETE FROM playlist WHERE playlist_name = ?" ,(playlist_name) )
    first.execute("DELETE FROM playlist_song WHERE playlist_id = ? " (playlist_name) ) 

    connection.close()


