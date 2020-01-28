#print()
#dir()
#type()
#len() 
#lambda :

def hello(name= 'Human'):
    print("Hello " + name)

hello("Dan")
hello('Roger')
hello('Max')
hello()

def add(number_one, number_two):
    return number_one + number_two

print(add(20, 20))
print(add(400,500))