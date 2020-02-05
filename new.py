#Examen 

def sentence(phrase):                         # Definir funcion "sentence" variable phrase                      
    interrogatives = ("how", "what", "why")   # Definir variable interrogatives para saber si es pregunta
    capitalized = phrase.capitalize()         # Capitalizar la frase entrante "phrase"
    if phrase.startswith(interrogatives):     # Condicionar la frase con el metodo .starswith() "que mira con que empieza el string, que en este caso seria 'interrogatives'" 
        return "{}?".format(capitalized)      # Devuelve el string formateado y capitalizado se le agrega el signo de interrogacion, por que es una pregunta
    else:
        return "{}.".format(capitalized)      # Devuelve el string capitalizado y formateado con un punto. 

results = []                                  # Crear una lista, que el usuario se encargara de agregar
while True:                                   # Loop que define, si mientras se cumple lo que aqui propone, sigue ejecutandose
    x = input("Say something: ")                  # pide al usuario que ingrese algo      
    if x == "/end":                           # Dice que si lo que ingresa el usuario es igual a "/end" detenga el bucle 
        break                                 # la palabra reservada de python que detiene el bucle  
    else:                                     # Palabra reservada de python que hace que el bucle cumpla otra tarea 
        results.append(sentence(x))           # Agrega lo que ingresa el usuario a la lista "results" y llama a la funcion "sentence" "que capta si la oracion empieza por un interrogante o si es una oracion normal y le agraga lo que lleva dichas oraciones"

print(" ".join(results))                       # Imprime en pantalla el resultado mas un espacio generado por el string vacio con la funcion ".join" que agregara un espacio por cada oracion que ingrese el usuario


# Se define una funcion en la parte superior que identifica si las oraciones igresadas por el usuario son preguntas u oraciones y les agrega sus respectivos signos de puntuacion e identificacion a continuacion se hizo un loop que pide a usuario una oracion que si es igual a "/end" se detiene, te lo contrario se cumple la condicion a continuacion 


"""

if phrase.startswith(("how", "what", "why")) 


while True: 
    x = input("Say something: ")
    if x == "/end":
        break  
    else:
        z = x.lower().capitalize() + '.'
        y = a.lower().capitalize() + '?'
        m = b.lower().capitalize() + '.'



    a = input("Say something: ")
    b = input("Say something: ")
    if x or a or b == "/end": 
        break    
    else:
        print (z + y + m)
        z = x.lower().capitalize() + '.'
        y = a.lower().capitalize() + '?'
        m = b.lower().capitalize() + '.'
    continue  
"""