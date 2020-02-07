''' Definir una funcion que dadas dos matrices cacule su multiplicación:
-- Para poder multiplicar dos matrices, las columnas de la primera matriz deben ser igual a las columnas de la segunda.
-- el resultado sera una matriz de orden de filas de la primera por columnas de la segunda
'''
#Ej: El consumo de los animales de una granja, por el precio de los productos de dos tiendas, para saber el coste de sus productos.
'''
    consumo de la granja
            trigo  cebada  pienso    
    vacas  [   21     18      35  ]
    cerdos [   19     11      21  ]

    precio de productos
                tienda1   tienda2
    trigo   [    0.65      0.58     ]
    cebada  [    0.45      0.49     ]
    pienso  [    1.27      1.32     ]


    Resultado = Coste de productos
                tienda1     tienda2
    vacas      [   66.2       67.2   ]
    cerdos     [  43.97     44.13    ]


'''
a =[[1, 2, 3],
    [4, 5, 6]]
b =[[1, 2],
    [3, 4],
    [5, 6]]


def multiplicar_matrices(m1, m2): #se define la funcion, toma dos parametros, que son las matrices que se van a multiplicar
    if len(m1[0]) == len(m2): #Se condiciona para saber si se puede multiplicar, se dice que la longitud de las filas de la primera es igual a las columndas de la sunda matriz, si no se cumple esto, no se pueden multiplicar
        m3=[]     #se crea una matriz que tenga las dimensiones de las filas de la primera por las columnas de la segunda
        for i in range(len(m1)):
            m3.append([])
            for j in rango(len(m2[0]): 
                m3[i].append(0)































