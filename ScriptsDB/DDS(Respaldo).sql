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
        num_version INT NOT NULL COMMENT "Version del dibujo",
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

        INSERT INTO User(var_userName, var_password, bit_type, var_penColor, var_fillColor) VALUE (
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
    IN paintName VARCHAR(20), IN jso_data BLOB, 
    IN id_user INT, IN adminPassword VARCHAR(7)
)
    BEGIN 
        INSERT INTO Paint(blob_name, blob_data, id_user) VALUE (
            AES_ENCRYPT(paintName,adminPassword), 
            AES_ENCRYPT(jso_data,adminPassword),
            id_user
            );
    END $$

CREATE PROCEDURE sp_searchVersion(
    IN namePaint VARCHAR(20),
    IN idUser INT,
    OUT result INT
)BEGIN
    DECLARE theNamePaint VARCHAR(20);
    DECLARE finished INT DEFAULT 0;
    DECLARE theversion INT DEFAULT 1;
    DECLARE cursorBinacle
            CURSOR FOR 
                    SELECT tex_namePaint,num_version FROM Binnacle WHERE id_user = idUser ORDER BY num_version DESC;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET finished = 1;

    OPEN cursorBinacle;
        getPaint: LOOP 
            FETCH cursorBinacle INTO theNamePaint, theversion;
            IF finished = 1 THEN
                SET result = theversion;
                LEAVE getPaint;
            END IF;
            IF theNamePaint = namePaint THEN 
                SET result = theversion + 1;
                LEAVE getPaint;
            END IF;
        END LOOP getPaint;
    CLOSE cursorBinacle;
END$$

CREATE TRIGGER InsertPaint AFTER INSERT ON Paint
        FOR EACH ROW
        BEGIN
            DECLARE theversion INT;
            CALL sp_searchVersion(CAST(AES_DECRYPT(NEW.blob_name,'admin')AS CHAR),NEW.id_user,theversion );

            INSERT INTO Binnacle(tex_action,id_user,tex_namePaint,num_version) VALUES ("Insert", 
            NEW.id_user,CAST(AES_DECRYPT(NEW.blob_name,'admin')AS CHAR), theversion);
        END $$

DELIMITER ;

SET @admin = 0;
CALL sp_addUser("admin","admin",0,'#FFFFFF','#222222','admin', @admin);