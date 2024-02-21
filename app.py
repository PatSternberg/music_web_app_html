# file: app.py

from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.database_connection import DatabaseConnection

import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /albums
# Returns the list of storead albums  as HTML
# Try it:
#   ; open http://localhost:5001/albums
@app.route('/albums', methods=['GET'])
def get_albums():
    # We use `render_template` to send the user the file `albums.html`
    return render_template('albums.html')

# class Application():

#     def __init__(self):
#         self._connection = DatabaseConnection()
#         self._connection.connect()
#         self._connection.seed("seeds/music_library_tables.sql")

#     def run(self):
#     # "Runs" the terminal application.
#         # Ask the user to enter some input
#         print('''What would you like to do?
#               1 - List all albums
#               2 - List all artists
              
#               Enter your choice: ''')
#         # Make some decisions based on that input
#         x = input()
#         if x == '1':
#             album_repository = AlbumRepository(self._connection)
#             albums = album_repository.all()
#             for album in albums:
#                 print(f"{album.id}: {album.title} ({album.release_year})")
#             print('\n')
#         elif x == '2':
#             artist_repository = ArtistRepository(self._connection)
#             artists = artist_repository.all()
#             for artist in artists:
#                 print(f"{artist.id}: {artist.name} ({artist.genre})")
#             print('\n')
#         else:
#             print('Enter a valid choice')

# if __name__ == '__main__':
#     app = Application()
#     app.run()


# import os
# from flask import Flask, request, render_template
# from lib.database_connection import get_flask_database_connection

# # Create a new Flask app
# app = Flask(__name__)

# # == Your Routes Here ==


# # == Example Code Below ==

# # GET /emoji
# # Returns a smiley face in HTML
# # Try it:
# #   ; open http://localhost:5001/emoji
# @app.route('/emoji', methods=['GET'])
# def get_emoji():
#     # We use `render_template` to send the user the file `emoji.html`
#     # But first, it gets processed to look for placeholders like {{ emoji }}
#     # These placeholders are replaced with the values we pass in as arguments
#     return render_template('emoji.html', emoji=':)')



# # This imports some more example routes for you to see how they work
# # You can delete these lines if you don't need them.
# from example_routes import apply_example_routes
# apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
