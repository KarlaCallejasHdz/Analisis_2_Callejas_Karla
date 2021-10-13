#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 11:34:40 2021

@author: pcc
"""

import csv 
from collections import Counter #contador 
import pandas as pd #para implementar la tabulacion
#register_id,direction,origin,destination,year,
#date,product,transport_mode,company_name,total_value
with open('synergy_logistics_database.csv') as archivo: #abriendo el archivo que contiene los datos de la bd
    lista = []
    lista_medios = []
    totales = [] #Lista que contiene todos los datos
    lector = csv.reader(archivo) #lectura del archivo con la funcion reader

    for linea in lector: #iterando en el archivo para agregarlo a una lista
         totales.append(linea)
    #funcion que opera para la opcion 1
    def rutas():
        for linea in totales:
            lista.append(linea[2:3])
        mayores = []
        i = 0
        columna = [fila[i] for fila in lista]
        mas = Counter(columna)
        mas1 = mas.most_common()
        mb = pd.DataFrame(mas1, columns = ['Ruta','Cantidad']) #para tabular el contenido de la matriz
        for x in range(len(mb)):
            if x < 11:
                mayores.append(mas1[x])
        mayores_b = pd.DataFrame(mayores, columns = ['Ruta','Cantidad']) #para tabular el contenido de la matriz
        print("""
              Listado con las rutas de importacion y exportacion mas demandados
              """)
        print(mayores_b)
    rutas();
    
    
    #______________________________________________________________________________________________________________
    #funcion que opera para la opcion 2
    #MEDIOS DE TRASPORTE
    def medios():
        for linea in totales:
             lista_medios.append(linea[7:8]) #agregando los medios de transporte a una lista
        medios = []
        menor_ruta = []
        m = 0
        columna_medio = [fil[m] for fil in lista_medios] #fila en que se va a iterar
        mas_m = Counter(columna_medio)
        mas1_m = mas_m.most_common()
        mb_m = pd.DataFrame(mas1_m, columns = ['Medio','Cantidad']) #para tabular el contenido de la matriz
        
        for y in range(len(mb_m)): #para optener los 3 medios de transporte mas utilizados
            if y < 3:
                medios.append(mas1_m[y])
            else:
                menor_ruta.append(mas1_m[y]) # la menor ruta
        mayores_m = pd.DataFrame(medios, columns = ['Transporte','Cantidad']) #para tabular el contenido de la matriz
        
        print("""
              Listado con los transportes de importacion y exportacion mas demandados
              """)
        print(mayores_m)
        menor_ruta.pop(1)
        menor_m = pd.DataFrame(menor_ruta, columns = ['Transporte','Cantidad']) #para tabular el contenido de la matriz
        
        print("""
             Transporte menos utilizado
              """)
        print(menor_m)
    medios()
    #_______________________________________________________________________-
    #funcion que opera para la opcion 3
    #valor total de importaciones y exportaciones que general màs del 80% del
    #valor total 
    
    def promedio():
        paises = []       
        total_valor = 0
        datos_paises = []
        porcentajes = []
        val_act = 0
        for linea in totales:
            pais = [linea[2] , linea[9]] # se extrae el pais y su valor total
            
            paises.append(pais) #agregando a una nueva lista los valores
        paises.pop(0) # eliminando encabezado
        
        for linea in paises:
            total_valor += int(linea[1]) #se calcula el valor total de imp y exp
        for p in paises:
            val_act += int(p[1])
            porcentaje_actual = round(val_act / total_valor, 3)
            datos_paises.append(p)
            porcentajes.append(porcentaje_actual)
            if porcentaje_actual <= (0.8):
                continue
            else:
                if porcentaje_actual - (0.8) <= porcentajes[-2] - (0.8):
                    break
                else:
                    datos_paises.pop(-1)
                    porcentajes.pop(-1)
        #print(paises[0:9])
        #print(total_valor)
        #print(porcentajes[1:])
    promedio()