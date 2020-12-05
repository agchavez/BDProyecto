class Paint():
    def __init__(self, idUser):
        self.idUser = idUser
        self.paints = [] #Digujos del usuario
        self.search()
        
    def search(self): #Solicitar los dibujos que pertencen al usuario
        self.paints = engie.select("""SELECT 
                                   id,var_name 
                                   FROM Paint 
                                   WHERE id_user = %s""" % self.idUser)
        
    def searchPaint(self, idPaint):
        query = engie.management('sp_searchPaint',(idPaint, None))
        if query[1]:
            return query[1]
        else:
            print('ERROR al obtener el dibujo')
            return False
        
    def addPaint(self,namePaint,data, idUser):
        query = engie.management('sp_addUser',(namePaint,data,idUser, None))
        if query[3] == 1:
            print('Dibujo ingresado con exito')
            return True

        else:
            print('ERROR al guardar')
            return False
        
    def showPaints(self):
        return self.paints
    
    def dropePaint(self, id):
        query = engie.management('sp_dropPaint',(id, None))
        if query[1] == 1:
            print('Dibujo eliminado con exito')
            return True
        else:
            print('ERROR al eliminar')
            return False
        
    def updatePaint(self,data,id):
        query = engie.management('sp_updatePaint',(data,id, None))
        if query[2] == 1:
            print('Dibujo actualizado con exito')
            return True

        else:
            print('ERROR al actualizar')
            return False 