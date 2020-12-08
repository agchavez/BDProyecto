import mysql.connector
import json
import gzip
#-*-coding:utf8-*-

class UserBDB():
    def __init__(self, engine = None):
        self.engie = engine
    # Agregar usuario
    def addUser(self, userName, password, typex, penColor, fillColor):
        query = self.engie.management('sp_addUser',(userName,password,typex, penColor, fillColor,'admin', None))
        if(query[6] > 0):
            print('usuario agregado en la base de respaldo')
        else:
            print('error base de datos de respaldo')

class paintBDB():
    def __init__(self, engine = None):
        self.engie = engine
        
    def search(self,namePaint,idUser): #Solicitar los dibujos que pertencen al usuario
        self.paints = self.engie.select("""SELECT 
                                        CAST(AES_DECRYPT(blob_data,'admin')AS CHAR) 
                                    FROM
                                        Paint
                                    WHERE 
                                        id_user = %s AND CAST(AES_DECRYPT(blob_name ,'admin')AS CHAR) = '%s'
                                    ;""" % (idUser,namePaint))
        return self.paints
                                   
    def addPaint(self,namePaint,data,idUser,adminPass= 'admin'):
        compress_data = self.compress_data(data)
        temp = compress_data.hex()
        query = self.engie.management('sp_addPaint',(namePaint,temp,idUser,'admin', None))
        if query[4] > 0:
            print('Dibujo ingresado con exito')
            return True

        else:
            print('ERROR al guardar')
            return False
        print(temp)
        
        
    def compress_data(self, data):
        json_data = json.dumps(data,indent=1)
        enconde = json_data.encode('utf-8')
        compressd = gzip.compress(enconde)
        return compressd
    
    def decompress_data(self, data):
        return gzip.decompress(data)
    
    def showPaints(self,idUser,namePaint):
        temp = self.search(namePaint,idUser)
        paint = self.decompress_data(bytes.fromhex(temp[-1][0])).decode()
        return (True,paint)
        