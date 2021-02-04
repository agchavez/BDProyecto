# -*- coding: utf-8 -*-
"""
    @author: david.jacome@unah.hn
"""


"""
    Crea la ventana de dibujo
    @self.paints: Dibujos del usuario
    @self.engine: Es la conexión con la base de datos
"""
class Paint():
    def __init__(self,engine):
        self.engine = engine
        self.paints = []
        
    """
        Solicita los dibujos que pertenecen al usuario
        @self.paints: modifica el arreglo del constructor ya con los dibujos que pertenecen al usuario
    """
    def search(self, id = None): 
        self.paints = self.engine.select("""SELECT 
                                   id, CAST(AES_DECRYPT(var_name,'admin')AS CHAR)
                                   FROM Paint 
                                   WHERE id_user = %s""" % id)
        return self.paints
        
    """
        Retorna el json del dibujo si se encontró en la DB, si no retorna False
    """
    def searchPaint(self, idPaint):
        query = self.engine.management('sp_searchPaint',(idPaint, None))
        if query[1]:
            return query[1]
        else:
            print('ERROR al obtener el dibujo')
            return False
        
    """
        Retorna True, si el dibujo se ingresó correctamente en la DB
        @namePaint: nombre del dibujo
        @data: el json del dibujo
        @idUser: el id del usuario al que pertenece dicho dibujo
    """
    def addPaint(self,namePaint, data, idUser):
        query = self.engine.management('sp_addPaint',(namePaint,data,idUser, None))
        if query[3] == 1:
            print('Dibujo ingresado con exito')
            return True

        else:
            print('ERROR al guardar')
            return 
            
    """
       retorna los dibujos encontrados 
    """    
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
    
    """
        @id: id del dibujo
    """
    def searchPaintName(self, namePaint, idUser):
        query = self.engine.management('sp_searchPaintName',(idUser,namePaint, None, None))
        temp = (True,query[3])
        if query[2] == 1:
            return temp
        else:
            return (False,0)

    def updatePaint(self,data,id):
        print(id)
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