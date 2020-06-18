# Ejercicio 5: 
### Solución Laberinto [x,y]
##### Modelos de programación II - G.020-82


#### Descripción

_Programa desarrollado para resolver un laberinto dado en una matriz en un archivo de texto de un punto X a un punto Y dentro de la matriz_

Se hace uso de inteligencia artificial clásica, ilustrado en el siguiente gráfico:

Image:

![](https://github.com/FelipeH22/laberinto/blob/master/assets/esquema.jpg)


Ejemplo:
```
#Lectura archivo .txt sin estados

def abre_archivo(archivo_txt):
	return [[elemento for elemento in x if(elemento!='\n' and elemento!=' ')]for x in open(archivo_txt,"r").readlines() ]



#Estructura busqueda de X

def buscar_en_matriz(matriz,cont):
    if matriz == []:
        return (-1,-1)
    if "X" in matriz[0]: 
        return (cont,matriz[0].index("X"))
    return buscar_en_matriz(matriz[1:],cont+1)

```
Debido a que no se pueden usar estados, hacemos uso de funciones anónimas lambda:

```
#Función anónima
matriz = (lambda x: abre_archivo2(x))("laberinto.txt")
```

Una vez se tenga estructurado la matriz y tengamos identificado la posición de X, leemos los caminos disponibles y mostraremos por pantalla, antes de realizar la operación principal, que nos permitirá identificar el recorrido que nos permitá partir desde la _X_ y llegar hasta la _Y_.

```
#Buscando cordenadas libres
def ubicando_variables():
    matriz = (lambda x: abre_archivo2(x))("laberinto.txt")
    for fila in range(len(matriz)):
        for columna in  range(len(matriz[fila])):
            #print('{},{}'.format(fila, columna))
            if matriz[fila][columna] == '0':
                print('{},{}'.format(fila, columna))
                #print('{},{} = {}'.format(fila, columna,matriz[fila][columna]))
            else:
                #print(matriz[fila][columna])
                pass
```

La función principal:

```
#Estructura

```


#### Ejecutar proyecto
```
~$ python laberinto.py
```


#### Estructura del proyecto
+ main.py
+ logica.py
+ laberinto.py
+ busqueda.py
+ matriz.txt
+ assets/


#### Referencias
+ [1] 

### Integrantes

Nombre | Código
------------- | -------------
Cristhian Mauricio Yara Pardo | 20181020081
Juan Esteban Olaya García | 20171020135
Juan Felipe Herrera Poveda | 20181020077
