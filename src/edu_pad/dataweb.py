import pandas as pd
import requests
from bs4 import BeautifulSoup
import datetime



class DataWeb:
    def __init__(self):
        self.url="https://finance.yahoo.com/quote/GC%3DF/history/"


    def obtener_datos(self):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0'

            }
            respuesta = requests.get(self.url, headers=headers)
            if respuesta.status_code != 200:
                print(f"Error al obtener la página: {respuesta.status_code}")
            #print(respuesta.text)
            soup = BeautifulSoup(respuesta.text, 'html.parser')
            tabla = soup.select_one('div[data-testid="history-table"] table')
            print(tabla)


            
        except Exception as err:
            print(f"Error al obtener los datos")               







dw=DataWeb()
dw.obtener_datos()
#print(dw.url)
