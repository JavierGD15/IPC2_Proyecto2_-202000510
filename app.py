from asyncio.windows_events import NULL
from cgitb import text
import os
import sys
from tkinter import filedialog
from tkinter.messagebox import NO
from turtle import color, shape
import xml.etree.ElementTree as ET
from graphviz import Digraph, Graph
from Nodos import Nodo, Nuevo_Nodo
from robots import Nodo_dron, Nuevo_nodo_dron





def opciones():
    global nuevalista, nuevopatron

    print("***************************************************")
    print("*"+"           Chapín Warriors, S. A."+ "                *")
    print("*"+" Hola, elijamos nuestro archivo de entrada"+ "       *")
    print("***************************************************")
    leerArchivo()
    menu()



def leerArchivo():
    global nuevalista, nuevopatron
    texto = ""
    nuevalista = Nuevo_Nodo()
    nuevodron = Nuevo_nodo_dron()
    direcion = filedialog.askopenfilename(initialdir ='/',
										title='Escoger Tu archivo de entrada',
										filetype=(('xml files', '*.xml*'),('All files', '*.*')))
    archivo_xml = ET.parse(direcion)
    xml_data = archivo_xml.getroot()

    for i in xml_data:

        ciudades = i.findall('ciudad')
        for j in ciudades:
            texto = ""
            nombre = j.find('nombre')
            filas = nombre.attrib['filas']
            columnas = nombre.attrib['columnas']

            for k in range(1 , int(filas)+1):
                texto = texto + str(j[k].text) + '\n'


            t1 = Nodo(nombre, filas, columnas, texto)
            nuevalista.insertar(t1)

        dron = i.findall('robot')


        for j in dron:

            nombre = j.find('nombre')
            
            tipo = nombre.attrib['tipo']
            try:
                capacidad = nombre.attrib['capacidad']
            except:
                capacidad = ""
            t1 = Nodo_dron(nombre.text, tipo, capacidad)
            nuevodron.insertar(t1)

    
    nuevalista.imprimir()
    nuevodron.imprimir()



if __name__ == "__main__":

    leerArchivo()
