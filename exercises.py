#Exercise 1: Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

'''name = input("What's your name?: ")
print("Hi! " + name)''' 

#Exercise 2: Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

'''name = input("What's your name?: ")
number = input("type a integer number please: ")
number_int = int(number)
print (name * number_int)''' 

#Exercise 3: Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

'''name = input("What's your name?: ")
number = input("type a integer number please: ")
number_int = int(number)
print ((name + "\n") * number_int)'''

#Execise 4: Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.

name = input("What's your name?: ")
n1 = len(name)

print (name.upper() + " has " + str(n1) + " letters. ")

