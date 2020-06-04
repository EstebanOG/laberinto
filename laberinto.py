def abre_archivo():
	return [(elemento)for x in open("matriz.txt","r").readlines() for elemento in x if(elemento!='\n' and elemento!=' ')]
print(abre_archivo())