cities = ["თბილისი", "ბატუმი", "გორი", "მცხეთა", "ქუთაისი", "მარნეული", "რუსთავი"]

for i in range(len(cities)):
    if len(cities[i]) > 6:
        print(cities[i])
#---------------------------------------------------------------------------------------------
words = ["mathematics", "supercalifragilistic", "information", "abcdefghijklmnopqrstu", "transportation"]

for i in range(len(words)):
    if len(words[i]) % 15 == 0:
        print(words[i])
#--------------------------------------------------------------------------------------------------
numbers = [3, 7, 10, 25, 100, 88, 99]
count = 0

for i in range(len(numbers)):  
    count += 1

print("რიცხვების რაოდენობაა:", count)
#---------------------------------------------------------------------------------------------------
words = ["apple", "peach", "mango", "grape", "plums", "kiwi", "melon"]

for i in range(len(words)):
    if len(words[i]) == 5:
        print(words[i])
#-------------------------------------------------------------------------------------------------------------------
text = input("შეიყვანე წინადადება: ")

length = 0
a_count = 0

for i in range(len(text)):
    length += 1
    if text[i] == "a" or text[i] == "A":
        a_count += 1

print("სრული სიმბოლოების რაოდენობა:", length)
print("ასო 'a' ან 'A' რაოდენობა:", a_count)
#---------------------------------------------------------------------------------------------------------------------------
#ვერ დავწერე 6 :(