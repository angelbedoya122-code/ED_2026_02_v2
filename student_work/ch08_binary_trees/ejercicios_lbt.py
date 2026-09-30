from goodrich.ch08.linked_binary_tree import LinkedBinaryTree


from collections import deque

def es_completo(T):
    '''True si T es un árbol completo'''
    if T.is_empty():
        return True
    cola = deque([T.root()])
    hueco_visto = False
    while cola:
        p = cola.popleft()
        if p is None:
            hueco_visto = True
        else:
            if hueco_visto:
                return False
            cola.append(T.left(p))
            cola.append(T.right(p))
    return True


def camino(T, p, q):
    '''Str con el camino de p a q, elementos separados por " -> ".'''
    ancestros_q = []
    x = q
    while x is not None:
        ancestros_q.append(x)
        x = T.parent(x)

    subida = []
    x = p
    while x not in ancestros_q:
        subida.append(x)
        x = T.parent(x)
    lca = x

    idx = ancestros_q.index(lca)
    bajada = ancestros_q[:idx][::-1]

    posiciones = subida + [lca] + bajada
    return ' -> '.join(str(pos.element()) for pos in posiciones)


if __name__ == "__main__":
    # tus pruebas (opcional)
    pass
