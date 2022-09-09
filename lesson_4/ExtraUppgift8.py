
x=100
for i in range (x):
    counter = 0
    for y in range(2, (i//2 + 1)):
        if(i % y == 0):
            counter=+1
            break
    if (counter == 0 and i > 1):
        print(i)