
#x=100
#for i in range(x):
#    num=0
#    for y in range(2,( i//2+1)):
#        if(i % y == 0):
#            num=+1
#            break
#    if (num==0 and i < 1):
#            print(num)
#    if i > 1 and not i % 2 == 0 and not i % 3 == 0 and not i%5==0 and not i%7==0:
#        print(i)
#else:
#
from typing import Counter


x=100
for i in range (x):
    counter = 0
    for y in range(2, (i//2 + 1)):
        if(i % y == 0):
            counter=+1
            break

    if (counter == 0 and i > 1):
        print(i)