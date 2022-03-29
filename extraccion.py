from graphviz import Digraph, Graph
from turtle import pen
from guerreros import Nodo_guerra, Nuevo_Nodo_guerra
guerra = Nuevo_Nodo_guerra()

class Matriz_nodo:
    def __init__(self, x = None, y = None, izquierda = None, derecha = None, arriba = None, abajo = None, color = None, capacidad = None):
        self.x = x
        self.y = y
        self.izquierda = izquierda
        self.derecha = derecha
        self.arriba = arriba
        self.abajo = abajo
        self.color = color
        self.capacidad = capacidad

class Nueva_extraccion:
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

    def editar_coordenadas_robot(self,fila,columna,color,capacidad):        
        aux = self.buscar_coordenadas(fila,columna)
        if color == "rojo":
            aux.color = color
            aux.capacidad = capacidad
        else:
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
                        elif i == "A":
                        
                            self.editar_coordenadas_robot(int(fila),int(columna),"rojo",1)
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

                    elif i == "A":
                        
                        self.editar_coordenadas(int(fila),int(columna),"rojo")
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

                    elif i == "amarrillo":
                        x = x+'''<TD BGCOLOR="yellow"><FONT> </FONT></TD>'''
                    
                    elif i == "bl":
                        x = x+'''<TD BGCOLOR="purple"><FONT> </FONT></TD>'''

                    elif i == "blanco":
                        x = x+'''<TD BGCOLOR="white"><FONT> </FONT></TD>'''

                    else:
                        x = x+'''<TD BGCOLOR="yellow"><FONT> </FONT></TD>'''

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
    def pelea(self,filas,columnas):
        global ciudad, guerreros
        ayuda = guerreros
        
        while ayuda != None:
            
            if ayuda.nombre == ciudad and int(ayuda.fila) == int(filas) and int(ayuda.columna) == int(columnas):
                
                return ayuda.valor
            else:
                ayuda = ayuda.siguiente
        


    def realizar_mision(self,filarecurso,columnarecurso, filaentrada, columnarentrada,matriz,capacidad1,filas,columnas,opcion,ayuda): 
        global capacidad, fila_final, columna_final, ciudad,guerreros
        guerreros = ayuda
        ciudad = opcion
        fila_final = filas
        columna_final = columnas
        capacidad = capacidad1
        self.raiz = matriz   
        recurso = self.buscar_coordenadas(filarecurso,columnarecurso)        
        usuario = self.buscar_coordenadas(filaentrada, columnarentrada)
        
        print("Coordenadas recurso: ", recurso.x, recurso.y)
        print("Coordenadas usuario: ", usuario.x, usuario.y)
        #Comparamos ubicaciones
        if usuario.x > recurso.x :
            if usuario.y > recurso.y :
                print("Esta hacia arriba y la izquierda")
                self.arriba_izquierda(usuario,recurso)
            elif usuario.y == recurso.y :
                print("Esta hacia arriba en la misma columna")
            else:
                print("Esta hacia arriba y la derecha")
                self.arriba_derecha(usuario,recurso)


        elif usuario.x == recurso.x :
            if usuario.y > recurso.y :
                print("Esta hacia la izquierda en la misma fila")
                self.abajo_izquierda(usuario,recurso)
            elif usuario.y == recurso.y :
                print("Esta en el mismo lugar")
            else:
                print("Esta hacia la derecha en la misma fila")
                self.abajo_derecha(usuario,recurso)

        else:
            if usuario.y > recurso.y :
                print("Esta hacia abajo y la izquierda")
                self.abajo_izquierda(usuario,recurso)
            else:
                print("Esta hacia abajo y la derecha")
                self.abajo_derecha(usuario,recurso)
        
    def derecha(self,usuario):
        global capacidad        
        if usuario.derecha.color == "blanco" or usuario.derecha.color == "amarrillo" or usuario.derecha.color == "verde" or usuario.derecha.color == "azul" or usuario.derecha.color == "gris":
            return True
        
        elif usuario.derecha.color == "rojo":
            if capacidad >= int(self.pelea(usuario.derecha.x,usuario.derecha.y)):
                capacidad = capacidad - int(self.pelea(usuario.derecha.x,usuario.derecha.y))    

                return True
            else:
                print("No hay suficiente capacidad")
                return False           
        
        else:
            return False

    def izquierda(self,usuario):
        global capacidad
        if usuario.izquierda.color == "blanco" or usuario.izquierda.color == "amarrillo" or usuario.izquierda.color == "verde" or usuario.izquierda.color == "azul" or usuario.izquierda.color == "gris":
            return True

        elif usuario.izquierda.color == "rojo":
            if capacidad >= int(self.pelea(usuario.izquierda.x,usuario.izquierda.y)):
                capacidad = capacidad - int(self.pelea(usuario.izquierda.x,usuario.izquierda.y))
                return True
            else:
                return False 

        else:
            return False

    
    def abajo(self,usuario):
        global capacidad
        if usuario.abajo.color == "blanco" or usuario.abajo.color == "amarrillo" or usuario.abajo.color == "verde" or usuario.abajo.color == "azul" or usuario.abajo.color == "gris":
            return True

        elif usuario.abajo.color == "rojo":
            if capacidad >= int(self.pelea(usuario.abajo.x,usuario.abajo.y)):
                capacidad = capacidad - int(self.pelea(usuario.abajo.x,usuario.abajo.y))
                
                return True
            else:
                return False 

        else:
            return False
        
    def arriba(self,usuario):
        global capacidad
        if usuario.arriba.color == "blanco" or usuario.arriba.color == "amarrillo" or usuario.arriba.color == "verde" or usuario.arriba.color == "azul" or usuario.arriba.color == "gris":
            return True
        
        elif usuario.arriba.color == "rojo":
            if capacidad >= int(self.pelea(usuario.arriba.x,usuario.arriba.y)):
                capacidad = capacidad - int(self.pelea(usuario.arriba.x,usuario.arriba.y))
                return True
            else:
                return False 

        else:
            return False
    
    def llegar_derecha(self,usuario,recurso):
        try:
            if usuario.derecha.x == recurso.x and usuario.derecha.y == recurso.y:
                print("Tipo de Misión: Extraccion")
                print("Coordenadas extracción: ", recurso.x, recurso.y)
                print("Capacidad final: ", capacidad)
                return True
            else:
                return False
        except:
            return False
    def llegar_izquierda(self,usuario,recurso):
        try:
            if usuario.izquierda.x ==  recurso.x and usuario.izquierda.y == recurso.y:
                print("Tipo de Misión: Extraccion")
                print("Coordenadas extracción: ", recurso.x, recurso.y)
                print("Capacidad final: ", capacidad)
                return True
            else:
                return False
        except:
            return False
    def llegar_abajo(self,usuario,recurso):
        try:
            if usuario.abajo.x ==  recurso.x and usuario.abajo.y == recurso.y:
                print("Tipo de Misión: Extraccion")
                print("Coordenadas extracción: ", recurso.x, recurso.y)
                print("Capacidad final: ", capacidad)
                return True
            else:
                return False
        except:
            return False
    def llegar_arriba(self,usuario,recurso):
        try:
            if usuario.arriba.x ==  recurso.x and usuario.arriba.y == recurso.y:
                print("Tipo de Misión: Extraccion")
                print("Coordenadas extracción: ", recurso.x, recurso.y)
                print("Capacidad final: ", capacidad)
                return True
            else:
                return False
        except:
            return False

    def abajo_derecha(self,usuario,recurso):
        global fila_final, columna_final
        try:
            
            if self.llegar_derecha(usuario,recurso) == True:
                print("Mision completada")
                self.imprimir_total(fila_final, columna_final)

            elif self.llegar_abajo(usuario,recurso) == True:
                print("Mision completada")
                self.imprimir_total(fila_final, columna_final)
            
            elif self.llegar_arriba(usuario,recurso) == True:
                print("Mision completada")
                self.imprimir_total(fila_final, columna_final)  

            elif self.llegar_izquierda(usuario,recurso) == True:
                print("Mision completada")
                self.imprimir_total(fila_final, columna_final) 

            else:
                if self.derecha(usuario) == True:
                    usuario.derecha.color = "amarrillo"
                    self.abajo_derecha(usuario.derecha, recurso)

                elif self.abajo(usuario) == True:
                    usuario.abajo.color = "amarrillo"
                    self.abajo_derecha(usuario.abajo, recurso)
                
                elif self.izquierda(usuario) == True:
                    usuario.color = "bl"
                    self.abajo_derecha(usuario.izquierda, recurso)

                elif self.arriba(usuario) == True:
                    usuario.arriba.color = "amarrillo"
                    self.abajo_derecha(usuario.arriba, recurso)

                

                else:
                    print("Coordenada", usuario.x, usuario.y)
                    
                    print("No se puede rescatar")
        except Exception as e:
            print(e)
            print("Coordenada", usuario.x, usuario.y)
           
            print("No se puede rescatar")

    def abajo_izquierda(self,usuario,recurso):
        global fila_final, columna_final
        try:
            if self.llegar_derecha(usuario,recurso) == True:
                print("Mision completada")
                self.imprimir_total(fila_final, columna_final)

            elif self.llegar_abajo(usuario,recurso) == True:
                print("Mision completada")
                self.imprimir_total(fila_final, columna_final)
            
            elif self.llegar_arriba(usuario,recurso) == True:
                print("Mision completada")
                self.imprimir_total(fila_final, columna_final)  

            elif self.llegar_izquierda(usuario,recurso) == True:
                print("Mision completada")
                self.imprimir_total(fila_final, columna_final)                

            else:
                if self.izquierda(usuario) == True:
                    usuario.izquierda.color = "amarrillo"
                    self.abajo_izquierda(usuario.izquierda, recurso)

                elif self.abajo(usuario) == True:
                    usuario.abajo.color = "amarrillo"
                    self.abajo_izquierda(usuario.abajo, recurso)
                
                elif self.derecha(usuario) == True:
                    usuario.color = "bl"
                    self.abajo_izquierda(usuario.derecha, recurso)

                elif self.arriba(usuario) == True:
                    usuario.arriba.color = "amarrillo"
                    self.abajo_izquierda(usuario.arriba, recurso)

                

                else:
                    print("Coordenada", usuario.x, usuario.y)
                    
                    print("No se puede rescatar")
        except:
            print("Coordenada", usuario.x, usuario.y)
            
            print("No se puede rescatar")

    def arriba_izquierda(self,usuario,recurso):
        global fila_final, columna_final
        try:
            if self.llegar_derecha(usuario,recurso) == True:
                print("Mision completada")
                self.imprimir_total(fila_final, columna_final)

            elif self.llegar_abajo(usuario,recurso) == True:
                print("Mision completada")
                self.imprimir_total(fila_final, columna_final)
            
            elif self.llegar_arriba(usuario,recurso) == True:
                print("Mision completada")
                self.imprimir_total(fila_final, columna_final)  

            elif self.llegar_izquierda(usuario,recurso) == True:
                print("Mision completada")
                self.imprimir_total(fila_final, columna_final) 
            else:
                if self.izquierda(usuario) == True:
                    usuario.izquierda.color = "amarrillo"
                    self.arriba_izquierda(usuario.izquierda, recurso)

                elif self.arriba(usuario) == True:
                    usuario.arriba.color = "amarrillo"
                    self.arriba_izquierda(usuario.arriba, recurso)

                elif self.derecha(usuario) == True:
                    usuario.color = "bl"
                    self.arriba_izquierda(usuario.derecha, recurso)

                elif self.abajo(usuario) == True:
                    usuario.color = "bl"
                    self.arriba_izquierda(usuario.abajo, recurso)

                else:
                    print("Coordenada", usuario.x, usuario.y)
                    
                    print("No se puede rescatar")
        except:
            print("Coordenada", usuario.x, usuario.y)
            print("No se puede rescatar")

    def arriba_derecha(self,usuario,recurso):
        global fila_final, columna_final
        try:
            if self.llegar_derecha(usuario,recurso) == True:
                print("Mision completada")
                self.imprimir_total(fila_final, columna_final)

            elif self.llegar_abajo(usuario,recurso) == True:
                print("Mision completada")
                self.imprimir_total(fila_final, columna_final)
            
            elif self.llegar_arriba(usuario,recurso) == True:
                print("Mision completada")
                self.imprimir_total(fila_final, columna_final)  

            elif self.llegar_izquierda(usuario,recurso) == True:
                print("Mision completada")
                self.imprimir_total(fila_final, columna_final) 

            else:
                if self.arriba(usuario) == True:
                    usuario.arriba.color = "amarrillo"
                    self.arriba_derecha(usuario.arriba, recurso)
                elif self.derecha(usuario) == True:
                    usuario.derecha.color = "amarrillo"
                    self.arriba_derecha(usuario.derecha, recurso)
                
                elif self.abajo(usuario) == True:
                    usuario.color = "bl"
                    self.arriba_derecha(usuario.abajo, recurso)

                elif self.izquierda(usuario) == True:
                    usuario.color = "bl"
                    self.arriba_derecha(usuario.izquierda, recurso)

                

                else:
                    print("Coordenadaaaaaaaaaaa", usuario.x, usuario.y)                    
                    print("No se puede rescatar")
        except Exception as e:
            print(e)
            print("Coordenada error", usuario.x, usuario.y)
           
            print("No se puede rescatar")



#guerra = Nuevo_Nodo_guerra()

# t1 = Nodo_guerra("Ratchet",5,15,1)
# t2 = Nodo_guerra("Ratchet",8,16,1)
# t3 = Nodo_guerra("Ratchet",5,19,1)
# t4 = Nodo_guerra("Ratchet",5,20,1)
# t5 = Nodo_guerra("Ratchet",11,7,1)
# t6 = Nodo_guerra("Ratchet",11,14,1)
# t7 = Nodo_guerra("Ratchet",14,10,1)

# guerra.insertar(t1)
# guerra.insertar(t2)
# guerra.insertar(t3)
# guerra.insertar(t4)
# guerra.insertar(t5)
# guerra.insertar(t6)
# guerra.insertar(t7)

# capacidad = 15

# self = Nuevo_mapa()
# self.llenar_matriz(int(15),int(20))
# self.unir_nodos(15,20)
# self.borrar_derecha(15,20)
# texto = "********************""*** **             *""*** *****E*****C****""*** ***** ***** ***R""E             A   AA""*** ** ** ** ** ****""*** ** ** ** ** **R*""*              A   *""*** ** ** ** ** ****""*** ** ** ** ** ****""***   A      A     *""*** ** ** ** ** ****""*** **  E ** *R ****""*** *****A        C*""*** *****C***** ****"

# self.llenar_colores(texto,15,20)
# #self.imprimir_total(fila_final, columna_final)

# self.realizar_mision(5,1,14,16, 10)