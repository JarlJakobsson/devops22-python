first_number = 4#int(input("Enter an integer: "))
second_number = 5#int(input("Enter an integer: "))
add = first_number + second_number
sub = first_number - second_number
mult = first_number * second_number
div = first_number / second_number

first_number = str(first_number)
second_number = str(second_number)
add = str(add)
sub = str(sub)
mult = str(mult)
div = str(div)

print(first_number + " + " + second_number + " = " + add)
print('%s' % first_number + " - " + second_number + " = " + sub)
print('{} * {} = {}'.format(first_number, second_number, mult))
print(f'{first_number} / {second_number} = {div}')