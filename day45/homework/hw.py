# 1) შექმენით რიცხვებით სავსე სია, თქვენი დავალებაა რომ დაპრინტოთ ახალი სია რომელშიც იქნება თქენს პირველ სიაში მყოფი მხოლოდ ლუწი რიცხვები. გამოიყენეთ შესაბამისი სიის ფუნქცია და for ციკლი.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers2 = []

for i in numbers:
    if i % 2 == 0:
        numbers2.append(i)

print(numbers2)

# 2) შექმენით რიცხვებით სავსე სია, თქვენი დავალებაა რომ დაპრინტოთ ახალი სია რომელშიც იქნება მხოლოდ თქენს პირველ სიაში კენტ ინდექსზე მდგომი რიცხვები რომელბიც არიან აუცილებლად კენტი. გამოიყენეთ შესაბამისი სიის ფუნქცია და for ციკლი.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers2= []

for i in range(1, len(numbers), 2):
    if numbers[i] % 2 == 0:
        numbers2.append(numbers[i])

print(numbers2)
#3
names = ['გელა', 'ნინო', 'გურამი', 'მარი', 'გია']

for name in names[:]:
    if name[0] == 'გ' and name[-1] == 'ი':
        names.remove(name)

for i in range(len(names) - 1, -1, -1):
    if names[i][0] == 'გ' and names[i][-1] == 'ი':
        names.pop(i)

print(names)
#4
words = ['Dato', 'sandro', 'Nika', 'lasha', 'Mariam', 'ana']

i = 0
while i < len(words):
    if words[i][0].isupper():
        if i % 2 == 0:
            words.pop(i)
        else:
            words[i] = words[i].lower()
            i += 1
    else:
        i += 1

print(words)
#5
words1 = ['GOLD', 'hello', 'Good', 'cat', 'go', 'GAME', 'WORLD', 'HOUSE', 'GHOST', 'GREEN', 'GIFT']

i = 0
while i < len(words1):
    if words1[i][0] == 'G' and words1[i][-2:].isupper():
        words1.pop(i)
    else:
        i += 1

for i in range(len(words1)):
    if words1[i].islower():
        words1[i] = words1[i].upper()

print(words1)
#6


