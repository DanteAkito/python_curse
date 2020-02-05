x = int(input("Enter a number: "))
z = range(2, x)

for y in z:
    if (x % y) == 0 :
        print("es divisible")
    else :
        print("nada")

