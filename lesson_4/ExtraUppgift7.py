
fruits=['apple','orange','pear','banana','grapes']
x=int(input("Enter how many slots your basket has: "))
#fruits=[fruits.extend(fruits) for i in range(x)] vet inte varför det inte funkade
for i in range(x):
    fruits.extend(fruits)
mybasket=[fruits[x] for x in range(x)]
print(mybasket)
