x = 1
y = 1

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
    
    def insertar(self, nuevoNodo,filas,columnas):
        global x,y
        if self.raiz.x == None:
            self.raiz = nuevoNodo
            self.ultimo = nuevoNodo
            x = x+1
        
        elif x > columnas:
            print(nuevoNodo.x, nuevoNodo.y)
            self.raiz.abajo = nuevoNodo  
            aux = self.raiz.abajo
            aux.derecha = self.ultimo
            x = 1

        elif self.raiz.derecha == None:
            self.raiz.derecha = nuevoNodo
            self.ultimo = nuevoNodo
            x = x+1
        else:
            self.ultimo.derecha = nuevoNodo
            self.ultimo = nuevoNodo
            x = x+1
    
    def imprimir(self):
        aux = self.raiz
        while aux.abajo != None:
            while aux != None:
                print(aux.x, aux.y, aux.izquierda, aux.derecha, aux.arriba, aux.abajo, aux.color)
                aux = aux.derecha
            
            aux = self.raiz.abajo

    def llenar_matriz(self, filas, columnas):
        Nuevo_mapa()
        for i in range(1,filas+1):
            for j in range(1,columnas+1):
                ejecutar.insertar(Matriz_nodo(i,j),filas,columnas)

    def buscar(self, x1,y1):
        aux = self.raiz
        try:
            while aux != None:
                if aux.x == x1 and aux.y == y1:
                    return aux
                elif aux.derecha == None:
                    aux = aux.abajo
                else:
                    aux = aux.derecha
            return None
        except:
            return None

    
    def unir_nodos(self,filas, columnas):
        Nuevo_mapa()
        
        for i in range(1,filas+1):
            for j in range(1,columnas+1):
                print(i,j)
                aux = ejecutar.buscar(i,j)
                print(aux)
                aux.izquierda = ejecutar.buscar(i,j-1)
                aux.derecha = ejecutar.buscar(i,j+1)
                aux.abajo = ejecutar.buscar(i+1,j)
                aux.arriba = ejecutar.buscar(i-1,j)

ejecutar = Nuevo_mapa()
ejecutar.llenar_matriz(5,5)
ejecutar.imprimir()
ejecutar.unir_nodos(5,5)
ejecutar.imprimir()

                



    
