
X = 1
Y = 4
adresses = {"Adam": "Ormvägen 5",
                "Bella":"Klockgatan 1",
                "Cornelia":"Vikingatan 3"}

cars = ["Volvo", "Opel","BMW"]
numbers1 = {1,2,3,X,6}
numbers2 = {Y,2,3,4,7}

adresses["Daniel"] = "Prinsgränd 2"

sortedList = list(sorted(adresses))
lastName = (sortedList[-1])
print(adresses[lastName])

adressesList = list(sorted(adresses.values()))
firstStreet = adressesList[0]
adresses: adresses = {v: k for k, v in adresses.items()}
print(adresses[firstStreet])

cars_2 = cars
cars.append("Saab")
cars_3 = cars.copy()

cars.extend(cars)
cars.sort(reverse=True)
unique_cars = list(dict.fromkeys(cars))

print(adresses)



#1 print(type(adresses)) svar: int
#2 print(adresses["Bella"]) svar: dict
#3 print(adresses["Bella"])
#4 Man lägger till Daniel i dictonaryn och ger honom adressen Prinsgränd 2
#5 print(len(adresses))
#6 print(type(cars)) svar: list
#7 Element [1] returneras då X=1, vilket returnerar Opel
#8 Det finns bara 3 element i cars, så 4 ligger utanför index
#9 cars sorteras i bokstavsordning och returnerar sedan Element [0] vilket är BMW
#10 cars och cars_2 innehåller Volvo, Opel, BMW och Saab. cars_2 innehåller också Saab eftersom den bara refererar till cars
#11 numbers1 och numbers2 är sets
#12 numbers1 har värdena 1,2,3,6 och numbers 2 har värdena 2,3,4,7 X och Y påverkar inte setten
#13 print(numbers1.intersection(numbers2)) {2,3} finns i båda setten
#14 print(numbers1.union(numbers2)) {1, 2, 3, 4, 6, 7} Är alla unika värden som finns i numbers1 och numbers2
#15 print(numbers1.symmetric_difference(numbers2)) {1, 4, 6, 7} Är alla värden som inte finns i både numbers1 och numbers2
