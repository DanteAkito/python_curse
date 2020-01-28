# 1 Own modules
# 2 Third party modules
# 3 python modules


'''import datetime

print(datetime.datetime.today())
print(datetime.timedelta(minutes=70))'''

from datetime import timedelta, date
#import fmath 
from fmath import add, subs
#import colorama
from colorama import Fore, Style, init
init(convert=True)
print(Fore.RED + "Hello")
print(timedelta(minutes=100))
print(date.today())

subs(1,4)
add(1,6)

#fmath.add(1,3)
#fmath.subs(1,5)
