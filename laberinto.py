'''
def abre_archivo(archivo):
	return [x for x in open(archivo,"r").readlines()]


def abre_archivo2(archivo):
	return [(elemento)for x in open(archivo,"r").readlines() for elemento in x if(elemento!='\n' and elemento!=' ')]

#print(abre_archivo2())
'''
def buscar_en_matriz(matriz,cont):
    if matriz == []:
        return (-1,-1)
    if "X" in matriz[0]: 
        return (cont,matriz[0].index("X"))
    return buscar_en_matriz(matriz[1:],cont+1)

def abre_archivo(archivo):
	return [[elemento for elemento in x if(elemento!='\n' and elemento!=' ')]for x in open(archivo,"r").readlines() ]

#print(abre_archivo())


