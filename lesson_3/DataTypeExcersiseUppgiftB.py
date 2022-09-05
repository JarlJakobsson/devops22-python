

from operator import itemgetter


person1name = input("Enter name: ").lower()
person1age = input("Enter age: ")
person1shoe = input("Enter shoe size: ")

person1data = (person1name, person1age, person1shoe)

person2name = input("Enter name: ").lower()
person2age = input("Enter age: ")
person2shoe = input("Enter shoe size: ")

person2data = (person2name, person2age, person2shoe)

person3name = input("Enter name: ").lower()
person3age = input("Enter age: ")
person3shoe = input("Enter shoe size: ")

person3data = (person3name, person3age, person3shoe)

persondata = []
persondata.append(person1data)
persondata.append(person2data)
persondata.append(person3data)

#lämnar kvar lite saker som jag testade
#persondata = {person1name: (person1age, person1shoe), person2name : (person2age, person2shoe), person3name : (person3age, person3shoe)}

#persondata: persondata = {v[0]: k for k, v in persondata.items()}
#asd = dict(sorted(persondata.items(), key=lambda item: item[1]))

age = sorted(persondata, key=itemgetter(1)) #Gör en sorterad lista efter ålder
shoe = sorted(persondata, key=itemgetter(2)) #Gör en sorterad lista efter skostorlek

oldest = age[-1]        #Skapar en variabel för den äldsta personen
medianshoe = shoe[1]    #Skapar en variabel för personen med madian skostorlek
print(oldest)

print(f"{oldest[0].capitalize()} is the oldest and his shoe size is {oldest[2]}.") #Skriver ut element [0] i oldest för att få namnet och element[2] för att få ut skostorleken
print(f"{medianshoe[0].capitalize()} have the median shoe size and he is {medianshoe[1]} years old.")

#Skapar ett dictionary som jag kan använda för sökningen
searchdata = {
    "name": {
        str(person1name): person1data,
        str(person2name): person2data,
        str(person3name): person3data
    },
    "age": {
        str(person1age): person1data,
        str(person2age): person2data,
        str(person3age): person3data},
    "shoesize": {
        str(person1shoe): person1data,
        str(person2shoe): person2data,
        str(person3shoe): person3data
    }
}
prop, value = input("Enter name/age/shoesize followed by value(Use lowercase): ").split(" ") #Skapar variabeln prop och value. prop får värded av första strängen i inputen och value får den andra strängen då jag använder split vid mellanrum (" ")
print(searchdata[prop][value])

#sökningen fungerar endast vid exakt input ifrån användaren. Den är case-sensative