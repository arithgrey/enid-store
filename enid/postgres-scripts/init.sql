CREATE USER db_user WITH PASSWORD 'test';

CREATE DATABASE db_enid OWNER db_user;

GRANT ALL PRIVILEGES ON DATABASE db_enid TO db_user;