class Person:
    def __init__(self, street_name, street_number, postal_code, country):
        self.street_name = street_name
        self.street_number = street_number
        self.postal_code = postal_code
        self.country = country
        self.adress = self.street_name, self.street_number, self.postal_code, self.country

    # def adress(self):
    #     adress = self.street_name, self.street_number, self.postal_code, self.country
    #     return adress

class Employee(Person):
    def __init__(self, adress, employee_number, salary):
        super.__init__(adress)
        self.employee_number = employee_number
        self.salary = salary

class Person2:
    def __init__(self, street_name, street_number, postal_code, country):
        self.street_name = street_name
        self.street_number = street_number
        self.postal_code = postal_code
        self.country = country
        self.adress = self.street_name, self.street_number, self.postal_code, self.country

class Employee2(Person2):
    def __init__(self, adress, employee_number, salary):
        self.employee_number = employee_number
        self.salary = salary
        self.adress = adress

def main():
    employee = Employee2(Person2())