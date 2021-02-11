#!/usr/bin/env python3
#Tengo que darle permiso de ejecucion a el archivo, de la siguiente manera en linux chmod +x Modulo_Pil.py

#Para ejecutarlo lo hago asi: ./Modulo_PIL.py



#Modulo Pil para imagenes
import PIL.Image
image = PIL.Image.open("bici.jpg")
print(image.size)

#modulo Pandas para analisis de Datos

import pandas
visitante=[1235,6424,9254,4181,4857]
errores=[23,54,22,43,432]

df = pandas.DataFrame({"Visitantes":visitante,"Errores":errores},index=["Lunes","Martes","Miercoles","Jueves","Viernes"])
print(df)