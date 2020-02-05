
m = [[1, 2], [3, 4], [5, 6]] #una matriz en python, es una lista que contiene listas, donde cada lista es una fila(un piso)
#Esto seria igual:
#1 2  #Tres filas, 2 columnas
#3 4
#5 6
"""
for f in range(3):
    for c in range(2):
        print(m[f][c], end="") #Forma clasica de recorrer una matriz
    print(" ")
"""
a = np.array([1, 2, 3])

print(a.ndim)#Dimension de la matriz (ndim)