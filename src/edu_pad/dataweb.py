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
            nombre_columnas = [th.get_text(strip=True) for th in tabla.thead.find_all('th')]
            filas = []
            for tr in tabla.tbody.find_all('tr'):
                columna=[td.get_text(strip=True) for td in tr.find_all('td')]
                if len(columna) == len(nombre_columnas):
                    filas.append(columna)            
            df = pd.DataFrame(filas, columns=nombre_columnas).rename(columns={
                'Date': 'date',
                'Open': 'open',
                'High': 'high',
                'Low': 'low',
                'CloseClose price adjusted for splits.': 'close',
                'Adj CloseAdjusted close price adjusted for splits and dividend and/or capital gain distributions.': 'adj_close',
                'Volume': 'volume'
            })
            df = self.convertir_numericos(df)
            df.to_excel("dataweb_limpios.xlsx", index=False)
            
            #print(nombre_columnas)
            #print(filas)


            
        except Exception as err:
            print(f"Error al obtener los datos")               




    def convertir_numericos(self,df=pd.DataFrame()):
        df=df.copy()
        if len(df)>0:
           for col in('date','open','high','low','close','adj_close','volume'):
               df[col]=(
                   df[col].str.replace(',','')
                   .str.replace('$','') 
                   
               )
        return df

                  


#dw=DataWeb()
#dw.obtener_datos()
#print(dw.url)
