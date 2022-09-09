from re import X


cost=int(input("How much did it cost: ")) #3.1
print(f'{cost} \u20AC') #3.2
if cost > 50000:
    print("\N{CLOWN FACE}")
else:
    print("\U0001F973") 