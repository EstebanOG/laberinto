def abre_archivo():
	return [x for x in open("matriz.txt","r").readlines()]
print(abre_archivo())