DROP DATABASE IF EXISTS BackupDB;
CREATE DATABASE BackupDB CHARACTER SET utf8;
USE BackupDB;

CREATE TABLE IF NOT EXISTS User(
    id INT AUTO_INCREMENT PRIMARY KEY,
    var_userName BLOB NOT NULL COMMENT "id de la tabla de User",
    var_password BLOB NOT NULL COMMENT "Contraseña de usuario",
    var_fillColor BLOB NOT NULL COMMENT "Color del fillcolor por defecto",
    var_penColor BLOB NOT NULL COMMENT "Color por defecto del pencolor",
    bit_type BIT NOT NULL DEFAULT 0 COMMENT "Tipo de usuario cero (0) si es administrador y uno (1) si es operador"
)COMMENT "Descripción de la tabla user";

CREATE TABLE IF NOT EXISTS Paint(
    id INT AUTO_INCREMENT PRIMARY KEY,
    blob_name BLOB NOT NULL COMMENT "Nombre del dibujo",
    blob_data BLOB NOT NULL COMMENT "Información del dibujo ",
    id_user INT NOT NULL COMMENT "llave foranéa de la tabla de usuario",
    FOREIGN KEY (id_user) REFERENCES User(id) ON DELETE CASCADE ON UPDATE CASCADE
)COMMENT "Descripción de la tabla paint con sus respectivos campos";

CREATE TABLE IF NOT EXISTS Binnacle(
        id INT AUTO_INCREMENT PRIMARY KEY,
        dat_date TIMESTAMP DEFAULT NOW() ON UPDATE NOW() COMMENT "Fecha de los cambios",
        tex_action ENUM('Insert') NOT NULL COMMENT "Acción que realiza el usuario ya sea operador o administrador",
        tex_namePaint VARCHAR(20) NOT NULL COMMENT "Nombre del dibujo creado",
        id_user INT NOT NULL COMMENT "Llave foranéa de la tabla de User",
        FOREIGN KEY (id_user) REFERENCES User(id) ON DELETE CASCADE ON UPDATE CASCADE
)COMMENT "Descripción de la tabla  de bitacora(Binnacle) con sus respectivos campos";


DELIMITER $$

CREATE PROCEDURE sp_addUser(
    IN serName VARCHAR(20), IN passwor VARCHAR(20), 
    IN typex BIT, IN penColor VARCHAR(7), IN fillColor VARCHAR(7),
    IN adminPassword VARCHAR(7),
    OUT result INT
)
    BEGIN   

        INSERT INTO User(var_userName, var_password, bit_type, var_fillColor, var_penColor) VALUE (
            AES_ENCRYPT(serName,adminPassword), 
            AES_ENCRYPT(passwor,adminPassword), 
            typex, 
            AES_ENCRYPT(penColor,adminPassword), 
            AES_ENCRYPT(fillColor,adminPassword)
            );
        SET result = lAST_INSERT_ID();
    END $$

DROP PROCEDURE IF EXISTS sp_addPaint;

-- Agregar Dibujos
CREATE PROCEDURE sp_addPaint(
    IN paintName VARCHAR(20), IN blob_data BLOB, 
    IN id_user INT, IN adminPassword VARCHAR(7),
    OUT result INT
)
    BEGIN 
        INSERT INTO Paint(blob_name, blob_data, id_user) VALUE (
            AES_ENCRYPT(paintName,adminPassword), 
            AES_ENCRYPT(blob_data,adminPassword),
            id_user
            );
        SET result = lAST_INSERT_ID();
    END $$

DELIMITER ;
CREATE TRIGGER InsertPaint AFTER INSERT ON Paint
        FOR EACH ROW
            INSERT INTO Binnacle(tex_action,id_user,tex_namePaint) VALUES ("Insert", 
            NEW.id_user,CAST(AES_DECRYPT(NEW.blob_name,'admin')AS CHAR));

SET @admin = 0;
CALL sp_addUser("admin","admin",0,'#FFFFFF','#222222','admin', @admin);
