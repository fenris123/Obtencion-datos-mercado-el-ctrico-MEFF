# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 12:03:35 2025

@author: fenris123
"""

import pandas as pd
import datetime


def obtener_MEFF():

# PASO 0 (OPCIONAL) imprimir un mensaje que recuerde que los datos de MEFF pueden cambiar cada dia.
    
    fecha_actual = datetime.datetime.now().strftime("%d-%b-%Y")
    print(f"Atención: los datos de MEFF obtenidos son válidos a fecha {fecha_actual}")



#PASO 1:  panda lee la tabla de la web, y la mete en un df

    url = "https://www.meff.es/esp/Derivados-Commodities/Precios-Cierre"
    tablas = pd.read_html(url)
    df = tablas [0]



# PASO 2:  limpiamos el DF para quedarnos solo con fecha y precio.

    df.columns = df.columns.droplevel(0)
    df = df.rename(columns={"Unnamed: 0_level_1": "fecha"})
    df = df.iloc[:, [0, 2]]



# PASO 3: Al cargar la tabla, los datos decimales de precios venian con ",".  Pandas ha eliminado esas comas.
# EJEMPLO.  19,20 lo ha transformado en 1920.   Para solucionarlo, dividiremos por 100.

    df[["Precio"]] = df[["Precio"]]/100

    return df




