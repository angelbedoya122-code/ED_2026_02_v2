
import matplotlib.pyplot as plt

class Heap:

    def __init__(self):
        self.arreglo = [float('-inf')]

    # Operaciones
    def insert(self, valor, imagen=False):
        self.arreglo.append(valor)
        i = len(self.arreglo) - 1
        while i > 1 and self.arreglo[i] < self.arreglo[i // 2]:
            self.arreglo[i], self.arreglo[i // 2] = self.arreglo[i // 2], self.arreglo[i]
            i = i // 2
        if imagen:
            self._mostrar(f'insert({valor})')

    def remove_smallest(self, imagen=False):
        if len(self.arreglo) > 1:               # heap no vacío
            ultimo = self.arreglo.pop()
            if len(self.arreglo) > 1:           # quedan elementos: el último pasa a la raíz
                self.arreglo[1] = ultimo
                self._hundir(1)
        if imagen:
            self._mostrar('remove_smallest()')

    def build_heap(self, lista, imagen=False):
        self.arreglo = [float('-inf')] + list(lista)
        for i in range((len(self.arreglo) - 1) // 2, 0, -1):
            self._hundir(i)
        if imagen:
            self._mostrar(f'build_heap({len(lista)} elementos)')

    def _hundir(self, i):
        n = len(self.arreglo) - 1
        while 2 * i <= n:
            izq = 2 * i
            der = 2 * i + 1
            menor = izq if der > n or self.arreglo[izq] <= self.arreglo[der] else der
            if self.arreglo[i] <= self.arreglo[menor]:
                break
            self.arreglo[i], self.arreglo[menor] = self.arreglo[menor], self.arreglo[i]
            i = menor

    # Imagen del árbol

    def _posiciones(self):
        """Coordenadas (x, y) de cada nodo i = 1..n.

        Cada nivel va debajo del anterior; dentro de un nivel los nodos se
        reparten en el ancho total, así los hijos izquierdos quedan a la
        izquierda y los derechos a la derecha, como en la página.
        """
        n = len(self.arreglo) - 1
        pos = {}
        for i in range(1, n + 1):
            nivel = i.bit_length() - 1           # raíz = nivel 0
            indice = i - (1 << nivel)            # posición dentro del nivel
            x = (indice + 0.5) / (1 << nivel)
            pos[i] = (x, -nivel)
        return pos

    def _mostrar(self, titulo=''):
        n = len(self.arreglo) - 1
        niveles = n.bit_length() if n else 1
        ancho = min(max(6, 0.55 * (1 << (niveles - 1)) + 2), 18)
        fig, ax = plt.subplots(figsize=(ancho, 1.4 * niveles + 1))
        ax.set_axis_off()
        ax.set_title(titulo)

        if n == 0:
            ax.text(0.5, 0.5, '(heap vacío)', ha='center', va='center')
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
        else:
            pos = self._posiciones()
            # aristas primero (quedan debajo de los nodos)
            for i in range(2, n + 1):
                (x0, y0), (x1, y1) = pos[i // 2], pos[i]
                ax.plot([x0, x1], [y0, y1], color='#555555', linewidth=1.3, zorder=1)
            # nodos
            for i in range(1, n + 1):
                x, y = pos[i]
                ax.text(x, y, str(self.arreglo[i]), ha='center', va='center',
                        fontsize=11, zorder=2,
                        bbox=dict(boxstyle='circle,pad=0.45', facecolor='#cfe8ff',
                                  edgecolor='#1f4e79', linewidth=1.5))
            ax.set_xlim(-0.03, 1.03)
            ax.set_ylim(-(niveles - 1) - 0.5, 0.5)

        plt.show()


if __name__ == "__main__":
    H = Heap()
    H.insert(10)
    H.insert(4)
    H.insert(7, imagen=True)
    H.remove_smallest(imagen=True)
