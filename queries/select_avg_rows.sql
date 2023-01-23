-- jeden SELECT vypočte průměrný počet záznamů na jednu tabulku v DB
SELECT AVG(TABLE_ROWS)
    FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_SCHEMA = 'ki_urdb_parachin';