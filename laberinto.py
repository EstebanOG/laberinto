def buscar_en_matriz(matriz,cont):
    if matriz == []:
        return (-1,-1)
    if "X" in matriz[0]: 
        return [cont,matriz[0].index("X")]
    return buscar_en_matriz(matriz[1:],cont+1)

def abre_archivo():
	return [[elemento for elemento in x if(elemento!='\n' and elemento!=' ')]for x in open("matriz.txt","r").readlines() ]

def verificar(mapa, jugador):
    if  mapa[jugador[0]][jugador[1]+1] == "Y":
        jugador[1] = jugador[1]+1
        return jugador
    elif mapa[jugador[0]-1][jugador[1]] == "Y":
        jugador[0] = jugador[0]-1
        return jugador
    elif mapa[jugador[0]][jugador[1]-1] == "Y":
        jugador[1] = jugador[1]-1
        return jugador
    elif mapa[jugador[0]][jugador[1]] == "Y":
        jugador[0] = jugador[0]+1
        return jugador
    else:
        return False

def recorrer(mapa, jugador,camino,jugador_anterior):
    #print(mapa)
    print(jugador)
    print(jugador_anterior)
    print("--")
    if verificar(mapa,jugador) != False:
        return jugador
    elif mapa[jugador[0]][jugador[1]+1] == "0":
        mapa[jugador[0]][jugador[1]] = "-"
        mapa[jugador[0]][jugador[1]+1] = "X"
        jugador_anterior = [jugador[0],jugador[1]]
        jugador[1] = jugador[1]+1
        return recorrer(mapa, jugador, camino+jugador, jugador_anterior)
    elif mapa[jugador[0]-1][jugador[1]] == "0":
        mapa[jugador[0]][jugador[1]] = "-"
        mapa[jugador[0]-1][jugador[1]] = "X"
        jugador_anterior = [jugador[0],jugador[1]]
        jugador[0] = jugador[0]-1
        return recorrer(mapa, jugador, camino+jugador, jugador_anterior)
    elif mapa[jugador[0]][jugador[1]-1] == "0":
        mapa[jugador[0]][jugador[1]] = "-"
        mapa[jugador[0]][jugador[1]-1] = "X"
        jugador_anterior = [jugador[0],jugador[1]]
        jugador[1] = jugador[1]-1
        return recorrer(mapa, jugador, camino+jugador, jugador_anterior)
    elif mapa[jugador[0]+1][jugador[1]] == "0":
        mapa[jugador[0]][jugador[1]] = "-"
        mapa[jugador[0]+1][jugador[1]] = "X"
        jugador_anterior = [jugador[0],jugador[1]]
        jugador[0] = jugador[0]+1
        return recorrer(mapa, jugador, camino+jugador, jugador_anterior)
    elif mapa[jugador[0]-1][jugador[1]] != "1" and mapa[jugador[0]-1][jugador[1]] != mapa[jugador_anterior[0]][jugador_anterior[1]]:
        mapa[jugador[0]][jugador[1]] = "-"
        mapa[jugador[0]-1][jugador[1]] = "X"
        jugador_anterior = [jugador[0],jugador[1]]
        jugador[0] = jugador[0]-1
        return recorrer(mapa, jugador, camino+jugador, jugador_anterior)
    elif mapa[jugador[0]][jugador[1]-1] != "1":
        mapa[jugador[0]][jugador[1]] = "-"
        mapa[jugador[0]][jugador[1]-1] = "X"
        jugador_anterior = [jugador[0],jugador[1]]
        jugador[1] = jugador[1]-1
        return recorrer(mapa, jugador, camino+jugador, jugador_anterior)
    elif mapa[jugador[0]+1][jugador[1]] != "1":
        mapa[jugador[0]][jugador[1]] = "-"
        mapa[jugador[0]+1][jugador[1]] = "X"
        jugador_anterior = [jugador[0],jugador[1]]
        jugador[0] = jugador[0]+1
        return recorrer(mapa, jugador, camino+jugador, jugador_anterior)
    elif mapa[jugador[0]][jugador[1]+1] != "1":
        mapa[jugador[0]][jugador[1]] = "-"
        mapa[jugador[0]][jugador[1]+1] = "X"
        jugador_anterior = [jugador[0],jugador[1]]
        jugador[1] = jugador[1]+1
        return recorrer(mapa, jugador, camino+jugador,jugador_anterior)
    
print(recorrer(abre_archivo(),buscar_en_matriz(abre_archivo(),0),[],[0,0]))


