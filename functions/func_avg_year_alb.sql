/*
d) FUNCTION (1x), která bude realizovat výpočet nějaké hodnoty z dat v DB
- average_album_year(), která výpočet průměrný rok vydání alb
*/

DELIMITER //
CREATE FUNCTION average_album_year ()
RETURNS INT
BEGIN
    DECLARE avg_year INT;
    SELECT AVG(release_year) INTO avg_year FROM albums;
    RETURN avg_year;
END //
DELIMITER ;