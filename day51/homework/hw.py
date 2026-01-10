nums = [3, 6, 10, 12, 15, 20, 25, 30, 4]
new_nums = []
for i in nums:
    new_nums.append(i * 2)
print(new_nums)


# task2
names = ["dato", "saba", "luka", "gio", "zurabi", "ana"]
your_num = int(input("Enter number: "))
for i in names:
    names.insert(your_num, "nino")
print(names)


# task3
word = "programireba dzalian magariia"
new_word = ""
for i in word:
    if i in "aeiou":
        new_word += i
print(new_word)


# task4
nothing = ["kompiuteri", "wigni", "mama", "eleqtroenergetika"]
for i in nothing:
    if len(i) > 4 or nothing.index(i) % 2 == 1:
        nothing.remove(i)
print(nothing)


# task5
numbers = [5, 15, 25, 35, 45, 55, 65]
sum = 0
for i in numbers:
    sum += i
print(sum / len(numbers))
