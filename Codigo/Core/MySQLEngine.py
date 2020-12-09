import mysql.connector
#from Core.ConnectionConfig import *

class MySQLEngine:
    def __init__(self, config = {}):
        print(config['server'])
        self.server = config['server']
        self.port = config['port']
        self.user = config['user']
        self.password = config['password']
        self.database = config['database']
        self.start()
        
    def start(self):
        self.con = mysql.connector.connect(
            host = self.server,
            port = self.port,
            user = self.user,
            password = self.password,
            database = self.database
        )

        #Version del texto
        self.link = self.con.cursor()
    
    def select(self, query):
        self.link.execute(query)
        temp = self.link.fetchall()
        #self.link.close()
        return temp
    
    def management(self, sp, arg):
        temp = self.link.callproc(sp, arg)
        self.commit()
        #self.link.close()
        return temp
        
    def commit(self):
        self.con.commit()

    #No se debe cerrar la coneccion en los select si no que despues de la consulta
    def closeConnection(self):
        self.link.close()