class Nodo_guerra:
    def __init__(self, nombre = None,fila = None, columna = None, valor =None, siguiente = None):        
        self.nombre  = nombre 
        self.fila = fila
        self.columna = columna
        self.valor = valor 
        self.siguiente = siguiente


class Nuevo_Nodo_guerra:
    def __init__(self):
        self.raiz = Nodo_guerra()
        self.ultimo = Nodo_guerra()

    def insertar(self, nuevoNodo):
        if self.raiz.nombre == None:
            self.raiz = nuevoNodo
            self.ultimo = nuevoNodo
        
        elif self.raiz.siguiente == None:
            self.raiz.siguiente = nuevoNodo
            self.ultimo = nuevoNodo
        else:
            self.ultimo.siguiente = nuevoNodo
            self.ultimo = nuevoNodo

    def devolver(self):
        aux = self.raiz
        return aux
    
    def imprimir(self):
        aux = self.raiz
        
        while aux != None:
            print(aux.nombre, aux.fila, aux.columna, aux.valor)
            
            aux = aux.siguiente

    def buscar(self, fila, columna):
        aux = self.raiz
        while aux != None:
            if aux.fila == fila and aux.columna == columna:
                return aux.valor
            aux = aux.siguiente
        return False
