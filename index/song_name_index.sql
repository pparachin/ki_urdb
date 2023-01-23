/*
c) INDEX (1x), indexový soubor nad nějakým sloupcem tabulky
- alespoň jeden netriviální indexový soubor (unikátní, fulltextový, …)
*/

-- Tento index umožní fulltextové vyhledávání písní dle jejich názvů.

CREATE FULLTEXT INDEX song_name_index ON songs (name);