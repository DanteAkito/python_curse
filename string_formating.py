#user_input  = input("Enter your name: ")
#message = "Hello %s" % user_input  OLD
#message = f"Hello {user_input}"  NEW 3.6 or greather
#print(message)

#Multiple

name = (input("Enter your name: "))
last_name = (input("Enter your last name: "))
when = (input("Enter day: "))
#message = "Hello %s %s" % (name, last_name) #OLD
message = f"Hello {name} {last_name}.  What´s up on {when}?"  #NEW
print(message)


#for key, value in phone_numbers.items():
    #print("{}: {}".format(key, value)) #another way

    phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for keys, values in phone_numbers.items():
    
    print(values.replace("+", "00"))