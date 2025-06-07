from src.edu_pad.database import DataBase
import pandas as pd


def main():
    database= DataBase()
    df_db = database.guardar_df(df)
    df= pd.read_csv("src/edu_pad/static/csv/data_webdb.csv", index=False)
    df_db= database.obtener_datos()
    

if __name__ == "__main__":
    main()