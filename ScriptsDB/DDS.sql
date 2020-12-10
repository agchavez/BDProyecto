DROP DATABASE IF EXISTS Proyecto2;
CREATE DATABASE Proyecto2 CHARACTER SET utf8;
USE Proyecto2;

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
    var_name BLOB NOT NULL COMMENT "Nombre del dibujo",
    jso_data BLOB NOT NULL COMMENT "Información del dibujo ",
    id_user INT NOT NULL COMMENT "llave foranéa de la tabla de usuario",
    FOREIGN KEY (id_user) REFERENCES User(id) ON DELETE CASCADE ON UPDATE CASCADE
)COMMENT "Descripción de la tabla paint con sus respectivos campos";

CREATE TABLE IF NOT EXISTS Binnacle(
        id INT AUTO_INCREMENT PRIMARY KEY,
        dat_date TIMESTAMP DEFAULT NOW() ON UPDATE NOW() COMMENT "Fecha de los cambios",
        tex_action ENUM('Login','Insert','Delete','Update','ColorConf') NOT NULL COMMENT "Acción que realiza el usuario ya sea operador o administrador",
        id_user INT NOT NULL COMMENT "Llave foranéa de la tabla de User",
        var_fillColor VARCHAR(7) COMMENT "Color de fondo hexadecimal",
        var_penColor VARCHAR(7) COMMENT "Color de lápiz decimal",
        FOREIGN KEY (id_user) REFERENCES User(id) ON DELETE CASCADE ON UPDATE CASCADE
)COMMENT "Descripción de la tabla  de bitacora(Binnacle) con sus respectivos campos";

DROP PROCEDURE IF EXISTS sp_showUser;

DELIMITER $$ 

 -- Logi de usuario
CREATE PROCEDURE sp_login(
    IN userName VARCHAR(20), IN passwor VARCHAR(20), OUT result BIT, OUT idUser INT
)BEGIN 
        DECLARE theuser VARCHAR(20);
        DECLARE thepassword VARCHAR(20);
        DECLARE finished INT DEFAULT 0;
        DECLARE id_user INT DEFAULT 0;

        DECLARE cursorUser
                CURSOR FOR 
                    SELECT CAST(AES_DECRYPT(var_userName,'admin')AS CHAR), CAST(AES_DECRYPT(var_password,'admin')AS CHAR), id FROM User;
        DECLARE CONTINUE HANDLER FOR NOT FOUND SET finished = 1;

        OPEN cursorUser;
            getUser: LOOP 
                FETCH cursorUser INTO theuser, thepassword, id_user;
                IF finished = 1 THEN
                    SET result = 0;
                    LEAVE getUser;
                END IF;
                IF theuser = userName AND thepassword = passwor  THEN 
                    SET result = 1;
                    SET idUser = id_user;
                    LEAVE getUser;
                END IF;
            END LOOP getUser;
        CLOSE cursorUser;     
END$$

DROP PROCEDURE IF EXISTS sp_searchUser;
 -- Buscar usuario
CREATE PROCEDURE sp_searchUser(
    IN userName VARCHAR(20),
    OUT result BIT
)BEGIN 
        DECLARE theuser VARCHAR(20);
        DECLARE finished INT DEFAULT 0;

        DECLARE cursorUser
                CURSOR FOR 
                    SELECT CAST(AES_DECRYPT(var_userName,'admin')AS CHAR) FROM User;
        DECLARE CONTINUE HANDLER FOR NOT FOUND SET finished = 1;

        OPEN cursorUser;
            getUser: LOOP 
                FETCH cursorUser INTO theuser;
                IF finished = 1 THEN
                    SET result = 0;
                    LEAVE getUser;
                END IF;
                IF theuser = userName THEN 
                    SET result = 1;
                    LEAVE getUser;
                END IF;
            END LOOP getUser;
        CLOSE cursorUser;  
END $$

DROP PROCEDURE IF EXISTS sp_addUser;
 /* Agregar un usuario */
CREATE PROCEDURE sp_addUser(
    IN serName VARCHAR(20), 
    IN passwor VARCHAR(20), 
    IN typex BIT, 
    IN penColor VARCHAR(7), 
    IN fillColor VARCHAR(7), 
    OUT result INT
)BEGIN 
        INSERT INTO User(var_userName, var_password, bit_type, var_fillColor, var_penColor) VALUES (AES_ENCRYPT(serName,'admin'), AES_ENCRYPT(passwor,'admin'), typex, AES_ENCRYPT(penColor,'admin'), AES_ENCRYPT(fillColor,'admin') 
        );
        INSERT INTO BackupDB.User(var_userName, var_password, bit_type, var_fillColor, var_penColor) VALUES (AES_ENCRYPT(serName,'admin'), AES_ENCRYPT(passwor,'admin'), typex, AES_ENCRYPT(penColor,'admin'), AES_ENCRYPT(fillColor,'admin') 
        );

        SET result = LAST_INSERT_ID();
END $$

DROP PROCEDURE IF EXISTS sp_updateUser;
 -- Actualizar un usuario
CREATE PROCEDURE sp_updateUser(
    IN serName VARCHAR(20), IN passwor VARCHAR(20), 
    IN typex BIT, IN penColor VARCHAR(7), IN fillColor VARCHAR(7), IN idUser INT, 
    OUT result BIT
)BEGIN
    UPDATE User SET 
        var_userName = AES_ENCRYPT(serName,'admin'),
        var_password = AES_ENCRYPT(passwor,'admin'),
        bit_type = typex,
        var_fillColor = AES_ENCRYPT(fillColor,'admin'), 
        var_penColor = AES_ENCRYPT(penColor,'admin')
        WHERE id = idUser;
        SET result = 1;
END $$

DROP PROCEDURE IF EXISTS sp_dropUser;
 -- ELiminar un usuario
CREATE PROCEDURE sp_dropUser(
    IN idUser INT,
    OUT result BIT
)BEGIN
        DELETE FROM User WHERE id = idUser;
        SET result = 1;
END $$

DROP PROCEDURE IF EXISTS sp_searchAdmin;
 -- Busca el administrador y retorna id
CREATE PROCEDURE sp_searchAdmin(
    IN var_userNam VARCHAR(20), 
    IN var_passwor VARCHAR(20), 
    OUT result BIT,
    OUT id_user INT
)BEGIN
        DECLARE theadmin VARCHAR(20);
        DECLARE thepasswor VARCHAR(20);
        DECLARE theType BIT;
        DECLARE finished INT DEFAULT 0;
        DECLARE idUser INT DEFAULT 0;

        DECLARE cursorUser
                CURSOR FOR 
                    SELECT CAST(AES_DECRYPT(var_userName,'admin')AS CHAR), CAST(AES_DECRYPT(var_password,'admin')AS CHAR), bit_type, id FROM User;

        DECLARE CONTINUE HANDLER FOR NOT FOUND SET finished = 1;

        OPEN cursorUser;
            getUser: LOOP 
                FETCH cursorUser INTO theadmin, thepasswor, theType, idUser;
                IF finished = 1 THEN
                    LEAVE getUser;
                END IF;

                IF (theadmin = var_userNam AND thepasswor = var_passwor AND theType = 0) THEN
                    SET result = 0;
                    SET id_user = idUser;
                    LEAVE getUser;
                END IF;

            END LOOP getUser;
        CLOSE cursorUser;  
END $$

DROP PROCEDURE IF EXISTS sp_searchUsers;
 -- busca todos los usuarios y retorna id
CREATE PROCEDURE sp_searchUsers(
    IN var_userNam VARCHAR(20), 
    IN var_passwor VARCHAR(20), 
    OUT result BIT,
    OUT id_user INT
)BEGIN
        DECLARE theUser VARCHAR(20);
        DECLARE thepasswor VARCHAR(20);
        DECLARE theType BIT;
        DECLARE finished INT DEFAULT 0;
        DECLARE idUser INT DEFAULT 0;

        DECLARE cursorUser
                CURSOR FOR 
                    SELECT CAST(AES_DECRYPT(var_userName,'admin')AS CHAR), CAST(AES_DECRYPT(var_password,'admin')AS CHAR), bit_type, id FROM User;

        DECLARE CONTINUE HANDLER FOR NOT FOUND SET finished = 1;

        OPEN cursorUser;
            getUser: LOOP 
                FETCH cursorUser INTO theUser, thepasswor, theType, idUser;
                IF finished = 1 THEN
                    LEAVE getUser;
                END IF;

                IF ((theUser = var_userNam AND thepasswor = var_passwor) AND (theType = 0 OR theType = 1)) THEN
                    SET result = 0;
                    SET id_user = idUser;
                    CALL sp_addBinnacle(id_user);
                    LEAVE getUser;
                END IF;

            END LOOP getUser;
        CLOSE cursorUser;  
END $$



DROP PROCEDURE IF EXISTS sp_searchPaint;
 -- Buscar dibujo retornar el data
CREATE PROCEDURE sp_searchPaint(
    IN id_paint INT,
    OUT j_data JSON
)BEGIN 
        SET j_data = (SELECT CAST(AES_DECRYPT(jso_data,'admin')AS CHAR) FROM Paint WHERE id = id_paint);
END $$

DROP PROCEDURE IF EXISTS sp_searchPaints;
CREATE PROCEDURE sp_searchPaints(
    IN id_user INT, 
    OUT idPaint INT, 
    OUT result BIT
) BEGIN
        DECLARE thePaintID INT;
        DECLARE theUserID INT;
        DECLARE finished INT DEFAULT 0;

        DECLARE cursorPaint
                CURSOR FOR 
                    SELECT Paint.id, User.id FROM User JOIN Paint ON User.id = Paint.id_User;

        DECLARE CONTINUE HANDLER FOR NOT FOUND SET finished = 1;

        OPEN cursorPaint;
            getUser: LOOP 
                FETCH cursorPaint INTO thePaintID, theUserID;
                IF finished = 1 THEN
                    LEAVE getUser;
                END IF;

                IF (theUserID = id_user) THEN
                    SET idPaint = thePaintID;
                    SET result = 1;
                    LEAVE getUser;
                END IF;

            END LOOP getUser;
        CLOSE cursorPaint;  
END $$

DROP PROCEDURE IF EXISTS sp_addPaint;
 -- Agregar Dibujos
CREATE PROCEDURE sp_addPaint(
    IN paintName VARCHAR(20), 
    IN jso_data BLOB, 
    IN id_user INT,
    OUT result BIT
)BEGIN 
        INSERT INTO Paint(var_name, jso_data, id_user) VALUE (AES_ENCRYPT(paintName,'admin'), AES_ENCRYPT(jso_data,'admin'), id_user);
        SET result = 1;
END $$

DROP PROCEDURE IF EXISTS sp_updatePaint;
 -- Actualizar dibujo
CREATE PROCEDURE sp_updatePaint(
    IN jso_data BLOB, 
    IN id_paint INT,
    OUT result BIT
)BEGIN
        UPDATE Paint SET 
            jso_data = AES_ENCRYPT(jso_data,'admin')
            WHERE id = id_paint;
            SET result = 1;
END $$ 

DROP PROCEDURE IF EXISTS sp_dropPaint;
 -- ELiminar un usuario
CREATE PROCEDURE sp_dropPaint(
    IN id_paint INT,
    OUT result BIT
)BEGIN
        DELETE FROM Paint WHERE id = id_paint;
        SET result = 1;
END $$

 -- Agregar bitacora
CREATE PROCEDURE sp_addBinnacle(
    IN id_user INT
)BEGIN 
    INSERT INTO Binnacle(tex_action,id_user, var_fillColor, var_penColor) VALUES ("Login", id_user, "","");
END $$

 -- Agregar bitacora de configuracion de colores
CREATE PROCEDURE sp_ColorConfig(
    IN id_user INT, IN penColor VARCHAR(7), IN fillColor VARCHAR(7)
)BEGIN
    INSERT INTO Binnacle(tex_action,id_user,var_fillColor, var_penColor) VALUES ("ColorConf",id_user,fillColor,penColor);
END $$

DROP PROCEDURE IF EXISTS sp_searchPaintName;
CREATE PROCEDURE sp_searchPaintName(
    IN idUser INT,
    IN namePaint VARCHAR(20),
    OUT result BIT,
    OUT id_Paint INT
)BEGIN
    DECLARE name_Paint VARCHAR(20);
    DECLARE finish INT DEFAULT 0;
    DECLARE id_P INT;
    DECLARE cursorPaint
            CURSOR FOR
                SELECT CAST(AES_DECRYPT(var_name,'admin')AS CHAR), id FROM Paint WHERE id_user = idUser;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET finish = 1;

    OPEN cursorPaint;
        getPaint: LOOP
            FETCH cursorPaint INTO name_Paint, id_P ;
            IF finish = 1 THEN
                SET result = 0;
                LEAVE getPaint;
            END IF;

            IF (name_Paint = namePaint) THEN
                SET id_Paint = id_P;
                SET result = 1;
                LEAVE getPaint;
            END IF;
        END LOOP getPaint;
    CLOSE cursorPaint;
END$$

DELIMITER ;


DELIMITER $$
    -- Creacion de los trigger
    -- Tigger de insertar dibujo
    DROP TRIGGER IF EXISTS InsertPaint;
    CREATE TRIGGER InsertPaint AFTER INSERT ON Paint
        FOR EACH ROW
        BEGIN
            INSERT INTO Binnacle(tex_action,id_user,var_fillColor, var_penColor) VALUES ("Insert", NEW.id_user, "","");
    END $$

    DROP TRIGGER IF EXISTS DeletePaint;
    -- Tigger de eliminar dibujos
    CREATE TRIGGER DeletePaint AFTER DELETE ON Paint
        FOR EACH ROW
        BEGIN
            INSERT INTO Binnacle(tex_action,id_user, var_fillColor, var_penColor) VALUES ("Delete", OLD.id_user, "","");
        
    END $$

    DROP TRIGGER IF EXISTS UpdatePaint;
    -- Tigger de Actualizar dibujo
    CREATE TRIGGER UpdatePaint AFTER UPDATE ON Paint
        FOR EACH ROW
        BEGIN
            INSERT INTO Binnacle(tex_action,id_user,var_fillColor,var_penColor) VALUES ("Update", OLD.id_user, "","");
    END $$

DELIMITER ;


SET @admin = 0;
CALL sp_addUser("admin","admin",0,'#222222','#222222', @admin);