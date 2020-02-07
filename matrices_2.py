# Crear programa para introducir datos en la matriz
x = int(input("Digita el numero de filas: ")) # se introduce el numero de filas
z = int(input("Digita el numero de columnas: ")) # se introduce el numero de columnas

matriz_cero = [] # se crea una matiz vacia
for i in range(x): # para una variable i en la variable x, osea las filas, agregar una lista
    matriz_cero.append([]) # indica que debe agregar una lista vacia
    for j in range(z): # para una variable j en las columnas
        v = int(input("Introduce los datos para " + "fila {}, columna {} :".format (i+1, j+1))) # pide los datos que contiene la matriz formateando para que cada vez pida el dato siguiente
        matriz_cero[i].append(v) # agregar el dato a la lista
        

for fila in matriz_cero: # crae la variable fila
    print(fila) # imprime el dato fila