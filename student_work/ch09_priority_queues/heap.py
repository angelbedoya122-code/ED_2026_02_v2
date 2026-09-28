
class Heap:

    def __init__(self):
        self.arreglo = [float('-inf')]

    def insert(self, valor):
        self.arreglo.append(valor)
        i = len(self.arreglo) - 1
        while i > 1 and self.arreglo[i] < self.arreglo[i // 2]:
            self.arreglo[i], self.arreglo[i // 2] = self.arreglo[i // 2], self.arreglo[i]
            i = i // 2

    def remove_smallest(self):
        ultimo = self.arreglo.pop()
        if len(self.arreglo) == 1:           
            return
        self.arreglo[1] = ultimo
        i = 1
        n = len(self.arreglo) - 1
        while 2 * i <= n:
            izq = 2 * i
            der = 2 * i + 1
            menor = izq if der > n or self.arreglo[izq] <= self.arreglo[der] else der
            if self.arreglo[i] <= self.arreglo[menor]:
                break
            self.arreglo[i], self.arreglo[menor] = self.arreglo[menor], self.arreglo[i]
            i = menor

    def build_heap(self, lista):
        pass
