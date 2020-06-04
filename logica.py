from laberinto import *

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



def ubicando_variables2():
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
    posiciónX = lambda x: [x.index("x") for x in matriz[x][x]]
    print(posiciónX)

ubicando_variables2()