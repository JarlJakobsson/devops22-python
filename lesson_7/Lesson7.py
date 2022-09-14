from lib2to3.pgen2.token import NEWLINE
import numbers
from operator import itemgetter, mul
from random import randint, shuffle, choices, sample
from stringprep import c22_specials
from tokenize import Number
from typing import Counter
import string
import random
from collections import deque

#1.1.1
def do_nothing():    
    pass
#1.1.2
do_nothing()

#2.2.1
def hello_world():
    print("hello world")

#2.2.2
def bool_func():
    print(1 == 1.0)

#2.2.3
def alphabet_func():
    print("* REVERSE ALPHABET *")
    print(string.ascii_lowercase[::-1])

#1.3.1
def hello_name(name):
    print(f"hello {name}")

#1.3.2
def to_upper(word=""):
    print(word.upper)

#1.3.3
def print_numbers(stop):
    for i in range(1, stop):
        print(i)

#2.1
def print_range(start=1,stop=11):
    for i in range(start, stop):
        print(i)

#2.2
def reverser(reverse=False):
    default_string = "ABCD"
    if reverse == True:
        print(default_string[::-1])
    else:
        print(default_string)

#2.3
reverser()
reverser(True)

#3.1
def return_int():
    return 1

#3.2
def return_tupple(x,y):
    return(x,y)

#3.3
def return_bool():
    return True

#3.4
def return_float():
    return 1.2

#3.5
def fullname(firstname, lastname):
    return f'{firstname} {lastname}'


#3.6
def area(height,width):
    return f'{int(height) * int(width)}'

#3.7
def list_sum(list):
    sum = 0
    for i in range(len(list)):
        sum = sum + int(list[i])
    print(sum)

#3.8
def repeater(word, repeat):
    print(word * repeat)

