class ColorConf():
    def __init__(self, engie=None):
        self.engie = engie

    #Agregar la configuracion de los colores en la BD
    def addBinnacle(self, id, pencolor, filcolor):
        self.engie.management('sp_ColorConfig',(id, pencolor, filcolor))
    
    def searchColor(self, id):
        return self.engie.select("SELECT DISTINCT CAST(AES_DECRYPT(var_fillColor,'admin')AS CHAR), CAST(AES_DECRYPT(var_penColor,'admin')AS CHAR) FROM User WHERE id = %s" % id)
        