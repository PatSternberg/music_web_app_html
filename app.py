# file: app.py
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

# == Routes below ==

# = Landing page Routes =

# GET /landing_page
# Returns the list of stored albums as HTML
# Try it:
#   ; open http://localhost:5001/albums/all
@app.route('/landing_page', methods=['GET'])
def get_landing_page():
    # We use `render_template` to send the user the file `landing_page.html`
    return render_template('landing_page.html')

# = Album Routes =

# GET /albums
# Returns the list of stored albums as HTML
# Try it:
#   ; open http://localhost:5001/albums/all
@app.route('/albums/all', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    # We use `render_template` to send the user the file `albums/all.html`
    return render_template('albums/all.html', albums=albums)

# GET /artist
# Returns the album with the supplied id as HTML
# Try it:
#   ; open http://localhost:5001/albums/1
@app.route('/albums/<int:id>', methods=['GET'])
def get_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.find(id)
    # We use `render_template` to send the user the file `albums/show.html`
    return render_template('albums/show.html', album=album)

# = Artist Routes =

# GET /artists
# Returns the list of stored artist as HTML
# Try it:
#   ; open http://localhost:5001/artists/all
@app.route('/artists/all', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    # We use `render_template` to send the user the file `artists/all.html`
    return render_template('artists/all.html', artists=artists)

# GET /artist
# Returns the artist with the supplied id as HTML
# Try it:
#   ; open http://localhost:5001/artists/1
@app.route('/artists/<int:id>', methods=['GET'])
def get_artist(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = repository.find(id)
    # We use `render_template` to send the user the file `artists/show.html`
    return render_template('artists/show.html', artist=artist)

# == Run program ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
