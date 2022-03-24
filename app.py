import os
import sys
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import NO
from turtle import color, shape
import xml.etree.ElementTree as ET
from graphviz import Digraph, Graph
from Nodos import Nodo, Nuevo_Nodo
from robots import Nodo_dron, Nuevo_nodo_dron



def abrir_archivo():    
    direcion = filedialog.askopenfilename(initialdir ='/',
										title='Escoger Tu archivo de entrada',
										filetype=(('xml files', '*.xml*'),('All files', '*.*')))
    return direcion


def leerArchivo(direcion):
    global nuevalista, nuevodron
    nuevalista = Nuevo_Nodo()
    nuevodron = Nuevo_nodo_dron()
    texto = ""   
    archivo_xml = ET.parse(direcion)
    xml_data = archivo_xml.getroot()

    for i in xml_data:

        ciudades = i.findall('ciudad')
        for j in ciudades:
            texto = ""
            nombre = j.find('nombre')
            opcion1 = nuevalista.buscar(nombre.text)
            if opcion1 == False:
                filas = nombre.attrib['filas']
                columnas = nombre.attrib['columnas']

                for k in range(1 , int(filas)+1):
                    texto = texto + str(j[k].text) + '\n'


                t1 = Nodo(nombre.text, filas, columnas, texto)
                nuevalista.insertar(t1)
            else:
                filas = nombre.attrib['filas']
                columnas = nombre.attrib['columnas']

                for k in range(1 , int(filas)+1):
                    texto = texto + str(j[k].text) + '\n'

                nuevalista.editar(nombre.text, filas, columnas, texto)
                

        dron = i.findall('robot')


        for j in dron:

            nombre = j.find('nombre')
            tipo = nombre.attrib['tipo']            
            try:
                capacidad = nombre.attrib['capacidad']
            except:
                capacidad = ""
            t1=Nodo_dron(nombre.text, tipo, capacidad)
            nuevodron.insertar(t1)


def menu():
    global nuevalista, nuevodron
    print("***************************************************")
    print("*"+"           Chapín Warriors, S. A."+ "                *")
    print("*"+"           ¿Que deseas realizar?"+ "                 *")
    print("***************************************************")
    print("*"+"1. Realizar estrategía de una nueva misión"+ "       *")
    print("*"+"2. Mostrar Mapa de ciudades"+ "                      *")
    print("*"+"3. Cargar archivo de entrada"+ "                     *")
    print("*"+"4. Salir"+ "                                         *")
    print("***************************************************")
    opcion = input("Ingrese su opcion: ")
    if opcion == "1":
        print("entro")
    elif opcion == "2":
        nuevalista.imprimir()
        nuevodron.imprimir()
        menu()
    elif opcion == "3":    
        carga = abrir_archivo()
        leerArchivo(carga)
        menu()
    elif opcion == "4":
        sys.exit()
    else:
        print("Opcion no valida")
        menu()


if __name__ == "__main__":
    ROOT = Tk()    
    ROOT.withdraw()
    menu()
