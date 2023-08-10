-- This sql file creates a 'users' table using the below parameter
-- id, integer, never null, auto increment and primary key
-- email, string (255 characters), never null and unique
-- name, string (255 characters)

-- creating database first
-- CREATE DATABASE IF NOT EXISTS holberton;

DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255) NOT NULL);
