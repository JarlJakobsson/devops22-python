
x=15
guess=int(input("Enter an integer: "))
while True:
    if guess==15:
        print("Congratulations, you guessed correct!")
        break
    elif guess < x :
        print("Wrong, the correct number is higher.")
        guess = int(input("Guess again: "))
    else:
        print("Wrong, the correct number is lower.")
        guess=int(input("Guess again"))