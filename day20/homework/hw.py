# 1) მოიყვანეთ აბსოლუტურად ყველა მათემატიკურ ოპერატორზე სამ-სამი მაგალითი ძველებურად და ახლებურად

print(4 + 6)
print(200 + 50)
print(10 + 30)

print(20 - 7)
print(55 - 12)
print(90 - 100)

print(8 * 3)
print(15 * 6)
print(2 * 25)

print(30 / 5)
print(99 / 11)
print(7 / 2)

print(25 // 6)
print(40 // 9)
print(17 // 4)

print(25 % 6)
print(14 % 4)
print(50 % 12)

print(2 ** 4)
print(3 ** 3)
print(10 ** 2)


# 2) კომენტარის სახით ახსენით თუ რა მათემატიკური ოპერატორები ვისწავლეთ დღეს და სიტყვიერად დაწერეთ

# + <-- დამატება
# - <-- გამოკლება
# * <-- გამრავლება
# / <-- გაყოფა (ყოველთვის float აბრუნებს)
# // <-- გაყოფის მთელი ნაწილი (floor division)
# % <-- დარჩენილი ნაშთი გაყოფისას
# ** <-- ხარისხში აყვანა


# 3) დღევანდელ მათემატიკურ ოპერატორებზე სათითაოდ მოიყვანეთ 5-5 მაგალითი , სულ 15 მაგალითი უნდა გქონდეთ
print(18 / 6)
print(9 / 4)
print(50 / 10)
print(7 / 3)
print(12 / 0.5)

print(18 // 5)
print(25 // 7)
print(9 // 4)
print(99 // 10)
print(15 // 4)

print(5 * 4)
print(33 * 2)
print(0 * 25)
print(7 * 9)
print((3 + 2) * 7)


# 5) კომენტარის სახით დაწერეთ თუ რაში ვიყენებთ სიებს, და რით განსხვავდებიან ისინი ცვლადებისაგან

# სიები (list) გამოიყენება მაშინ, როცა გვჭირდება ერთ ცვლადში რამდენიმე მნიშვნელობის შენახვა.
# მაგალითად: [1, 2, 3] ან ["dog", "cat", "bird"]
# ცვლადი ჩვეულებრივ ინახავს მხოლოდ ერთ მნიშვნელობას (მაგ: a = 5),
# ხოლო სია საშუალებას გვაძლევს ერთდროულად ბევრი მნიშვნელობა შევინახოთ და ვიმუშაოთ მათზე.


# 6) სია მხოლოდ სტრინგებით
words = ["apple", "banana", "grape", "cherry", "orange"]
print(words)


# 7) სია მხოლოდ ინტეჯერებით
numbers = [5, 10, 20, 30, 40]
print(numbers)


# 8) სია მხოლოდ ფლოატებით
decimals = [1.5, 2.7, 3.14, 10.25, 100.75]
print(decimals)


# 9) სია მხოლოდ boolean-ებით
bools = [True, False, True, False, True]
print(bools)


# 10) შერეული სია ყველა მონაცემთა ტიპით
mixed = [10, 3.14, "hello", False, None]
print(mixed)


# ==============   Bonus   ==============

# 11) მომხმარებელს შემოატანინეთ ორი რიცხვი და მოახდინეთ მათემატიკური ოპერაციები
a = int(input("შეიყვანე პირველი რიცხვი: "))
b = int(input("შეიყვანე მეორე რიცხვი: "))

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
if b != 0:
    print("a / b =", a / b)
    print("a // b =", a // b)
    print("a % b =", a % b)
print("a ** b =", a ** b)


# 12) მომხმარებელს შემოატანინეთ მთელი რიცხვი და შეამოწმეთ დიაპაზონი
n = int(input("შეიყვანე მთელი რიცხვი: "))

if 30 < n < 100:
    print("between 30 and 100")
elif 100 < n < 200:
    print("between 100 and 200")
else:
    print("other number")


# 13) შექმენი 5 ცვლადი განსხვავებული ტიპებით და დაბეჭდე მათი ტიპები
a = 42              # int
b = 3.5             # float
c = "Python"        # str
d = True            # bool
e = [1, 2, 3]       # list

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))




# 14) while ციკლის დახმარებით გამოიტანეთ რიცხვები 50 დან 100 მდე 5 ის გამოტოვებით --> 50 55 60 ...
i = 50
while i <= 100:
    print(i)
    i += 5


# 15) for ციკლის დახმარებით გამოიტანეთ რიცხვები 40 დან 90 მდე 3 ის გამოტოვებით -- > 40 43 46 ...
for i in range(40, 91, 3):
    print(i)


# 16) გამოიტანე შენი სახელი და გვარი 15 ჯერ

# for loop
for i in range(15):
    print("Nika talaxadze")

# while loop
i = 0
while i < 15:
    print("Nika talaxadze")
    i += 1

# 17) მომხმარებლის შემოყვანილი სახელი და გვარი შევადაროთ ჩვენსას
my_name = "Nika"
my_surname = "talaxadze"

user_name = input("შეიყვანე შენი სახელი: ")

if user_name =="nika":
    user_surname = input("შეიყვანე შენი გვარი: ")
    if user_surname == "talaxadze":
        print("same name and surname")
    else:
        print("same name but different surname")
else:
    print("aqedan moshordi")


# 18) პაროლის შემოწმება while ციკლით
password = "12345"

while True:
    user_password = input("შეიყვანე პაროლი: ")
    if user_password == password:
        print("გამოიცანი")
        break
    else:
        print("არასწორია, სცადე თავიდან!")
