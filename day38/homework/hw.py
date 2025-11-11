# 1) 
name = input("შეიყვანე შენი სახელი: ")
print(name.upper())  


# 2) 
name = input("შეიყვანე შენი სახელი დიდი ასოებით: ")
print(name.lower())  


# 3) 
name = input("შეიყვანე შენი სახელი პატარა ასოებით: ")
print(name.capitalize())  


# 4) 
names = ["goga", "nika", "luka", "saba"]
for i in range(len(names)):  
    print(names[i].upper())


# 5) 
names = ["GOGA", "NIKA", "LUKA", "SABA"]
for i in range(len(names)):
    print(names[i].lower())


# 6) 
names = ["goga", "nika", "luka", "saba"]
for i in range(len(names)):
    print(names[i].capitalize())


# 7) 
items = ["ვაშლი", "ბანანი", "მსხალი", "ატამი"]
print("სიის სიგრძე არის:", len(items))


# 8) 
name = "ალექსანდრე"
print("სტრინგის სიგრძე არის:", len(name))


# 9) ს
numbers = [2, 5, 8, 11, 14, 17, 20]
even_count = 0
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_count += 1
print("ლუწი რიცხვების რაოდენობაა:", even_count)


# 10) 
numbers = [2, 5, 8, 11, 14, 17, 20]
odd_count = 0
for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        odd_count += 1
print("კენტი რიცხვების რაოდენობაა:", odd_count)


# 11) 
start = int(input("შეიყვანე start: "))
end = int(input("შეიყვანე end: "))
step = int(input("შეიყვანე step: "))

for i in range(start, end, step):
    if i % 2 == 0:
        print(i)
