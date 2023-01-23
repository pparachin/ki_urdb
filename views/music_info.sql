/*
b) VIEW (1x) s podstatnými informacemi z alespoň několika tabulek
- alespoň tři tabulky, mezi informacemi nemají figurovat FK a nedůležité informace
- pro spojení tabulek použijte různé typy příkazu JOIN (inner, left, right, natural, …)
*/

CREATE VIEW music_info AS
SELECT albums.title AS "Název alba", albums.release_year, songs.name AS "Název písníčky",
       authors.name AS "Jméno autora", nationalities.nationality
FROM albums
INNER JOIN songs ON albums.id_a = songs.album_id
INNER JOIN authors_songs ON songs.id_s = authors_songs.id_s
INNER JOIN authors ON authors_songs.id_a = authors.id_a
INNER JOIN nationalities ON authors.nationality_id = nationalities.id_n