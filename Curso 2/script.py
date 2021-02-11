#!/usr/bin/env python3
#Tengo que darle permiso de ejecucion a el archivo, de la siguiente manera en linux chmod +x Modulo_Pil.py
#Este Scripr me dira el porcentaje que uso de mi Disco Duro y Procesador
#Para ejecutarlo lo hago asi: ./script.py

import shutil
import psutil

def disco_usado(disco):
    disco = shutil.disk_usage(disco)
    libre = disco.free/disco.total*100
    #Esta funcion me dice que queda libre {libre} este porcentaje
    return libre>20

def chequear_cpu_usado():
    usado = psutil.cpu_percent(1)
    #Esta duncion me dice que procentaje uso el procesador
    return usado<75

def chequear():
    if not disco_usado("/") or not chequear_cpu_usado():
        print("ERROr!")
    else:
        print("Todo Bien")


chequear()