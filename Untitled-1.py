#Daniel Arias Rivero-2240078
#Warly Andres Peña Rangel-2240057
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.raiz:
            self.raiz = nuevo_nodo
        else:
            self._insertar_recursivo(self.raiz, nuevo_nodo)

    def _insertar_recursivo(self, actual, nuevo):
        direccion = input(f"¿Dónde insertar el nodo {nuevo.valor} desde el nodo {actual.valor}? (i para izquierda, d para derecha): ").lower()
        if direccion == 'i':
            if not actual.izquierda:
                actual.izquierda = nuevo
            else:
                self._insertar_recursivo(actual.izquierda, nuevo)
        elif direccion == 'd':
            if not actual.derecha:
                actual.derecha = nuevo
            else:
                self._insertar_recursivo(actual.derecha, nuevo)
        else:
            print("Entrada inválida. Usa 'i' o 'd'.")
            self._insertar_recursivo(actual, nuevo)

    def peso(self):
        return self._contar_nodos(self.raiz)

    def _contar_nodos(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._contar_nodos(nodo.izquierda) + self._contar_nodos(nodo.derecha)

    def altura(self):
        return self._altura(self.raiz)

    def _altura(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self._altura(nodo.izquierda), self._altura(nodo.derecha))

    def orden(self):
        return 2  # Como es un árbol binario

    def mostrar_info(self):
        print(f"Peso del árbol (número de nodos): {self.peso()}")
        print(f"Altura del árbol: {self.altura()}")
        print(f"Orden del árbol: {self.orden()}")


# Programa principal
if __name__ == "__main__":
    arbol = Arbol()
    cantidad = int(input("¿Cuántos nodos deseas ingresar? "))

    for i in range(cantidad):
        valor = input(f"Ingrese el valor del nodo {i + 1}: ")
        arbol.insertar(valor)

    print("\n--- Información del Árbol ---")
    arbol.mostrar_info()
