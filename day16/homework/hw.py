# 1) მომხმარებლის რიცხვის შემოწმება
num = float(input("შემოიყვანე რიცხვი: "))
if num > 0:
    print("ეს რიცხვი დადებითი რიცხვია")
elif num < 0:
    print("ეს რიცხვი უარყოფითი რიცხვია")
else:
    print("ეს რიცხვი ნულია")

print("-" * 40)

# 2) ასაკის შემოწმება
age = int(input("შემოიყვანე შენი ასაკი: "))
if age < 0:
    print("არასწორი ინფო")
elif 0 <= age <= 12:
    print("ბავშვი ხარ")
elif 13 <= age <= 19:
    print("მოზარდი/თინეიჯერი ხარ")
elif 20 <= age <= 64:
    print("ზრდასრული ხართ")
elif 65 <= age <= 120:
    print("ხანში შესული ხართ")
else:
    print("გურუ ან ჯადოქარი")

print("-" * 40)

# 3) Password guesser
secret_password = "giajonjoli"
tries= 0
while True:
    guess = input("გამოიცანი პაროლი ან დაწერე 'nah strong password': ")
    tries += 1
    if guess == secret_password:
        print(f"გილოცავ! გამოიცანი პაროლი  ცდაში!")
        break
    elif guess == "nah strong password":
        print(f"შენ შეწყვიტე მცდელობა  ცდის შემდეგ.")
        break
    else:
        print("არასწორია, სცადე თავიდან...")

print("-" * 40)

# 4) 3 რიცხვიდან უდიდესი
a = float(input("შემოიყვანე პირველი რიცხვი: "))
b = float(input("შემოიყვანე მეორე რიცხვი: "))
c = float(input("შემოიყვანე მესამე რიცხვი: "))
print("უდიდესი რიცხვია:", )

print("-" * 40)

# 5) კვირის დღე
day = int(input("შემოიყვანე რიცხვი (1-7): "))
if day == 1:
    print("ორშაბათი")
elif day == 2:
    print("სამშაბათი")
elif day == 3:
    print("ოთხშაბათი")
elif day == 4:
    print("ხუთშაბათი")
elif day == 5:
    print("პარასკევი")
elif day == 6:
    print("შაბათი")
elif day == 7:
    print("კვირა")
else:
    print("არ ვიცი ეგ რა დღეა")
