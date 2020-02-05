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


friday_temperatures = [9.1, 8.8, 7.5, 6.6, 9.9]
len(friday_temperatures) #len(obj, /) Return the number of items in a container. 
friday_temperatures[3]
friday_temperatures[1:4]
friday_temperatures[0:2]
friday_temperatures[:2]
print(friday_temperatures)
""" friday_temperatures[3]
6.6
>>> friday_temperatures[1:4]
[8.8, 7.5, 6.6]
>>> friday_temperatures[0:2]
[9.1, 8.8]
>>> friday_temperatures[:2]
"""  

mystring = 'hello'
mystring[1]
mystring[-1]
mystring[:3]

"""mystring = 'hello'
>>> mystring[1]
'e'
>>> mystring[-1]
'o'
>>> mystring[:3]
'hel' 

Summary: Positive/Negative Indexes, Slicing
In this section you learned that:

Lists, strings, and tuples have a positive index system:

["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
   0      1      2      3      4      5      6
And a negative index system:

["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  -7     -6     -5     -4     -3     -2     -1
In a list, the 2nd, 3rd, and 4th items can be accessed with:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[1:4]
Output: ['Tue', 'Wed', 'Thu']
First three items of a list:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:3]
Output:['Mon', 'Tue', 'Wed'] 
Last three items of a list:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[-3:]
Output: ['Fri', 'Sat', 'Sun']
Everything but the last:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-1] 
Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 
Everything but the last two:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-2] 
Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'] 
A single in a dictionary can be accessed using its key:

phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
phone_numbers["Marry Simpsons"]
Output: '+423998200919'


def (create own funtion)
"""
def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean

print(mean([1, 2, 3]))

"""
Bonus Code: Using "and" and "or" in a Conditional
You learned to check for one single condition:

x = 1
 
if x == 1:
    print("Yes")
else:
    print("No")
You can also check if two conditions are met at the same time using an and operator:

x = 1
y = 1
 
if x == 1 and y==1:
    print("Yes")
else:
    print("No")
That will return Yes since x == 1 and y ==1 are both True.

You can also check if one of two conditions are met using an or operator:

x = 1
y = 1
 
if x == 1 or y==2:
    print("Yes")
else:
    print("No")
That will return Yes since at least one of the conditions is True. In this case x == 1 is True.
"""
"""
student_grades = []

You can create a list of numbers automatically using a range. For example:

list(range(1, 10))

That will output:

[1, 2, 3, 4, 5, 6, 7, 8, 9]

As you can see we just needed to specify the list boundaries inside range(). So, we specified 1and 10. Note that 10 is not included in the list. The generated list always runs up to one number before the upper number. In our example it goes up to 9 since the upper number is 10.

You can also specify a step as a third argument:

list(range(1, 10, 2))

That will output:

[1, 3, 5, 7, 9]

So, the count happens every two items starting from 1 and ending at 9.


student_grades = [2, 3.5, 8.9]
mysum = sum(student_grades)

length = len(student_grades)

mean = mysum / length

print(mean)
student_grades = [9.1, 8.8, 7.5]
max_value = max(student_grades)
print(max_value)

"""

"""Summary: Processing User Input
In this section you learned that:

A Python program can get user input via the input function:

The input function halts the execution of the program and gets text input from the user:

name = input("Enter your name: ")
The input function converts any input to a string, but you can convert it back to int or float:

experience_months = input("Enter your experience in months: ")
experience_years = int(experience_months) / 12
You can format strings with (works both on Python 2 and 3):

name = "Sim"
experience_years = 1.5
print("Hi %s, you have %s years of experience." % (name, experience_years))
Output: Hi Sim, you have 1.5 years of experience.

You can also format strings with (Python 3 only):

name = "Sim"
experience_years = 1.5
print("Hi {}, you have {} years of experience".format(name, experience_years))
Output: Hi Sim, you have 1.5 years of experience. 


For Loop Over a Function
Note that using loops you can call any function multiple times, even your own functions. Let's suppose we defined this function:

def celsius_to_kelvin(cels):
    return cels + 273.15
That is a function that gets a number as input, adds 273.15 to it and returns the result. A for loop allows us to execute that function over a list of numbers:

monday_temperatures = [9.1, 8.8, -270.15]
 
for temperature in monday_temperatures:
    print(celsius_to_kelvin(temperature))
The output of that would be:

282.25
281.95
3.0

So, in the first iteration celsius_to_kelvin(9.1) was executed, in the second celsius_to_kelvin(8.8) and in the third celsius_to_kelvin(-270.15).

That's just something to keep in mind.



