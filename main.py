from dataweb import DataWeb
from database import DataBase
import pandas as pd


def main():
    dw = DataWeb()
    database= DataBase()
    df = dw.obtener_datos()
    df = dw.convertir_numericos(df)
    df_db = database.guardar_df(df)
    df_db2= database.obtener_datos()
    df_db2.to_csv("src/edu_pad/static/csv/data_webdb.csv", index=False)

if __name__ == "__main__":
    main()