/*
f) TRIGGER (1x), který ošetří práci s daty nad nějakou tabulkou DB
- využívají se hlavně pro příkazy INSERT, UPDATE, DELETE, ale můžete zkusit i jiný typ
- např. pro UPDATE do nové tabulky zapíše datum, čas a informace o uživateli, který
nějakým způsobem upravoval data v dané tabulce
*/
CREATE TRIGGER `update_song_count` AFTER INSERT ON `songs`
 FOR EACH ROW BEGIN
  UPDATE albums SET number_of_songs = number_of_songs + 1 WHERE id_a = NEW.album_id;
END