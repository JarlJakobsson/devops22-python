salary = 5000
print(f'Your salary is {salary} \u20AC.') #4.1
suggestion = int(input("How much more do you want?")) #4.2
increase = (suggestion / salary) * 100
print(f'Thats a {increase}% increase.\nNo. \N{slightly smiling face}') #4.3

while True: #4.4 and 4.5
    suggestion = int(input('Try again: '))
    increase = (suggestion/salary) * 100
    if increase > 20:
        increase = (suggestion/salary) * 100
        print(f'Thats a {increase}% increase.\nNo. \N{slightly smiling face}')
        continue
    else:
        print(f'Thats a {increase}% increase.\nK. \N{slightly smiling face}')
        break