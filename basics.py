import datetime
mynow = datetime.datetime.now()
print("The date and time is :", datetime.datetime.now())
print(mynow)
mynumber = 31
mytext = "fuck"
print(mynumber, mytext) 
x = 10
y = "10"

#Uso de variables. el signo (-) menos es reservado como operador de python

#Listas

sum1 = x + x
sum2 = y + y
print(sum1, sum2)

student_grades = (9.1, 8.8, 7.5,10, 6.8, 8.1, 10)

mysum = sum (student_grades)
length = len(student_grades)
mean = mysum / length
print(mean)

#Calcular maximo

max_value = max(student_grades)
print(max_value)

#Contador
print(student_grades.count(10.0))

#Minúsculas
username = "Python3"
print(username.lower())

#Mayúsculas
username = "Python3"
print(username.upper())

#Dictionary

day_temperatures = {'morning':10.1, 'noon':20.2, 'evening':15.3}

#morning, noon, evening are keys and the numbers are float values.

#Tuple (Ordered list). 
""" Asing a dictionary to variable. 
The dictionary should contain three keys and each key contain a tuple as value. 
Each tuple contain three floats"""

day_temperatures ={'morning':(10.1,9.2,7.3), 'noon':(6.4,4.5,3.6), 'evening':(2.7,1.8,0.9)}

"""
Integers are for representing whole numbers:

rank = 10
eggs = 12
people = 3
Floats represent continuous values:

temperature = 10.2
rainfall = 5.98
elevation = 1031.88
Strings represent any text:

message = "Welcome to our online shop!"
name = "John"
serial = "R001991981SW"
Lists represent arrays of values that may change during the course of the program:

members = ["Sim Soony", "Marry Roundknee", "Jack Corridor"]
pixel_values = [252, 251, 251, 253, 250, 248, 247]
Dictionaries represent pairs of keys and values:

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
volcano_elevations = {"Glacier Peak": 3213.9, "Rainer": 4392.1}
Keys of a dictionary can be extracted with:

phone_numbers.keys()
Values of a dictionary can be extracted with:

phone_numbers.values()
Tuples represent arrays of values that are not to be changed during the course of the program:

vowels = ('a', 'e', 'i', 'o', 'u')
one_digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
To find out what attributes a type has:

dir(str)
dir(list)
dir(dict)
To find out what Python builtin functions there are:

dir(__builtins__)
Documentation for a Python command can be found with:

help(str)
help(str.replace)
help(dict.values)

python words

and	del	for	is	raise	assert
if	else	elif	from	lambda	return
break	global	not	try	class	except
or	while	continue	exec	import	yield
def	finally	in	print


"""







#Uso de variables. el signo (-) menos es reservado como operador de python

tuesday_temperatures = [10.1, 8.8, 7.5]
tuesday_temperatures.append(15.2)  #append object to the end of the list.
print(tuesday_temperatures)

# = [10.1, 8.8, 7.5, 15.2]
#Clear() Remove all items from the list.
tuesday_temperatures.clear()


