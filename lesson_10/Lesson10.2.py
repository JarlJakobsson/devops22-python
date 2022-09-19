class Animal:
    def __init__(self):
        pass

    def __str__(self):
        return "Animal"

class Menu:
    my_object = None
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
            self.my_object = Animal()
            print("Created Animal")

        elif choice == 2:
            if not self.my_object:
                print("No object available to print")
            else:
                print(self.my_object)

        elif choice == 3:
            if self.my_object:
                del(self.my_object)
                print("Deleted")
            else:
                print("No object to delete")

    def user_input(self):
        return int(input("Enter your choice:\n: "))

if __name__ == '__main__':
    Menu().menu_loop()

