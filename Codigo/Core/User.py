class User():
    def __init__(self,engine = None):
        self.engie = engine

    def showUser(self):
        users = self.engie.select("SELECT * FROM User ORDER BY id ASC")
        print(users)
    
    # Buscar usuario
    def loginUser(self, userName, password):
        # Comprobar si el usuario 
        query = self.engie.management('sp_login',(userName, password, None, None))
        if query[2] == 1:
            #print('Bienvenid@', userName)
            return query[3]
        elif query[2] == 0:
            print('Usuario o password incorrecto')
            return False
        else:
            print('Error en a peticion')
            return False
    
    # Agregar usuario
    def addUser(self, userName, password, typex, penColor, fillColor):
        #Comprobar si el usuario exite en la base de datos del usuario
        temp = self.engie.management('sp_searchUser',(userName, None))

        if temp[1] == 0:
            query = self.engie.management('sp_addUser',(userName,password,typex, penColor, fillColor, None))

            if query[5] > 0:
                print('Usuario ingresado con exito')
                return True

            else:
                print('ERROR al guardar')
                return False

        if temp[1] == 1:
            print('El nombre del usuario ya existe')
            return True
            
                
    #Eliminar usuario
    def dropUser(self, id):
        query = self.engie.management('sp_dropUser',(id, None))
        if query[1] == 1:
            print('Usuario eliminado con exito')
            return True
        else:
            print('ERROR al eliminar')
            return False
            
    #Modificar usuarios
    def updateUser(self,userName, password, typex, penColor, fillColor,id):
        query = self.engie.management('sp_updateUser',(userName,password,typex, penColor, fillColor, id, None))
        if query[6] == 1:
            print('Usuario actualizado con exito')
            return True
        else:
            print('ERROR al actualizar')
            return False
        
    def searchAdmin(self,user=None,password=None):
        query = self.engie.management('sp_searchAdmin',(user, password, None))
        if query[2] == 0:
            return True
        else:
            return False

    def searchUsers(self, user=None, password=None):
        query = self.engie.management('sp_searchUsers',(user, password, None))
        if query[2] == 0:
            return True
        else:
            return False