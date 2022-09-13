from operator import itemgetter, mul
from random import randint, shuffle, choices, sample
from stringprep import c22_specials
from typing import Counter
import string
import random
from collections import deque

#1.1
num = [i for i in range(1, 101)]
#print(num)

#1.2
numb = [i for i in range(1,61)]
even_num = []
for i in numb:
    if i % 2 == 0:
        even_num.append(i)
#print(even_num)

#1.3
odd_num = [i for i in range(1,78) if i % 2 != 0]
#print(odd_num)

#1.4
random_list = random.sample(range(1, 301), 100)
#print(random_list)

first_list = ["Green", "White", "Black", "Yellow", "Blue"]
second_list = ["Red"]

#1.5.1
#first_choice = random.choice(first_list)
#second_choice = random.choice(first_list)
#second_list.append(first_choice)
#second_list.append(second_choice)

second_list.extend(random.choices(first_list, k = 2))
#print(second_list)

#1.5.2
third_list = choices((second_list), k = 50)
#print(third_list)

#1.5.3
c = Counter(first_list + second_list + third_list)
too_dict = dict(c)
#print("* TOTAL ELEMENTS *")
#print(len(first_list + second_list + third_list))
#print("* UNIQUE COLORS *")
#print(*Counter(first_list + second_list + third_list))

#2.1
names = ["johan", "lisa", "johan", "tove", "markus"]
names = random.choices((names), k = 100)
#print(names)

#2.2
c = Counter(names)
#print("* COUNTER *")
#print(Counter(names))

#2.3
#print(c.most_common(3))

#2.4
#print(c.most_common()[-1])

#2.5.1
dict_names = dict(c)
#print("* SORTED NAMES *")
#print(sorted(dict_names))

#2.5.2
list_names = list(dict_names)
#shuffle(list_names)
#print("* SHUFFLED NAMES *")
#print(list_names)

#2.5.3
reverse_list = sorted(list_names, reverse = True)
#print("* REVERSE SORTED NAMES *")
#print(reverse_list)

#3.1
alphabet = list(string.ascii_lowercase)

#3.2
alphabet_stack = []
for i in range(len(alphabet)):
    alphabet_stack.append(alphabet[i])
#print("* STACK *")
#print(alphabet_stack)

#3.3
popped_string = ""
for x in range(len(alphabet)):
    popped_string = popped_string + (alphabet_stack.pop(0))
#print(popped_string)

#4.1
names_two = ["lisa", "olle", "pelle", "johan", "markus"]
names_two = random.choices((names), k = 50)

#4.2
queue = deque(names_two, maxlen=10)
print("* ORIGINAL QUEUE *")
print(queue)

#4.3
rand_num = random.randint(0,len(queue))
print("* RANDOM NUMBER *")
print(rand_num)

for i in range(rand_num):
    queue.pop()
print("* POPPED QUEUE *")
print(queue)

#4.4
queue.extend(random.choices((names_two), k = rand_num))
print("* NEW QUEUE *")
print(queue)
print("* NAMES TWO *")
print(names_two)
    