sentence = "Hello World from Python"

vowels = "aeiouAEIOU"
count = 0

for letter in sentence:
    if letter in vowels:
        count += 1

print("ხმოვანი ასოების რაოდენობაა:", count)
#----------------------------------------------

numbers = [3, 8, 12, 5, 7, 10, 14]

even_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num

print("ლუწი რიცხვების ჯამია:", even_sum)
#------------------------------------------

numbers = [15, 42, 7, 89, 23, 56]

max_number = numbers[0]

for num in numbers:
    if num > max_number:
        max_number = num

print("ყველაზე დიდი რიცხვია:", max_number)
#--------------------------------------

password = input("შეიყვანე პაროლი: ")

while len(password) < 6:
    print("პაროლი უნდა იყოს მინიმუმ 6 სიმბოლო!")
    password = input("შეიყვანე თავიდან: ")

print("Your password is correct!")
#-------------------------------------------------
numbers = [3, 5, 3, 8, 5, 10, 8]

new_list = []

for num in numbers:
    if num not in new_list:
        new_list.append(num)

print("გამეორებების გარეშე:", new_list)
#--------------------------------------------------------

sentence = input("შეიყვანე წინადადება: ")
words = sentence.split()

checked = []

for word in words:
    if word not in checked:
        counter = 0
        for w in words:
            if w == word:
                counter += 1
        
        print(word, counter)
        checked.append(word)
