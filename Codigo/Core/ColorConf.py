class ColorConf():

    def __init__(self, engie=None):
        self.engie = engie

    #Agregar la configuracion de los colores en la BD
    def addBinnacle(self, id, pencolor, filcolor):
        self.engie.management('sp_ColorConfig',(id, pencolor, filcolor))
    
    def searchColor(self, id):
        return self.engie.select("SELECT var_fillColor, var_penColor FROM User WHERE id = %s" % id)
        