from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When we call AlbumRepository#all
We get a list of Album objects reflecting the seed data.
"""

def test_get_all_records(db_connection):
    db_connection.seed('seeds/music_library_tables.sql') # Seed our database with some test data
    repository = AlbumRepository(db_connection) # Create a new AlbumRepository
    albums = repository.all() # Get all albums
    # Assert on the results
    assert albums == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Super Trouper', 1980, 2),
        Album(3, 'Bossanova', 1990, 1),
        Album(4, 'Folklore', 2020, 3),
        Album(5, 'I Put a Spell on You', 1965, 4),
        Album(6, 'Here Comes the Sun', 1971, 4),
        Album(7, 'Ring Ring', 1973, 2)
    ]

# """
# When we call AlbumRepository#find
# We get a single Album object reflecting the seed data.
# """

# def test_get_single_record(db_connection):
#     db_connection.seed("seeds/music_library_tables.sql")
#     repository = AlbumRepository(db_connection)

#     album = repository.find(3)
#     assert album == Album(3, 'Waterloo', 1974, 2)

# """
# When we call ArtistRepository#create
# We get a new record in the database.
# """

# def test_create_record(db_connection):
#     db_connection.seed("seeds/music_library_tables.sql")
#     repository = AlbumRepository(db_connection)
    
#     repository.create(Album(13, 'Trompe le Monde', 1991, 1))
#     result = repository.all()
#     assert result == [
#         Album(1, 'Doolittle', 1989, 1),
#         Album(2, 'Surfer Rosa', 1988, 1),
#         Album(3, 'Waterloo', 1974, 2),
#         Album(4, 'Super Trouper', 1980, 2),
#         Album(5, 'Bossanova', 1990, 1),
#         Album(6, 'Lover', 2019, 3),
#         Album(7, 'Folklore', 2020, 3),
#         Album(8, 'I Put a Spell on You', 1965, 4),
#         Album(9, 'Baltimore', 1978, 4),
#         Album(10, 'Here Comes the Sun', 1971, 4),
#         Album(11, 'Fodder on My Wings', 1982, 4),
#         Album(12, 'Ring Ring', 1973, 2),
#         Album(13, 'Trompe le Monde', 1991, 1)
#     ]

# """
# When we call ArtistRepository#delete
# We remove a record from the database.
# """

# def test_delete_record(db_connection):
#     db_connection.seed("seeds/music_library_tables.sql")
#     repository = AlbumRepository(db_connection)

#     repository.delete(3)

#     result = repository.all()
#     assert result == [
#         Album(1, 'Doolittle', 1989, 1),
#         Album(2, 'Surfer Rosa', 1988, 1),
#         Album(4, 'Super Trouper', 1980, 2),
#         Album(5, 'Bossanova', 1990, 1),
#         Album(6, 'Lover', 2019, 3),
#         Album(7, 'Folklore', 2020, 3),
#         Album(8, 'I Put a Spell on You', 1965, 4),
#         Album(9, 'Baltimore', 1978, 4),
#         Album(10, 'Here Comes the Sun', 1971, 4),
#         Album(11, 'Fodder on My Wings', 1982, 4),
#         Album(12, 'Ring Ring', 1973, 2)
#     ]