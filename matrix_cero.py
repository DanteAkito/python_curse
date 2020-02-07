#mc = [[0]* 15] * 10

#for fila in mc:
#  print(fila)

matriz_cero = []    #Se crea una lista vacia
for i in range(10): #En rango de 1 a 10, se crean 10 listas
    matriz_cero.append([0]* 15) #Se agrega a la lista un cero, concatenado 15 veces
matriz_cero [2] [3] = 2     # Se indica que en el indice 2, 3 se va a cambiar el elemento a 2 ne donde el 3 indica la columna y el 2, la fila
for fila in matriz_cero:
    print(fila)