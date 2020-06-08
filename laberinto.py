def buscar_en_matriz(matriz,cont):
    if matriz == []:
        return (-1,-1)
    if "X" in matriz[0]: 
        return (cont,matriz[0].index("X"))
    return buscar_en_matriz(matriz[1:],cont+1)

def abre_archivo():
	return [[elemento for elemento in x if(elemento!='\n' and elemento!=' ')]for x in open("matriz.txt","r").readlines() ]

print(buscar_en_matriz(abre_archivo(),0))


