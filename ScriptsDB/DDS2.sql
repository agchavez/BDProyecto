DROP DATABASE IF EXISTS Respaldo;
CREATE DATABASE Respaldo CHARACTER SET utf8;

USE Respaldo;

CREATE TABLE IF NOT EXISTS Draw(
    id INT AUTO_INCREMENT PRIMARY KEY,
    var_Name VARCHAR(20) NOT NULL COMMENT "Nombre del dibujo",
    blo_Content blob NOT NULL COMMENT "Contenido del dibujo"
)COMMENT "Descripción de la tabla Dibujo";


INSERT INTO Draw(var_Name, blo_Content) VALUES("prueba","{}");