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

    def imprimir(self, variable):
        aux = self.raiz

        while aux != None:
            if variable != "ChapinRescue":
                if aux.tipo != "ChapinRescue":
                    print("Nombre:",aux.nombre," Tipo:",aux.tipo," Capacidad:",aux.capacidad)              
                    aux = aux.siguiente
                else:
                    aux = aux.siguiente

            else:
                if aux.tipo == "ChapinRescue":
                    print("Nombre:",aux.nombre," Tipo:",aux.tipo)  
                    aux = aux.siguiente

                else:
                    aux = aux.siguiente


    def buscar(self, nombre):
        aux = self.raiz
        while aux != None:
            if aux.nombre == nombre:
                return aux
            aux = aux.siguiente
        return False

    def editar(self, nombre, tipo, capacidad):
        aux = self.raiz
        while aux != None:
            if aux.nombre == nombre:
                aux.tipo = tipo
                aux.capacidad = capacidad                
                return True
            aux = aux.siguiente
        return False
    def verificar(self):
        aux = self.raiz
        while aux != None:
            if aux.tipo== "ChapinRescue":
                return True
            aux = aux.siguiente
        return False

    def verificar_tipo(self):
        aux = self.raiz
        while aux != None:
            if aux.tipo == "ChapinFighter":
                return True
            aux = aux.siguiente
        return False