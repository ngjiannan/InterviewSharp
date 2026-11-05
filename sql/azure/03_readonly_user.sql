-- Run in the PracticeDB database as the Azure SQL admin.
-- Replace the password before running. This login can only read data.
-- On Azure SQL a contained database user avoids needing access to master.
CREATE USER practice_reader WITH PASSWORD = 'CHANGE-ME-Str0ng!Passw0rd';
ALTER ROLE db_datareader ADD MEMBER practice_reader;
DENY INSERT, UPDATE, DELETE, ALTER, EXECUTE, CREATE TABLE, CREATE VIEW, CREATE PROCEDURE, CREATE FUNCTION, CREATE SCHEMA, REFERENCES TO practice_reader;
DENY VIEW DATABASE STATE TO practice_reader;
