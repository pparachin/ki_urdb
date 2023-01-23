# jeden SELECT bude obsahovat vnořený SELECT
SELECT title, release_year
FROM albums
WHERE id_a = (SELECT album_id
                  FROM songs
                  WHERE name = 'Mráz');