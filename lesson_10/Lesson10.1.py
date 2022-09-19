#1
class Myclass:
    def __init__(self) -> None:
        pass

    def my_func(self):
        return print("Myclass func")

class Mysubclass(Myclass):
    def __init__(self):
        pass

    def my_func(self):
        return print("Mysubclass func")

obj1 = Myclass()
obj2 = Mysubclass()

obj1.my_func()
obj2.my_func()