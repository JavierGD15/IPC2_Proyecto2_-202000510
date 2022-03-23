from cgitb import text
import os
import sys
from tkinter import filedialog
from tkinter.messagebox import NO
from turtle import color, shape
import xml.etree.ElementTree as ET
from graphviz import Digraph, Graph
from Nodos import Nodo, Nuevo_Nodo




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
    direcion = filedialog.askopenfilename(initialdir ='/', 
										title='Escoger Tu archivo de entrada', 
										filetype=(('xml files', '*.xml*'),('All files', '*.*')))
    archivo_xml = ET.parse(direcion)
    xml_data = archivo_xml.getroot()

    for i in xml_data:
        ciudades = i.findall('ciudad')
        for j in ciudades:
            lola = j.find('nombre')
            print(lola.text)



if __name__ == "__main__":
    
    leerArchivo()
