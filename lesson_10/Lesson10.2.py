class Animal:
    def __init__(self):
        pass

    def __str__(self):
        return "Animal"

class Menu:
    my_animal = None
    menu_text = """
'-------------------------'
'------- Main Menu -------'
'-------------------------'

1: 'Create object',
2: 'Print object',
3: 'Delete object'
"""

    def menu_loop(self):
        self.running = True
        while self.running:
            print(Menu.menu_text)
            choice = self.user_input()
            self.menu_choice(choice)

    def menu_choice(self, choice):
        if choice == 1:
            self.my_animal = Animal()
            print("*** Animal created ***")

        elif choice == 2:
            if not self.my_animal:
                print("*** No object available to print ***")
            else:
                print(self.my_animal)

        elif choice == 3:
            if self.my_animal:
                del(self.my_animal)
                print("*** Deleted ***")
            else:
                print("*** No object to delete ***")

    def user_input(self):
        try:
            return int(input("Enter your choice:\n: "))
        except:
            print("*** Somethig went wrong ***")
            pass

if __name__ == '__main__':
    Menu().menu_loop()

