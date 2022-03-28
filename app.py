import os
import sys
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import NO
from tracemalloc import stop
from turtle import color, shape
import xml.etree.ElementTree as ET
from graphviz import Digraph, Graph
from Nodos import Nodo, Nuevo_Nodo
from robots import Nodo_dron, Nuevo_nodo_dron
from matriz import Matriz_nodo, Nuevo_mapa
from guerreros import Nodo_guerra, Nuevo_Nodo_guerra
from Rescate import Nuevo_rescate
from extraccion import Nueva_extraccion
from imprimir_mapa import mapas



def abrir_archivo():    
    direcion = filedialog.askopenfilename(initialdir ='/',
										title='Escoger Tu archivo de entrada',
										filetype=(('xml files', '*.xml*'),('All files', '*.*')))
    return direcion


def leerArchivo(direcion):
    global nuevalista, nuevodron,Nuevo_guerrero
    nuevalista = Nuevo_Nodo()
    nuevodron = Nuevo_nodo_dron()
    Nuevo_guerrero = Nuevo_Nodo_guerra()
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
                    texto = texto + str(j[k].text) 
                   
                x =0
                ayuda = ""
                try:
                    while True:
                        ayuda =j[x].text
                        x = x+1
                except:
                    stop
                
                for k in range(int(filas)+1 , x):
                    
                    t2 = Nodo_guerra(nombre.text,j[k].attrib['fila'],j[k].attrib['columna'],j[k].text)
                    Nuevo_guerrero.insertar(t2)  
                 
                x = 0                  
                 
        
                
                t1 = Nodo(nombre.text, filas, columnas, texto)
                nuevalista.insertar(t1)
            else:
                filas = nombre.attrib['filas']
                columnas = nombre.attrib['columnas']

                for k in range(1 , int(filas)+1):
                    texto = texto + str(j[k].text) 
                    

                nuevalista.editar(nombre.text, filas, columnas, texto)
                

        dron = i.findall('robot')


        for j in dron:

            nombre = j.find('nombre')
            nuevodron.buscar(nombre.text)

            if nuevodron.buscar(nombre.text) == True:
                tipo = nombre.attrib['tipo']                                          
                try:
                    capacidad = nombre.attrib['capacidad']
                except:
                    capacidad = ""
                nuevodron.editar(nombre.text,tipo,capacidad)            
            else:
                tipo = nombre.attrib['tipo']            
                try:
                    capacidad = nombre.attrib['capacidad']
                except:
                    capacidad = ""
                t1=Nodo_dron(nombre.text, tipo, capacidad)
                nuevodron.insertar(t1)




def menu():
    global nuevalista, nuevodron,Nuevo_guerrero
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
        opcion = input("Ingrese R si desea elaborar un rescate o E si desea una extracción de recursos: ")
        if opcion == "R":
            mision_rescate()
        elif opcion == "E":
            mision_extraccion()
        else:
            print("Opcion no valida")
            menu()
    elif opcion == "2":
        print("Las ciudades disponibles son: ")
        nuevalista.imprimir()
        opcion = input("Ingrese el nombre de la ciudad que desea visualizar: ")
        llenado_lista(opcion)
                    

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

def mision_rescate():
    global nuevalista, nuevodron,Nuevo_guerrero,matriz
    rescate = Nuevo_rescate()
    print("***************************************************")
    print("*"+"           Verificando existencia de ChapinRescue..."+ "                *")
    op = nuevodron.verificar()
    if op == True:
        print("Los drones disponibles son: ")
        nuevodron.imprimir(False)
        opcion = input("Ingrese el nombre del drone que desea utilizar: ")
        aux = nuevodron.buscar(opcion)
        if aux != False:
            print("Las ciudades disponibles son: ")
            nuevalista.imprimir()
            opcion = input("Ingrese el nombre de la ciudad que desea rescatar: ")
            aux56 = nuevalista.mostrar(opcion)
            print(aux56.fila, aux56.columna)
            llenado_lista(opcion)
            print("La ciudad seleccionada es la siguiente: ")
            entradas =matriz.buscar_color(int(aux56.fila),int(aux56.columna),"azul")
            if entradas > 0:
                print("Si hay unidades civiles en la ciudad seleccionada, se rescataran")
                if entradas > 1:
                    civilesX = input("Ingrese la coordenada Y de la unidad civil a rescatar: ")
                    civilesY = input("Ingrese la coordenada X de la unidad civil a rescatar: ")
                    entradas =matriz.buscar_color(int(aux56.fila),int(aux56.columna),"verde")
                    if entradas > 1:
                        coordenadaX = input("Ingrese la coordenadas en Y de su punto de entrada: ")
                        coordenadaY = input("Ingrese la coordenadas en X de su punto de entrada: ")
                        mat = matriz.buscar_coordenadas(1,1)
                        rescate.realizar_mision(int(civilesX),int(civilesY),int(coordenadaX),int(coordenadaY), mat) 
                    else:
                        mat = matriz.buscar_coordenadas(1,1)
                        coordenadamatriz = matriz.buscar_color_coordenada(int(aux56.fila),int(aux56.columna),"verde")
                        rescate.realizar_mision(int(civilesX),int(civilesY),int(coordenadamatriz.x),int(coordenadamatriz.y) , mat)
                
                else:
                    mat = matriz.buscar_coordenadas(1,1)
                    civilesX1 = matriz.buscar_color_coordenada(int(aux56.fila),int(aux56.columna),"azul")                    
                    if len(entradas) > 1:
                        coordenadaX = input("Ingrese la coordenadas en Y de su punto de entrada: ")
                        coordenadaY = input("Ingrese la coordenadas en X de su punto de entrada: ")
                        rescate.realizar_mision(int(civilesX1),int(civilesX1),int(coordenadaX),int(coordenadaY), mat)
                    else:
                        coordenadamatriz = matriz.buscar_color_coordenada(aux56.fila,aux56.columna,"verde")
                        rescate.realizar_mision(int(civilesX1),int(civilesX1),int(coordenadamatriz.x),int(coordenadamatriz.y), mat)
                        
                    
                    
                
            else:
                print("No hay unidades civiles en la ciudad seleccionada")
                menu()


        else:
            print("No existe este dron")
            menu()
    else:
        print("No existen drones disponibles")
        menu()
    menu()

def mision_extraccion():
    print("***************************************************")
    global nuevalista, nuevodron,Nuevo_guerrero,matriz
    rescate = Nueva_extraccion()
    print("***************************************************")
    print("*"+"           Verificando existencia de ChapinFighter..."+ "                *")
    op = nuevodron.verificar_tipo()
    if op == True:
        print("Los drones disponibles son: ")
        nuevodron.imprimir(True)
        opcion = input("Ingrese el nombre del drone que desea utilizar: ")
        aux = nuevodron.buscar(opcion)
        if aux != False:
            print("Las ciudades disponibles son: ")
            nuevalista.imprimir()
            opcion = input("Ingrese el nombre de la ciudad que desea Recoger recursos: ")
            aux56 = nuevalista.mostrar(opcion)
            print(aux56.fila, aux56.columna)
            llenado_lista(opcion)
            print("La ciudad seleccionada es la siguiente: ")
            entradas =matriz.buscar_color(int(aux56.fila),int(aux56.columna),"gris")
            if entradas > 0:
                print("Si hay Recursos en la ciudad seleccionada, se recogeran")
                entradas =matriz.buscar_color(int(aux56.fila),int(aux56.columna),"gris")
                if entradas > 1:
                    civilesX = input("Ingrese la coordenada Y de la unidad de recursos: ")
                    civilesY = input("Ingrese la coordenada X de la unidad de recursos: ")
                    entradas =matriz.buscar_color(int(aux56.fila),int(aux56.columna),"verde")
                    if entradas > 1:
                        coordenadaX = input("Ingrese la coordenadas en Y de su punto de entrada: ")
                        coordenadaY = input("Ingrese la coordenadas en X de su punto de entrada: ")
                        mat = matriz.buscar_coordenadas(1,1)
                        rescate.realizar_mision(int(civilesX),int(civilesY),int(coordenadaX),int(coordenadaY), mat, int(aux.capacidad)) 
                    else:
                        mat = matriz.buscar_coordenadas(1,1)
                        coordenadamatriz = matriz.buscar_color_coordenada(int(aux56.fila),int(aux56.columna),"verde")
                        rescate.realizar_mision(int(civilesX),int(civilesY),int(coordenadamatriz.x),int(coordenadamatriz.y) , mat, int(aux.capacidad))
                
                else:
                    mat = matriz.buscar_coordenadas(1,1)
                    civilesX1 = matriz.buscar_color_coordenada(int(aux56.fila),int(aux56.columna),"gris")                    
                    if len(entradas) > 1:
                        coordenadaX = input("Ingrese la coordenadas en Y de su punto de entrada: ")
                        coordenadaY = input("Ingrese la coordenadas en X de su punto de entrada: ")
                        rescate.realizar_mision(int(civilesX1),int(civilesX1),int(coordenadaX),int(coordenadaY), mat, int(aux.capacidad))
                    else:
                        coordenadamatriz = matriz.buscar_color_coordenada(aux56.fila,aux56.columna,"verde")
                        rescate.realizar_mision(int(civilesX1),int(civilesX1),int(coordenadamatriz.x),int(coordenadamatriz.y), mat, int(aux.capacidad))
                        
                    
                    
                
            else:
                print("No hay unidades civiles en la ciudad seleccionada")
                menu()


        else:
            print("No existe este dron")
            menu()
    else:
        print("No existen drones disponibles")
        menu()
    menu()
    
def llenado_lista(opcion):
    global nuevalista, nuevodron,Nuevo_guerrero,matriz
    aux = nuevalista.mostrar(opcion)
    if aux != False:
            matriz = Nuevo_mapa()
            matriz.reiniciaraiz()
            matriz.llenar_matriz(int(aux.fila),int(aux.columna))
            matriz.unir_nodos(int(aux.fila),int(aux.columna))
            matriz.borrar_derecha(int(aux.fila),int(aux.columna))
            matriz.llenar_colores(aux.filatexto,int(aux.fila),int(aux.columna))
            
            
            ayuda = Nuevo_guerrero.devolver()
            
            while ayuda != None:
                if ayuda.nombre == opcion:
                    matriz.editar_coordenadas_robot(int(ayuda.fila),int(ayuda.columna),"rojo",int(ayuda.valor))
                    ayuda = ayuda.siguiente
                else:
                    ayuda = ayuda.siguiente
            matriz.imprimir_total(int(aux.fila),int(aux.columna)) 
    else:
        print("No existe esa ciudad")
        menu()

if __name__ == "__main__":
    ROOT = Tk()    
    ROOT.withdraw()
    menu()
    #leerArchivo("Entrada_Ejemplo.xml")
