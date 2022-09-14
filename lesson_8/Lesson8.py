#1
from decimal import DivisionByZero

def checker(var):
    if type(var) != float:
        raise TypeError("not a float")
    else:
        print("thats a float")

#2
def var_maker():
    intvar=input("Enter an intager: ")
    try:
        intvar = int(intvar)
        print(intvar)
    except Exception:
        try:
            print("Sorry, not an int")
            #intvar=int(input("Enter an intager: "))
            int(input("Enter an integer: ")) % 2 != 0
            raise Exception('Even numbers are not allowed')
        except Exception as v:
            print(v)
#3
def my_func(x,y):
    try:
        sum = x / y
        print(sum)
    except ZeroDivisionError:
        print("Divition by zero is not allowed")
    except TypeError:
        print("y is a string")

#4
from math import sqrt
#print(sqrt(16))

from random import randint
x = randint(1,10)
#print(x)

from calc import add
#print(add(7,2))

#5
mylist=list(range(1,11))
#print(mylist)

print(list(map(lambda temp: temp + 1, list(range(1,11)))))
#print(mylist)