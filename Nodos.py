class Nodo:
    def __init__(self, nombre = None, fila = None, columna = None, filatexto =None, siguiente = None):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.filatexto = filatexto
        self.siguiente = siguiente


class Nuevo_Nodo:
    def __init__(self):
        self.raiz = Nodo()
        self.ultimo = Nodo()

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
        return self.raiz

    def imprimir(self):
        aux = self.raiz
        
        while aux != None:
            print(aux.nombre, aux.fila, aux.columna, aux.filatexto)
            
            aux = aux.siguiente

    def buscar(self, nombre):
        aux = self.raiz
        while aux != None:
            if aux.nombre == nombre:
                return True
            aux = aux.siguiente
        return False

    def editar(self, nombre, fila, columna, filatexto):
        aux = self.raiz
        while aux != None:
            if aux.nombre == nombre:
                aux.fila = fila
                aux.columna = columna
                aux.filatexto = filatexto
                return True
            aux = aux.siguiente
        return False


