x = int(input("Enter a number: "))
z = range(2, x)

for y in z:
    if (x % y) != 0 :
        continue     
    else:
        print("No es primo")
    break
else:
    print("Es primo")    

