class Paint():
    def __init__(self,engine):
        self.engine = engine
        self.paints = [] #Digujos del usuario
        #self.search()
        
    def search(self, id = None): #Solicitar los dibujos que pertencen al usuario
        self.paints = self.engine.select("""SELECT 
                                   id, CAST(AES_DECRYPT(var_name,'admin')AS CHAR)
                                   FROM Paint 
                                   WHERE id_user = %s""" % id)
        return self.paints
        
    def searchPaint(self, idPaint):
        query = self.engine.management('sp_searchPaint',(idPaint, None))
        if query[1]:
            return query[1]
        else:
            print('ERROR al obtener el dibujo')
            return False
        
    def addPaint(self,namePaint, data, idUser):
        query = self.engine.management('sp_addPaint',(namePaint,data,idUser, None))
        if query[3] == 1:
            print('Dibujo ingresado con exito')
            return True

        else:
            print('ERROR al guardar')
            return False
        
    def showPaints(self):
        return self.paints
    
    def dropePaint(self, id):
        query = self.engine.management('sp_dropPaint',(id, None))
        if query[1] == 1:
            print('Dibujo eliminado con exito')
            return True
        else:
            print('ERROR al eliminar')
            return False
        
    def updatePaint(self,data,id):
        query = self.engine.management('sp_updatePaint',(data,id, None))
        if query[2] == 1:
            print('Dibujo actualizado con exito')
            return True

        else:
            print('ERROR al actualizar')
            return False 

    def searchPaints(self,userId):
        query = self.engine.management('sp_searchPaints',(userId, None,None))
        if query[1] == 1:
            print(query[1])
            print(query[2])
            return query[2]
        else:
            print('ERROR al eliminar')
            return False