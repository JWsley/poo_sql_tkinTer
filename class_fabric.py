from class_info import *

import mysql.connector
class Fabric:
    def __init__(self):
        self.con = mysql.connector.connect(
            host = 'LocalHost',
            user = 'root',
            password = 'q1w2e3',
            database = 'estoque'

        )
        self.curs = self.con.cursor()
        self.nomEmpr = []
        


    def cadastro_fabric(self):
        print("|■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■|")
    

        nomEmp = input('Informe o nome de sua empresa:')
        
        sql_command = f'insert into fabricante (nomeFabri) values ("{nomEmp}")' 
        self.nomEmpr.append(nomEmp)
        self.curs.execute(sql_command)
        self.con.commit()
        print('Empresa cadastrada com Sucesso!!!')
        print("|■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■|")
        
        
        
