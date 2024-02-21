# file: app.py
from lib.album import Album
from lib.album_repository import AlbumRepository
from lib.artist import Artist
from lib.artist_repository import ArtistRepository
import os
from flask import Flask, request, render_template, redirect
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

# GET /album
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

# GET /books/new
# Returns a form to create a new book
@app.route('/albums/new', methods=['GET'])
def get_new_album():
    return render_template('albums/new.html')

# POST /albums
# Creates a new album
@app.route('/albums', methods=['POST'])
def create_album():
    # Set up the database connection and repository
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)

    # Get the fields from the request form
    title = request.form['title']
    release_year = request.form['release_year']

    # Create an album object
    album = Album(None, title, release_year, 1)

    # Check for validity and if not valid, show the form again with errors
    if not album.is_valid():
        return render_template('albums/new.html', album=album, errors=album.generate_errors()), 400

    # Save the book to the database
    album = repository.create(album)

    # Redirect to the book's show route to the user can see it
    return redirect(f"/albums/{album.id}")

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
