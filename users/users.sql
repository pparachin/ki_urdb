/*
h) USER - mít předem připravené příkazy na ukázku
*/
-- umět vytvořit účet uživatele
# xampp/mysqs/bin
# mysql -u root
CREATE USER 'test'@'localhost' IDENTIFIED BY 'heslo';
# - umět smazat účet uživatele
DROP USER test;
# - umět se přihlásit jako právě vytvořený uživatel a ověřit dostupnost databází
# mysql -u test -p
# - umět vytvořit/odstranit roli CREATE/DROP ROLE (některé DBMS nemají)
CREATE ROLE admin;
GRANT SELECT ON *.* TO admin;
