DROP DATABASE IF EXISTS Proyecto;
CREATE DATABASE Proyecto CHARACTER SET utf8;

USE Proyecto;

CREATE TABLE IF NOT EXISTS User(
    id INT AUTO_INCREMENT PRIMARY KEY,
    var_userName VARCHAR(20) NOT NULL COMMENT "id de la tabla de User",
    var_password VARCHAR(20) NOT NULL COMMENT "Contraseña de usuario",
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
        tex_action TEXT NOT NULL COMMENT "Acción que realiza el usuario ya sea operador o administrador",
        id_user INT NOT NULL COMMENT "Llave foranéa de la tabla de User",
        FOREIGN KEY (id_user) REFERENCES User(id) ON DELETE CASCADE ON UPDATE CASCADE
)COMMENT "Descripción de la tabla  de bitacora(Binnacle) con sus respectivos campos";

CREATE TABLE IF NOT EXISTS Color(
    id INT AUTO_INCREMENT PRIMARY KEY,
    var_fillColor VARCHAR(7) NOT NULL COMMENT "Color de fondo hexadecimal",
    var_penColor VARCHAR(7) NOT NULL COMMENT "Color de lápiz decimal",
    id_user INT NOT NULL UNIQUE COMMENT "llave foranéa de la tabla de User",
    FOREIGN KEY (id_user) REFERENCES User(id) ON DELETE CASCADE ON UPDATE CASCADE
)COMMENT "Descripción de la tabla color con sus respectivos campos";