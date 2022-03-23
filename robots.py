class Nodo_dron:
    def __init__(self, nombre = None, tipo = None, capacidad = None, siguiente = None):
        self.nombre = nombre
        self.tipo = tipo
        self.capacidad = capacidad
        self.siguiente = siguiente

class Nuevo_nodo_dron:
    def __init__(self):
        self.raiz = Nodo_dron()
        self.ultimo = Nodo_dron()

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

    def imprimir(self):
        aux = self.raiz

        while aux != None:
            print(aux.nombre, aux.tipo, aux.capacidad)

            aux = aux.siguiente