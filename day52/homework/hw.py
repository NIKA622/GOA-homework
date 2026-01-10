#2



text = "PyThOn"
result = []

i = 0
while i < len(text):
    if text[i].isupper():
        result.append(text[i].lower())
    else:
        result.append(text[i].upper())
    i += 1

print(result)



#3
names = ["nika", "GIO", "luka", "ANNA"]
result = []

for name in names:
    if name.islower():
        result.insert(0, name.upper())  
    elif name.isupper():
        result.append(name.lower())     

print(result)




#4
cities = ["TBILISI", "batumi", "KUTAISI", "zugdidi"]

i = 0
while i < len(cities):
    if cities[i].isupper():
        cities.pop(i)            
    else:
        cities[i] = cities[i].upper()
        i += 1

print(cities)



#5
surnames = ["nikauri", "GELASHVILI", "beridze", "TSIKLAURI"]

i = 0
while i < len(surnames):
    word = surnames[i]

    if word.islower():
        surnames.pop(i)
        surnames.insert(i + 1, word.upper())
        i += 2

    elif word.isupper():
        surnames.pop(i)
        if i - 1 < 0:
            surnames.insert(0, word.lower())
            i += 1
        else:
            surnames.insert(i - 1, word.lower())
            i += 1
    else:
        i += 1

print(surnames)
