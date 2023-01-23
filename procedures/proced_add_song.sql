/*
e)
PROCEDURE (1x), která bude používat 1x CURSOR a také 1x ošetření chyb (HANDLER /
TRY…CATCH / RAISE / EXCEPTION - dle zvoleného DBMS)
*/
DELIMITER //
CREATE PROCEDURE add_song (IN song_name VARCHAR(255), IN album_id INT, IN author_id INT, IN genre_id INT, IN length INT, IN number_of_plays INT, IN release_year INT)
BEGIN
    DECLARE song_id INT;
    DECLARE album_title VARCHAR(255);
    DECLARE genre_name VARCHAR(255);
    DECLARE author_name VARCHAR(255);

    BEGIN
    DECLARE album_cursor CURSOR FOR SELECT title FROM albums WHERE id_a = album_id;
    OPEN album_cursor;
    FETCH album_cursor INTO album_title;
    CLOSE album_cursor;
    END;

    BEGIN
    DECLARE author_cursor CURSOR FOR SELECT name FROM authors WHERE id_a = author_id;
    OPEN author_cursor;
    FETCH author_cursor INTO author_name;
    CLOSE author_cursor;
    END;

    BEGIN
    DECLARE genre_cursor CURSOR FOR SELECT title FROM genres WHERE id_g = genre_id;
    OPEN genre_cursor;
    FETCH genre_cursor INTO genre_name;
    CLOSE genre_cursor;
    END;

    BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        SELECT "Chyba při přidávání písničky: " , song_name , " do alba: " , album_title , " od autora: " , author_name;
        ROLLBACK;
        RESIGNAL;
    END;

    BEGIN
    START TRANSACTION;
	INSERT INTO songs (name, album_id, genre_id, length, number_of_plays, release_year, created_at, updated_at)
	VALUES (song_name, album_id, genre_id, length, number_of_plays, release_year, NOW(), NOW());
	SELECT LAST_INSERT_ID() INTO song_id;
	INSERT INTO authors_songs (id_a, id_s, created_at, updated_at)
	VALUES (author_id, song_id, NOW(), NOW());
	SELECT "Úspešně přidaná: " , song_name , "do alba: " , album_title , " od autora: " , author_name , " se žánřem: " , genre_name , " a id: " , song_id;
	COMMIT;
    END;
END
