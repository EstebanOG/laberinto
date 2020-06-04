from laberinto import *

def ubicando_variables():
    matriz = abre_archivo("matriz.txt")
    for fila in range(len(matriz)):
        for columna in  range(len(matriz[fila])):
            #print('{},{}'.format(fila, columna))
            if matriz[fila][columna] == '0':
                print('{},{}'.format(fila, columna))
            else:
                #print(matriz[fila][columna])
                pass

ubicando_variables()