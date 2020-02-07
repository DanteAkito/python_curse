
a = [[21, 18, 35, 40],
     [19, 11, 21, 14],
     [12, 15, 20, 30]]

b = [[11, 7, 21, 32],
     [9, 15, 24, 10],
     [23, 8, 12, 22]]

def sumar_matrices(m1, m2): # se define una funcion para sumar matrices
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]): # se condiciona que si la longitud (a longitud se refiere a que tenga el mismo numero de columnas y filas) de la matriz 1 es igual a la matriz 2 se puedan sumar, de lo contrario, si son distintas no se pueda.
        m3= [] #Se crea una tercera matriz, donde se van sumar las matrices
        for i in range(len(m1)): # se crea variable 'i' en el rango de la longitud de la matriz 1 de las filas agregar una lista
            m3.append([]) # agrega la lista
            for j in range(len(m1[0])): #para la variable j en el rango de la longitud de la matriz 1 de las columnas agregar un dato
                m3[i].append(m1[i][j] + m2[i][j]) # se indica que el dato que rellenara la matriz sera la suma de las dos matrices y se la agrega a la posicion
        return m3 #retorna la matriz creada
    else:
        return None # retorna none, que significa que las matrices son de diferente tamaño

c = sumar_matrices(a, b) # Se le da nombre a la funcion antes creada
if c == None: # se usa condicional que dice que si da none en la funcion se imprima
    print('No se pueden sumar') #imprime que no se púeden sumar
else: # segunda condicion donde se imprime la matriz anteriormente sumada
    for fila in c: # se dice que para para fila en la matriz le imprima un corchete y un espacio para darle orden
        print("[", end=' ') # imprime el corchete y el espacio
        for elemento in fila: # se dice que para cada elemento en la fila, imprima el elemento mas un espacio
            print(elemento, end=' ') # imprime el elemento y el espacio
        print("]")    # imprime el corchete final
