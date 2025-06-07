from src.edu_pad.dataweb import DataWeb
import pandas as pd

def main():
    dw = DataWeb()
    df = dw.obtener_datos()
    df = dw.convertir_numericos(df)
    df.to_csv("src/edu_pad/static/csv/data_webdb.csv", index=False)

if __name__ == "__main__":
    main()
