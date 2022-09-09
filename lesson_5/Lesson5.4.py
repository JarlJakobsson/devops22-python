salary = 5000
print(f'Your salary is {salary}.') #4.1
suggestion = 2000 #int(input("How much more do you want?")) #4.2
increase = (suggestion / salary) * 100
print(f'Thats a {increase}% increase.\nNo. \N{slightly smiling face}') #4.3

while True:
    suggestion = int(input('Try again: '))
    increase = (suggestion/salary) * 100
    if increase > 30:
        #print(f'Thats a {increase}% increase.\nNo. \N{slightly smiling face}')
        #suggestion=int(input("Try again"))
        increase = (suggestion/salary) * 100
        print(f'Thats a {increase}% increase.\nNo. \N{slightly smiling face}')
        continue
    else:
        print("K")
        break