import pandas as pd
import sqlite3
import os



class DataBase:
    def __init__(self):
        self.rutadb = "src/edu_pad/static/db/gold_database.db"

    def guardar_df(self,df=pd.DataFrame()):
        df= df.copy()
        try:
            conn= sqlite3.connect(self.rutadb)
            df["fecha_create"] = "2025-05-05"
            df["fecha_update"] = "2025-05-05"
            df.to_sql("gold_database",conn, if_exists="replace", index=False)
            print("*********************************************")
            print("Datos Obtenidos ")
            print("*********************************************")
            print("Se guardo el DataFrame en la base de datos {}".format(df.shape))
        except Exception as errores:
            print("Error al guardar el DataFrame en la base de datos:{}".format(df.shape))

    def obtener_datos(self,nombre_tabla="gold_database"):
        try:
            conn= sqlite3.connect(self.rutadb)
            consulta= "select * from {}".format(nombre_tabla)
            df= pd.read_sql_query(consulta,conn)
            print("*********************************************")
            print("se obtuvieron los datos de la bse de datos")
            print("*********************************************")
            print("Cantidad de registros {}".format(df.shape))
            return df
        except Exception as errores:
            return df    
            print("error al obtener los datos de la tabla {str(nombre_tabla)} en base de datos {str(errores)}")   
           


       