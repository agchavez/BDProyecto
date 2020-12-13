@author agchavez@unah.hn
david.jacome@unah.hn

@date 2020/12/13

@version 1.0

# <b>Proyecto final</b> Bases de datos I

Proyecto final clase bases de datos

## Ventanas 
- ###  Ventana Login
La ventana login muestra dos campos uno para nombre del usuario y otro para la contraseña del usuario, al precionar el boton ingresar se hace un llamdo a un proceso almacenado de la base de datos A que compara si el usuario existe y la contraseña ingresada concuerda con la almacenada y retorna un True para dar acceso a la siguiente ventana.
- ### Ventana principal



## Funcionalidad 
### Clases de User
#### Agregar usuarios
- Para agregar un usuario primero se comprueba si el nombre del usuario a ingresar ya esta en la base de datos retornando un true si el usuario existe, por lo que no se agrega el usuario
- Si el usuario no existe se agrega a la base de datos retornando un true si el valor fue agregado con exito y false si hay un error al guardar

#### Eliminar Usuario
- **Parametros de entrada:** @id esta variable hace referencia al id de la tabla User
- **Retorno:** Al eliminar el usuario returna True si el valor fue eliminado y False si hay un error al eliminar 

#### Modificar Usuario 
- **Parametros de entrada:** id del usuario a modificar, nuevo nombre del usuario, nueva contraseña, nuevos colores por defecto.
- **Retorno:** True si se actualizo con exito el usuario.

### Clase dibujos
### Agregar un nuevo dibujo

## Base de datos A
Esta es la base de datos principal utilizada para el desarrollo del proyecto,

Algunas tablas cuentan con campos encriptados con el algoritmos de encriptacio AES incorporado el SGBD utilizado, para poder encriptar los datos se necesita de una contraseña usando la que utiliza el administrador para acceder al sistem.

### Tablas 
Las tablas que forman parte de esta base de datos tenemos:

#### <b>User </b>
La tabla User almacena los datos correspondientes a los usuarios tanto el administrador como el los usuarios operadores,  entre los campos que la conforman tenemos:
- El nombre del usuario no se puede repetir tiene que se unico
- Los colores por defecto en esta tabla son los que apareceran cuando el usuario inicie secion.
#### <b>Paint</b>
Almacena los datos de los dibujos de cada usurio regristrado.
- Cuenta con una relacion con la tabla usuarios y donde un usuario puede tener muchos dibujos.
- No se puede almacenar un dibujo con el mismo nombre.
- Si se elimina un usuario se eliminan todos los dibujos relacionados con id del usuario.
- Si se actualiza un dibujo, no se guardan en versiones.
#### <b>Binnacle</b> 
Almacenar cada una de las acciones de los usuarios tanto administrador como operadores, uno de los campos almacena el tipo de accion que realizo, una de las acciones es para la configuracion del color si el usuario cambia los colores por defecto automaticamente se almacenan en esta tabla.
- Nose puede eliminar ningun valor
### Procesos almacenados 
- Un proceso almacenado para agregar:
    - Usuarios 
    - Dibujos 
- Un proceso almacenado para eliminar:
  - Usuarios
  - Dibujos
- Un proceso almacenado para actualizar:
  - Usuarios 
  - Dibujos
- Un proceso almacenado para comprobar:
  - Usuarios
- Un proceso almacenado para buscar:
  - Dibujos 

### Triggers 
- Un trigger para cada vez que un usuario inicia seccion.
- Un trigger para cada insercion en la tabla Paint agrega un valor a la tabla Binnacle con la accion 'Create' y los datos de la fecha de crracion.
- Un trigger para cada eliminacion de un dibujo de la tabla Paint agrega un valor a la tabla Binnacle con la accion 'Delete' y los datos de la fecha de la eliminacion.
- Un trigger para cada actualizacion de un dibujo de la tabla Paint agrega un valor a la tabla Binnacle con la accion 'Update' y los datos de la fecha de actualizacion.

### Vistas
- Una vista para cada vez que el usuario administrador desea ver la bitacora de todos los usuarios en el sistema.

## Base de datos B

Base de datos secundaria utilizada como respaldo pero tambien como control de versiones de esta forma se tiene un mejor control y manejo de errores que se puedan presentar en la 
base de datos principal.

Al utilizar archivos compresos tenemos un mayor rango de espacio disponible en comparacion a la base de datos A que los almacena sin comprimirlos.

Cada version del dibujo esta identificada por un numero que identifica cual es la primera y la mas reciente, tambien se tiene una fecha de creacion de cada version del dibujo 
estos datos almacenados en la bitacora, al realizar la consulta desde python para poder descargar la ultima version del dibujo guardada se obtiene la ultima version del dibujo.
### Procesos almacenados 

- Un proceso almacenado para agregar:
    - Usuarios 
    - Dibujos