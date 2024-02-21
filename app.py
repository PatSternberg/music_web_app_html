# file: app.py
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /albums
# Returns the list of stored albums as HTML
# Try it:
#   ; open http://localhost:5001/albums
@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    # We use `render_template` to send the user the file `albums.html`
    return render_template('albums.html', albums=albums)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
