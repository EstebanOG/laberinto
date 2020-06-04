from laberinto import *
from busqueda import *
'''
def ubicando_variables():
    matriz = abre_archivo("matriz.txt")
    for fila in range(len(matriz)):
        for columna in  range(len(matriz[fila])):
            #print('{},{}'.format(fila, columna))
            if matriz[fila][columna] == '0':
                print('{},{} = {}'.format(fila, columna))
                #print('{},{} = {}'.format(fila, columna,matriz[fila][columna]))
            else:
                #print(matriz[fila][columna])
                pass
'''



def ubicando_variables():
    matriz = abre_archivo("matriz.txt")
    for fila in range(len(matriz)):
        for columna in  range(len(matriz[fila])):
            #print('{},{}'.format(fila, columna))
            if matriz[fila][columna] == '0':
                print('{},{}'.format(fila, columna))
                #print('{},{} = {}'.format(fila, columna,matriz[fila][columna]))
            else:
                #print(matriz[fila][columna])
                pass

    print('La ubicación de X es: {}'.format(buscar_en_matriz(matriz,0)))
