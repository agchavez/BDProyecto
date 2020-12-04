DROP DATABASE IF EXISTS Proyecto2;
CREATE DATABASE Proyecto2 CHARACTER SET utf8;

USE Proyecto2;

CREATE TABLE IF NOT EXISTS User(
    id INT AUTO_INCREMENT PRIMARY KEY,
    var_userName VARCHAR(20) NOT NULL COMMENT "id de la tabla de User",
    var_password VARCHAR(20) NOT NULL COMMENT "Contraseña de usuario",
    var_fillColor VARCHAR(6) NOT NULL COMMENT "Color del fillcolor por defecto",
    var_penColor VARCHAR(6) NOT NULL COMMENT "Color por defecto del pencolor",
    boo_type BOOLEAN NOT NULL DEFAULT 0 COMMENT "Tipo de usuario cero (0) si es administrador y uno (1) si es operador"
)COMMENT "Descripción de la tabla user";

CREATE TABLE IF NOT EXISTS Paint(
    id INT AUTO_INCREMENT PRIMARY KEY,
    var_name VARCHAR(20) NOT NULL COMMENT "Nombre del dibujo",
    jso_data JSON NOT NULL COMMENT "Información del dibujo ",
    id_user INT NOT NULL COMMENT "llave foranéa de la tabla de usuario",
    FOREIGN KEY (id_user) REFERENCES User(id) ON DELETE CASCADE ON UPDATE CASCADE
)COMMENT "Descripción de la tabla paint con sus respectivos campos";

CREATE TABLE IF NOT EXISTS Binnacle(
        id INT AUTO_INCREMENT PRIMARY KEY,
        dat_date TIMESTAMP DEFAULT NOW() ON UPDATE NOW() COMMENT "Fecha de los cambios",
        tex_action ENUM('Login','Create','Delete','Update') NOT NULL COMMENT "Acción que realiza el usuario ya sea operador o administrador",
        id_user INT NOT NULL COMMENT "Llave foranéa de la tabla de User",
        FOREIGN KEY (id_user) REFERENCES User(id) ON DELETE CASCADE ON UPDATE CASCADE
)COMMENT "Descripción de la tabla  de bitacora(Binnacle) con sus respectivos campos";

CREATE TABLE IF NOT EXISTS Color(
    id INT AUTO_INCREMENT PRIMARY KEY,
    var_fillColor VARCHAR(7) NOT NULL COMMENT "Color de fondo hexadecimal",
    var_penColor VARCHAR(7) NOT NULL COMMENT "Color de lápiz decimal",
    id_binnacle INT NOT NULL UNIQUE COMMENT "llave foranéa de la tabla de Binnacle",
    FOREIGN KEY (id_binnacle) REFERENCES Binnacle(id) ON DELETE CASCADE ON UPDATE CASCADE
)COMMENT "Descripción de la tabla color con sus respectivos campos";


DROP PROCEDURE IF EXISTS sp_showUser;

DELIMITER $$ 

-- Logi de usuario
CREATE PROCEDURE sp_login(
    IN userName VARCHAR(20), IN passwor VARCHAR(20), OUT result BOOLEAN, OUT idUser INT
    )
    BEGIN 
        DECLARE theuser VARCHAR(20);
        DECLARE thepassword VARCHAR(20);
        DECLARE finished INT DEFAULT 0;
        DECLARE id_user INT DEFAULT 0;

        DECLARE cursorUser
                CURSOR FOR 
                    SELECT var_userName, var_password, id FROM User;
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

-- Buscar usuario
CREATE PROCEDURE sp_searchUser(
    IN userName VARCHAR(20),
    OUT result BOOLEAN
)BEGIN 
        DECLARE theuser VARCHAR(20);
        DECLARE finished INT DEFAULT 0;

        DECLARE cursorUser
                CURSOR FOR 
                    SELECT var_userName FROM User;
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

-- Agregar un usuario
CREATE PROCEDURE sp_addUser(
    IN serName VARCHAR(20), IN passwor VARCHAR(20), 
    IN typex BOOLEAN, IN penColor VARCHAR(6), IN fillColor VARCHAR(6), 
    OUT result BOOLEAN
)
    BEGIN 
        INSERT INTO User(var_userName, var_password, boo_type,var_fillColor, var_penColor ) VALUE (serName, passwor, typex, fillColor, penColor);
        SET result = 1;
    END $$

-- Actualizar un usuario
CREATE PROCEDURE sp_updateUser(
    IN serName VARCHAR(20), IN passwor VARCHAR(20), 
    IN typex BOOLEAN, IN penColor INT, IN fillColor INT, IN idUser INT, 
    OUT result BOOLEAN
)
    BEGIN
        UPDATE User SET 
            var_userName = serName,
            var_password = passwor,
            boo_type = typex,
            var_fillColor = fillColor, 
            var_penColor = penColor
            WHERE id = idUser;
            SET result = 1;

    END $$

-- ELiminar un usuario
CREATE PROCEDURE sp_dropUser(
    IN idUser INT,
    OUT result BOOLEAN
)
    BEGIN
        DELETE FROM User WHERE id = idUser;
        SET result = 1;
    END $$

-- Buscar dibujo retornar el data
CREATE PROCEDURE sp_searchPaint(
    IN id_paint INT,
    OUT j_data JSON
)
    BEGIN 
        SET j_data = (SELECT jso_data FROM Paint WHERE id = id_paint);
    END $$

-- Agregar Dibujos
CREATE PROCEDURE sp_addPaint(
    IN paintName VARCHAR(20), IN jso_data JSON, 
    IN id_user INT,
    OUT result BOOLEAN
)
    BEGIN 
        INSERT INTO Paint(var_name, jso_data, id_user ) VALUE (paintName, jso_data,id_user);
        SET result = 1;
    END $$

-- Actualizar dibujo

CREATE PROCEDURE sp_updatePaint(
    IN jso_data JSON, 
    IN id_paint INT,
    OUT result BOOLEAN
)
    BEGIN
        UPDATE Paint SET 
            jso_data = jso_data
            WHERE id = id_paint;
            SET result = 1;
    END $$ 

-- ELiminar un usuario
CREATE PROCEDURE sp_dropPaint(
    IN id_paint INT,
    OUT result BOOLEAN
)
    BEGIN
        DELETE FROM Paint WHERE id = id_paint;
        SET result = 1;
    END $$

DELIMITER ;

