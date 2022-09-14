int_input = int(input("Enter an integer: "))
if int_input > 5 :
    print(f"{str(int_input)*int_input}")

if int_input <= 5:
    counter = 0
    for i in range(int_input):
        counter += 1
        print(f"{str(counter)*counter}")

def my_func(int_input):
    if int_input > 5 :
        print(f"{str(int_input)*int_input}")

    if int_input <= 5:
        counter = 0
        for i in range(int_input):
            counter += 1
            print(f"{str(counter)*counter}")

