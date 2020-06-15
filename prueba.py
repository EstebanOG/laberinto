from laberinto import *
from busqueda import *

matriz = (lambda x: abre_archivo2(x))("laberinto.txt")
mapa = {matriz}
origen = buscar_en_matriz(matriz,0)
print('Origen: {}'.format(origen))
destino = [1,9]
print('destino: {}'.format(origen))

initial_node = [origen[0],origen[1],[]]

#elem_visitado = lambda x: for key in matriz.keys(): visitados[key] = [False for _ in mapa[key]]



for key in mapa.keys():
    visitados[key] = [False for _ in mapa[key]]
visitados

visitados[origen[0]][origen[1]] = True
visitados

'''
from collections import deque

def search():

    # Inicialización de la cola auxiliar para ejecutar la búsqueda
    q = deque()
    q.append(initial_node)
    
    while len(q) > 0:
        # Extraer un nodo del árbol de búsqueda
        node = q.popleft()
        
        # Comprobar si se trata de nuestro nodo objetivo
        if node[0] == destino[0] and node[1] == destino[1]:
            return node
        
        # Generar nuevos movimientos
        mov_x = [-1,  0,  0,  1]
        mov_y = [ 0, -1,  1,  0]
        
        predecesores = [n for n in node[2]]
        predecesores.append([node[0], node[1]])
        
        for i in range(4):
            x = node[0] + mov_x[i]
            y = node[1] + mov_y[i]
            
            # Se agrega el nodo sólo si el nuevo movimiento no ha sido ya realizado o si no hay obstáculos en la nueva coordenada
            if not visitados[x][y] and mapa[x][y] == 0:
                visitados[x][y] = True
                new_node = [x,y,predecesores]
                q.append(new_node)
    
    return []
        

print(search())'''