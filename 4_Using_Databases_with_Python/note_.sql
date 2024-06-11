-- Multiple tables in SQL

CREATE TABLE 'Artist' (
    'id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    'name' TEXT);

CREATE TABLE 'Album' (
    'id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    'artist_id' INTEGER,
    'title' TEXT);

CREATE TABLE 'Genre' (
    'id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    'name' TEXT);

CREATE TABLE 'Track' (
    'id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    'album_id' INTEGER,
    'genre_id' INTEGER,
    'len' INTEGER,
    'rating' INTEGER,
    'title' TEXT,
    'count' INTEGER);

INSERT INTO Artist (name) VALUES ('Led Zepplin');
INSERT INTO Artist (name) VALUES ('AC/DC');

INSERT INTO Genre (name) VALUES ('Rock');
INSERT INTO Genre (name) VALUES ('Metal');

INSERT INTO Album (title, artist_id) VALUES ('Who Made Who', 2);
INSERT INTO Album (title, artist_id) VALUES ('IV', 1);

INSERT INTO Track (title, rating, len, count, album_id, genre_id)
    VALUES ('Black Dog', 5, 297, 0, 2, 1);
INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
    VALUES ('Stairway', 5, 482, 0, 2, 1) ;
INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
    VALUES ('About to Rock', 5, 313, 0, 1, 2) ;
INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
    VALUES ('Who Made Who', 5, 207, 0, 1, 2) ;

-- Select Album title and Artist name:

SELECT Album.title, Artist.name 
FROM Album JOIN Artist
WHERE Album.artist_id = Artist.id;

SELECT Album.title, Album.artist_id, Artist.id, Artist.name 
    FROM Album JOIN Artist ON Album.artist_id = Artist.id;

-- Select Track title, artist name, album title and genre name:

SELECT Track.title as Track_Title, Artist.name AS Artist_Name, Album.title AS Album_Name, Genre.name AS Genre_Name
FROM Track JOIN Artist JOIN Album JOIN Genre
ON Track.genre_id = Genre.id AND Track.album_id = Album.id 
    AND Album.artist_id = Artist.id;

