def buscar_en_matriz(matriz,cont):
    if matriz == []:
        return (-1,-1)
    if "X" in matriz[0]: 
        return [cont,matriz[0].index("X")]
    return buscar_en_matriz(matriz[1:],cont+1)

def abre_archivo():
	return [[elemento for elemento in x if(elemento!='\n' and elemento!=' ')]for x in open("matriz.txt","r").readlines() ]
def verificar(mapa,jugador):
    pass
def recorrer(mapa, jugador):
    print(mapa)
    print(jugador)
    
    if jugador[1] != len(mapa[0])-1 and mapa[jugador[0]][jugador[1]+1] == "0":
        print("derecha")
        mapa[jugador[0]][jugador[1]] = "0"
        mapa[jugador[0]][jugador[1]+1] = "X"
        jugador[1] = jugador[1]+1
        return recorrer(mapa, jugador)
    elif mapa[jugador[0]-1][jugador[1]] == "0":
        print("arriba")
        mapa[jugador[0]][jugador[1]] = "0"
        mapa[jugador[0]-1][jugador[1]] = "X"
        jugador[0] = jugador[0]-1
        return recorrer(mapa, jugador)
    elif mapa[jugador[0]][jugador[1]-1] == "0":
        print("Izquierda")
        mapa[jugador[0]][jugador[1]] = "0"
        mapa[jugador[0]][jugador[1]-1] = "X"
        jugador[1] = jugador[0]-1
        return recorrer(mapa, jugador)
    elif mapa[jugador[0]][jugador[1]] == "0":
        print("abajo")
        mapa[jugador[0]][jugador[1]] = "0"
        mapa[jugador[0]+1][jugador[1]] = "X"
        jugador[0] = jugador[0]+1
        return recorrer(mapa, jugador)
    

print(recorrer(abre_archivo(),buscar_en_matriz(abre_archivo(),0)))

