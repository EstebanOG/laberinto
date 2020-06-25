def buscar_en_matriz(matriz,cont):
    if matriz == []:
        return (-1,-1)
    if "X" in matriz[0]: 
        return [cont,matriz[0].index("X")]
    return buscar_en_matriz(matriz[1:],cont+1)

def abre_archivo():
	return [[elemento for elemento in x if(elemento!='\n' and elemento!=' ')]for x in open("matriz.txt","r").readlines() ]

def verificar_y(mapa, jugador,camino):
    if  mapa[jugador[0]][jugador[1]+1] == "Y":
        jugador[1] = jugador[1]+1
        return camino+[jugador]
    elif mapa[jugador[0]-1][jugador[1]] == "Y":
        jugador[0] = jugador[0]-1
        return camino+[jugador]
    elif mapa[jugador[0]][jugador[1]-1] == "Y":
        jugador[1] = jugador[1]-1
        return camino+[jugador]
    elif mapa[jugador[0]][jugador[1]] == "Y":
        jugador[0] = jugador[0]+1
        return camino+[jugador]
    else:
        return False

def recorrer(mapa, jugador, jugador_anterior, camino):
    #print(jugador)
    #print(jugador_anterior)
    #print("--")
    if verificar_y(mapa,jugador,camino) != False:
        return camino
    elif mapa[jugador[0]][jugador[1]+1] == "0":
        mapa[jugador[0]][jugador[1]] = "-"
        mapa[jugador[0]][jugador[1]+1] = "X"
        jugador_anterior = [jugador[0],jugador[1]]
        jugador[1] = jugador[1]+1
        return recorrer(mapa, jugador, jugador_anterior,camino+[jugador])
    elif mapa[jugador[0]-1][jugador[1]] == "0":
        mapa[jugador[0]][jugador[1]] = "-"
        mapa[jugador[0]-1][jugador[1]] = "X"
        jugador_anterior = [jugador[0],jugador[1]]
        jugador[0] = jugador[0]-1
        return recorrer(mapa, jugador, jugador_anterior,camino+[jugador])
    elif mapa[jugador[0]][jugador[1]-1] == "0":
        mapa[jugador[0]][jugador[1]] = "-"
        mapa[jugador[0]][jugador[1]-1] = "X"
        jugador_anterior = [jugador[0],jugador[1]]
        jugador[1] = jugador[1]-1
        return recorrer(mapa, jugador, jugador_anterior,camino+[jugador])
    elif mapa[jugador[0]+1][jugador[1]] == "0":
        mapa[jugador[0]][jugador[1]] = "-"
        mapa[jugador[0]+1][jugador[1]] = "X"
        jugador_anterior = [jugador[0],jugador[1]]
        jugador[0] = jugador[0]+1
        return recorrer(mapa, jugador, jugador_anterior,camino+[jugador])
    ###
    elif mapa[jugador[0]-1][jugador[1]] != "1" and jugador[0]-1 != jugador_anterior[0]:
        mapa[jugador[0]][jugador[1]] = "-"
        mapa[jugador[0]-1][jugador[1]] = "X"
        jugador_anterior = [jugador[0],jugador[1]]
        jugador[0] = jugador[0]-1
        return recorrer(mapa, jugador, jugador_anterior,camino+[jugador])
    elif mapa[jugador[0]][jugador[1]-1] != "1":
        mapa[jugador[0]][jugador[1]] = "-"
        mapa[jugador[0]][jugador[1]-1] = "X"
        jugador_anterior = [jugador[0],jugador[1]]
        jugador[1] = jugador[1]-1
        return recorrer(mapa, jugador, jugador_anterior,camino+[jugador])
    elif mapa[jugador[0]+1][jugador[1]] != "1":
        mapa[jugador[0]][jugador[1]] = "-"
        mapa[jugador[0]+1][jugador[1]] = "X"
        jugador_anterior = [jugador[0],jugador[1]]
        jugador[0] = jugador[0]+1
        return recorrer(mapa, jugador, jugador_anterior,camino+[jugador])
    elif mapa[jugador[0]][jugador[1]+1] != "1":
        mapa[jugador[0]][jugador[1]] = "-"
        mapa[jugador[0]][jugador[1]+1] = "X"
        jugador_anterior = [jugador[0],jugador[1]]
        jugador[1] = jugador[1]+1
        return recorrer(mapa, jugador, jugador_anterior,camino+[jugador])
    
print(recorrer(abre_archivo(),buscar_en_matriz(abre_archivo(),0),[0,0],[]))


