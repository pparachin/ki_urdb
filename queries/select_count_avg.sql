-- jeden SELECT bude obsahovat nějakou analytickou funkci (SUM, COUNT, AVG,…)

-- Průměrná delká pisníček v tabulce songs
SELECT title, COUNT(name) AS song_count
FROM albums
JOIN songs ON albums.id_a = songs.album_id
GROUP BY title;

-- Avg length of songs in minutes
SELECT AVG(length) / 60
FROM songs;