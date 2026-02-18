sentence = input("შეიყვანე წინადადება: ")
words = sentence.split()

count = 0
i = 0

while i < len(words):
    if len(words[i]) > 4:
        count += 1
    i += 1

print("4-ზე მეტი სიგრძის სიტყვების რაოდენობაა:", count)

#------------------------------------------------------------------------

word = input("შეიყვანე სიტყვა: ")

is_palindrome = True

for i in range(len(word) // 2):
    if word[i] != word[len(word) - 1 - i]:
        is_palindrome = False
        break

print(is_palindrome)
#-----------------------------------------------------------------

numbers = [5, 8, 12, 3, 14, 7, 20, 9, 6, 11]

list1 = []
list2 = []

for i in range(len(numbers)):
    if numbers[i] % 2 == 0 and i % 2 == 1:
        list1.append(numbers[i])
    elif numbers[i] % 2 != 0 and i % 2 == 0:
        list2.append(numbers[i])

print("ლუწი რიცხვები კენტ ინდექსზე:", list1)
print("კენტი რიცხვები ლუწ ინდექსზე:", list2)

#-------------------------------------------------

data = [1, 2, 2, 3, "nika", "nika", 4.5, 4.5, True, True, True]

i = 0

while i < len(data):
    count = data.count(data[i])
    
    if count > 1:
        data.remove(data[i])
    else:
        i += 1

print("დუპლიკატების გარეშე სია:", data)
