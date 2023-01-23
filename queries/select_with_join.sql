-- jeden SELECT bude řešit rekurzi nebo hierarchii (JOIN)
SELECT albums.title, albums.release_year, authors.name
FROM albums
INNER JOIN authors ON albums.author_id=authors.id_a
