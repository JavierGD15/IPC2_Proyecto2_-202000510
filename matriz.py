from graphviz import Digraph, Graph
import collections
import re
from turtle import pen


class Matriz_nodo:
    def __init__(self, x = None, y = None, izquierda = None, derecha = None, arriba = None, abajo = None, color = None):
        self.x = x
        self.y = y
        self.izquierda = izquierda
        self.derecha = derecha
        self.arriba = arriba
        self.abajo = abajo
        self.color = color

class Nuevo_mapa:
    def __init__(self):
        self.raiz = Matriz_nodo()
        self.ultimo = Matriz_nodo()
    

    #Funciones de llenado de matriz
    def reiniciaraiz(self):

        self.raiz = Matriz_nodo()
        self.ultimo = Matriz_nodo()

    def insertar(self, nuevoNodo):
        global x,y
        
        if self.raiz.x == None:
            
            self.raiz = nuevoNodo
            self.ultimo = nuevoNodo


        elif self.raiz.derecha == None:
            
            self.raiz.derecha = nuevoNodo
            self.ultimo = nuevoNodo
        else:
            
            self.ultimo.derecha = nuevoNodo
            self.ultimo = nuevoNodo
        

    
    def imprimir(self):
        try:
            aux = self.raiz
            
            while aux != None:
                print("Nodo",aux.x, aux.y,"Derecha" ,aux.derecha.x, aux.derecha.y,"Izquierda",aux.izquierda.x, aux.izquierda.y,"Abajo",aux.abajo.x, aux.abajo.y,"Arriba",aux.arriba.x, aux.arriba.y)
                aux = aux.derecha
        except:
            print("No hay nodos")

    def llenar_matriz(self,filas, columnas):
        Nuevo_mapa()
        for i in range(1,filas+1):
            for j in range(1,columnas+1):
                self.insertar(Matriz_nodo(i,j))

    def buscar(self, x1,y1):
        aux3 = self.raiz
        while aux3 != None:
            if aux3.x == x1 and aux3.y == y1:
                return aux3
            aux3 = aux3.derecha
    
    def borrar_derecha(self,filas, columnas):
        for i in range(1,filas+1):
            
            aux = self.buscar(i,columnas)
            if aux== None:
                break
            else:
                aux.derecha = None       
           
    
    def unir_nodos(self,filas, columnas):
        
        for i in range(1,filas+1):
            for j in range(1,columnas+1):
                
                aux = self.buscar(i,j)
                
                if j-1 >= 0:
                    aux.izquierda = self.buscar(i,j-1)
               
                if i+1 <= filas:                    
                    aux.abajo = self.buscar(i+1,j)   
                    
                    
                if i-1 >= 1:
                    aux.arriba = self.buscar(i-1,j)
                

    #funciones de tablero

    def buscar_coordenadas(self,x2,y2):
        aux = self.raiz
        

        for j in range(1,y2):
            
            aux = aux.derecha
        for i in range(1,x2):
            aux = aux.abajo
        return aux

    def editar_coordenadas(self,fila,columna,color):        
        aux = self.buscar_coordenadas(fila,columna)
        aux.color = color
    
    def llenar_colores(self,cadena,fila1,columna1):
        
        columna = 1
        fila = 1
        for i in cadena:
            
            try:            
                if i != "\n":
                    if columna == columna1:                          
                        
                        if i == "*":       
                                    
                            self.editar_coordenadas(int(fila),int(columna),"negro")
                            fila = fila+1
                            columna = 1
                        

                        elif i == "E":
                            
                            self.editar_coordenadas(int(fila),int(columna),"verde") 
                            fila = fila+1
                            columna = 1
                        elif i == '"':
                            continue

                        elif i == "C":
                            
                            self.editar_coordenadas(int(fila),int(columna),"azul") 
                            fila = fila+1
                            columna = 1
                        elif i == "R":
                            
                            self.editar_coordenadas(int(fila),int(columna),"gris")
                            fila = fila+1
                            columna = 1
                        else:                        
                            self.editar_coordenadas(int(fila),int(columna),"blanco")
                            fila = fila+1
                            columna = 1
                    elif fila > fila1:
                        break
                    elif i == "*":       
                                
                        self.editar_coordenadas(int(fila),int(columna),"negro")
                        columna = columna+1
                    
                    elif i == '"':
                            continue

                    elif i == "E":
                        
                        self.editar_coordenadas(int(fila),int(columna),"verde") 
                        columna = columna+1

                    elif i == "C":
                        
                        self.editar_coordenadas(int(fila),int(columna),"azul") 
                        columna = columna+1
                    elif i == "R":
                        
                        self.editar_coordenadas(int(fila),int(columna),"gris")
                        columna = columna+1
                    else:
                        
                        self.editar_coordenadas(int(fila),int(columna),"blanco")
                        columna = columna+1
                
                else:
                    
                    fila = fila+1
                    columna = 1
            except:
                print("Error", fila, columna)
                break


    def imprimir_total(self,filas, columnas):
                
        x = ""
        y = ""
        tr_inicio = '''<TR>'''
        tr_fin = '''</TR>'''
        cuerpo = ""


        dot = Digraph(filename='Mapa', format= 'png')

        for i in range(0,columnas+1):
            y = y + '''<TD BGCOLOR="white"><FONT>'''+str(i)+'''</FONT></TD>'''

        cuerpo = cuerpo +tr_inicio+y+tr_fin
        for k in range(1,filas+1):
            x = x + '''<TD BGCOLOR="white"><FONT>'''+str(k)+'''</FONT></TD>'''
            for j in range(1,columnas+1):
                
                i = self.buscar_coordenadas(k,j).color                
                try:
                    if i == "negro":
                        x = x+'''<TD BGCOLOR="black"><FONT> </FONT></TD>'''


                    elif i == "verde":
                        x = x+'''<TD BGCOLOR="green"><FONT> </FONT></TD>'''

                    
                    elif i == "azul":
                        x = x+'''<TD BGCOLOR="blue"><FONT> </FONT></TD>'''


                    elif i == "gris":
                        x = x+'''<TD BGCOLOR="gray"><FONT> </FONT></TD>'''
       
                    elif i == "rojo":
                        x = x+'''<TD BGCOLOR="red"><FONT> </FONT></TD>'''

                    else:
                        x = x+'''<TD BGCOLOR="white"><FONT> </FONT></TD>'''

                except:
                    print("Error", i)
                    break
            cuerpo = cuerpo +tr_inicio+x+tr_fin  
            x = ""          

        dot.node('tab',shape='plaintext', label='''<<TABLE CELLSPACING="0">
                
                '''+cuerpo+'''

        </TABLE>>''')

                #generar salto de linea

                
        dot.view()
    
    def buscar_color(self,filas,columnas,color):
        z = 0
        for i in range(1,filas+1):
            for j in range(1,columnas+1):
                
                aux = self.buscar(i,j)
                
                if aux.color == color:
                    z = z+1
                    
        return z

    def buscar_color_coordenada(self,filas,columnas,color):
        
        for i in range(1,filas+1):
            for j in range(1,columnas+1):
                
                aux = self.buscar(i,j)
                
                if aux.color == color:                    
                    return aux
                    
    def realizar_mision(self,filacivil,columnacivil, filaentrada, columnarentrada):    
        aux = self.buscar_coordenadas(filacivil,columnacivil)
        print(aux.color)
        aux = self.buscar_coordenadas(filaentrada, columnarentrada)
        print(aux.color)

# self = Nuevo_mapa()
# self.llenar_matriz(int(15),int(20))

# self.unir_nodos(15,20)

# self.borrar_derecha(15,20)
# texto = "********************""*** **             *""*** *****E*****C****""*** ***** ***** ***R""E             A   AA""*** ** ** ** ** ****""*** ** ** ** ** **R*""*              A   *""*** ** ** ** ** ****""*** ** ** ** ** ****""***   A        A   *""*** ** ** ** ** ****""*** **  E ** *R ****""*** *****A        C*""*** *****C***** ****"

# self.llenar_colores(texto,15,20)
# self.imprimir_total(15,20)




    
