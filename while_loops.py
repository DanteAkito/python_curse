"""a = 3

while a > 0:
    print(1)
    print(2)

"""

#user = '' # asignamos una variable (string) vacia

"""while user != "Dante": #Mientras la variable user no sea igual al str "Dante" no salir del loop
    user = input("Enter ur user: ") #se pide al usuario ingresar una cadena de string 
"""



while True: #Mientras esto se cumpla, seguira en loop
    user = input("Enter user: ") #pide una cadena de string al usuario
    if user == "Dante": # condiciona a que si el user name es igual a Dante o no, se cumpla lo que sigue en la siguiente linea
        break     # Rompe el loop, si lo de arriba se cumple
    else:
        continue  # Continua el loop, si lo de arriba no se cumple

# LA DIFERENCIA ENTRE LAS DOS FORMAS ES QUE AUNQUE LAS DOS HACEN LO MISMO, CON LA SEGUNDA SE MANEJA MEJOR EL CONTROL DE FLUJO DE TRABAJO Y MEJOR SYNTAXIS.    