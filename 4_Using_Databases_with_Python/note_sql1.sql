DROP TABLE IF EXISTS Users;
 
CREATE TABLE Users ('name' TEXT, 'email' TEXT);

INSERT INTO Users (name, email) VALUES ('Chuck', 'csev@umich.edu');
INSERT INTO Users (name, email) VALUES ('Colleen', 'cvl@umich.edu');
INSERT INTO Users (name, email) VALUES ('Ted', 'ted@umich.edu');
INSERT INTO Users (name, email) VALUES ('Sally', 'a1@umich.edu');
INSERT INTO Users (name, email) VALUES ('Ted', 'ted@umich.edu');
INSERT INTO Users (name, email) VALUES ('Kristen', 'kf@umich.edu');

DELETE FROM Users WHERE email='ted@umich.edu';

UPDATE Users SET name='Charles' WHERE email='csev@umich.edu';

SELECT * FROM Users;

SELECT * FROM Users ORDER BY email;

SELECT * FROM Users ORDER BY name DESC;


