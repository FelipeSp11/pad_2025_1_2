
from dataweb import DataWeb
import pandas as pd


def main():
    dw = DataWeb()
    df = dw.obtener_datos()
    df = dw.convertir_numericos(df)
    df.to_csv("dataweb_limpios.csv", index=False)

if __name__ == "__main__":
    main()