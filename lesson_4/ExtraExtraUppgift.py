message=input("Enter message you want to encrypt: ")
shift = int(input("Enter how many times you want to shift your message: "))
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for c in message:
    if c not in alphabet:
        print(c, end='')
        continue
    shiftedindex = (alphabet.index(c)+shift) % len(alphabet)
    print(alphabet[shiftedindex], end='')