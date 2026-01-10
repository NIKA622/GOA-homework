word = ["Dato", "Saba", "luka", "gio", "Zurabi"]
Upper_name = []
for i in word:
    if i == i.capitalize():
        Upper_name.append(i)
print(Upper_name)


# task2
names = ["sandro", "irakli", "nino", "vano", "salome", "ilia"]
surname = ["Beridze", "Kapanadze", "Japaridze"]
for i in names:
    if i == i.lower():
        print(i.upper())

for i in surname:
    if i == i.capitalize():
        print(i.lower())

for i in range(1):
    if 10 == 10:
        surname.append(names)
        print(surname)


# task3
words = ["velosipedi", "kata", "kompiuteri", "APPLE"]
for i in words:
    if len(i) <= 6 or i == i.upper():
        words.remove(i)
print(words)


# task4
num = [15.5, 9.9, 55.55, 101.1, 20.2, 88.8, 7.7, 66.6, 120.3, 33.3]
clear = []
for i in num:
    if i >= 10 and i <= 100:
        clear.append(i)
print(clear)


# task5
cities = ["LONDON", "MADRID", "BERLIN", "VIENNA", "PRAGUE"]
countries = ["SPAIN", "AUSTRIA", "CZECHIA", "POLAND", "SWEDEN", "NORWAY", "DENMARK", "FINLAND", "ICELAND", "ESTONIA"]
for i in range(0,5):
    countries.append(cities[i])
print(countries)
