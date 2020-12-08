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
        return self.link.fetchall()
    
    def management(self, sp, arg):
        temp = self.link.callproc(sp, arg)
        self.commit()
        return temp
        
    def commit(self):
        self.con.commit()