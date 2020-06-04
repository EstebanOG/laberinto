def abre_archivo(archivo):
	return [x for x in open(archivo,"r").readlines()]


def abre_archivo2(archivo):
	return [(elemento)for x in open(archivo,"r").readlines() for elemento in x if(elemento!='\n' and elemento!=' ')]

#print(abre_archivo2())
