# file: app.py

from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.database_connection import DatabaseConnection

class Application():

    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library_tables.sql")

    def run(self):
    # "Runs" the terminal application.
        # Ask the user to enter some input
        print('''What would you like to do?
              1 - List all albums
              2 - List all artists
              
              Enter your choice: ''')
        # Make some decisions based on that input
        x = input()
        if x == '1':
            album_repository = AlbumRepository(self._connection)
            albums = album_repository.all()
            for album in albums:
                print(f"{album.id}: {album.title} ({album.release_year})")
            print('\n')
        elif x == '2':
            artist_repository = ArtistRepository(self._connection)
            artists = artist_repository.all()
            for artist in artists:
                print(f"{artist.id}: {artist.name} ({artist.genre})")
            print('\n')
        else:
            print('Enter a valid choice')

if __name__ == '__main__':
    app = Application()
    app.run()
