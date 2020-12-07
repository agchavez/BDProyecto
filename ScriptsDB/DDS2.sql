DROP DATABASE IF EXISTS Respaldo;
CREATE DATABASE Respaldo CHARACTER SET utf8;

USE Respaldo;

CREATE TABLE IF EXISTS User(
    id INT AUTO_INCREMENT PRIMARY KEY,
    tex_nameUser TEXT NOT NULL COMMENT "Nombre del usuario que realizo el dibujo encriptado",
    tex_password TEXT NOT NULL COMMENT "Constrasela del usuario ingresado encriptado",
    tex_fillColor TEXT NOT NULL COMMENT "Color del fillcolor por defecto encriptado",
    tex_penColor TEXT NOT NULL COMMENT "Color por defecto del pencolor encriptado",
    tex_type TEXT NOT NULL DEFAULT 0 COMMENT "Tipo de usuario cero (0) si es administrador y uno (1) si es operador encriptado"
)COMMENT "Datos del usuario encriptados";

CREATE TABLE IF NOT EXISTS Draw(
    id INT AUTO_INCREMENT PRIMARY KEY,
    tex_Name TEXT NOT NULL COMMENT "Nombre del dibujo encriptado",
    blo_Content BLOB NOT NULL COMMENT "Contenido del dibujo encriptado",
    id_user INT NOT NULL COMMENT "llave foranéa de la tabla de usuario",
    FOREIGN KEY (id_user) REFERENCES User(id)
)COMMENT "Descripción de la tabla Dibujo";


DELIMITER $$
DROP PROCEDURE IF EXISTS sp_addPaint;
CREATE PROCEDURE sp_addPaint(
    IN paintName TEXT, IN jso_data BLOB, 
    IN id_user INT,
    OUT result BIT
)
    BEGIN 
        INSERT INTO Paint(var_name, jso_data, id_user) VALUE (paintName, jso_data,id_user);
        SET result = 1;
    END $$

DROP PROCEDURE IF EXISTS sp_addUser;
CREATE PROCEDURE sp_addUser(
    IN serName TEXT, IN passwor TEXT, 
    IN typex TEXT, IN penColor TEXT, IN fillColor TEXT, 
    OUT result INT
)
    BEGIN 
        INSERT INTO User(var_userName, var_password, bit_type, var_fillColor, var_penColor ) VALUE (serName, passwor, typex, penColor, fillColor);
        SET result = lAST_INSERT_ID();
    END $$

DELIMITER;

