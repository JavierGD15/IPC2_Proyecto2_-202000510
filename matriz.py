
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

    def insertar(self, nuevoNodo,filas,columnas):
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

    def llenar_matriz(self, filas, columnas):
        Nuevo_mapa()
        for i in range(1,filas+1):
            for j in range(1,columnas+1):
                ejecutar.insertar(Matriz_nodo(i,j),filas,columnas)

    def buscar(self, x1,y1):
        aux3 = self.raiz
        while aux3 != None:
            if aux3.x == x1 and aux3.y == y1:
                return aux3
            aux3 = aux3.derecha
    
    def borrar_derecha(self, filas, columnas):
        for i in range(1,filas+1):
            
            aux = ejecutar.buscar(i,columnas)
            if aux== None:
                break
            else:
                aux.derecha = None       
           
    
    def unir_nodos(self,filas, columnas):
        Nuevo_mapa()
        for i in range(1,filas+1):
            for j in range(1,columnas+1):
                
                aux = ejecutar.buscar(i,j)
                
                if j-1 >= 0:
                    aux.izquierda = ejecutar.buscar(i,j-1)
               
                if i+1 <= filas:                    
                    aux.abajo = ejecutar.buscar(i+1,j)   
                    
                    
                if i-1 >= 1:
                    aux.arriba = ejecutar.buscar(i-1,j)
                

    #funciones de tablero

    def buscar_coordenadas(self,x2,y2):
        aux = self.raiz

        for j in range(1,y2):
            print(j)
            aux = aux.derecha
        for i in range(1,x2):
            aux = aux.abajo
        return aux

    def editar_coordenadas(self,x2,y2,color):
        aux = self.buscar_coordenadas(x2,y2)
        aux.color = color



ejecutar = Nuevo_mapa()
ejecutar.llenar_matriz(5,5)

ejecutar.unir_nodos(5,5)

ejecutar.borrar_derecha(5,5)

print("Resultado",ejecutar.buscar_coordenadas(5,1).x,ejecutar.buscar_coordenadas(5,5).y)

                



    
