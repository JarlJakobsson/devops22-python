
firstname = "john"
lastname = "smith"
tele = "00468123456789"

print(firstname + " " + lastname + " " + tele) #1.1
fullname = "" #1.2
fullname = firstname + " " + lastname #1.3
print(len(fullname + firstname + lastname)) #1.4
print(f'{fullname} \n{tele}') #1.5
print(fullname + " " + tele) #1.6.1
print(f'{fullname} {tele}') #1.6.2
print('{} {}'.format(fullname, tele)) #1.6.3
print('%s' % fullname + " " + tele) #1.6.4

print(fullname[:5]) #2.1
print(fullname[1:-1]) #2.2
print(fullname[::2]) #2.3
print(fullname[::-1]) #2.4
print(fullname[4:5]) #2.5