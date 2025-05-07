
from dataweb import DataWeb
import pandas as pd


def main():
    # Crear una instancia de DataWeb
    dw = DataWeb()
    df = pd.DataFrame()
    df = dw.obtener_datos()
    df.to_csv("dataweb_limpios.csv")

if __name__ == "__main__":
    main()