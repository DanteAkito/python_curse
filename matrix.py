consumo = [ [21, 18, 35, 40],
            [19, 11, 21, 14],
            [12, 15, 20, 30] ]

for listas in consumo: #Consumo tiene 3 listas, para cada lista en consumo,
    print("[", end=' ') # Se le agrega un "[" y un espacio
    for elemento in listas: #Para cada elemento detro de cada lista
        print(elemento, end=' ') #Imprime el elemento y un espacio
    print("]") # Imprime "]" 


