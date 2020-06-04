def abre_archivo():
	return [[elemento for elemento in x if(elemento!='\n' and elemento!=' ')]for x in open("matriz.txt","r").readlines() ]
print(abre_archivo())