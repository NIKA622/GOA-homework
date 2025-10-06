# 1)
nums = [2, 4, 6, 8, 10, 12, 14]

for i in range(-7, -6+1): print(nums[i])
for i in range(-1, 0): print(nums[i])
print(nums[-7] * nums[-1])
for i in range(2, 3): print(nums[i])
for i in range(4, 5): print(nums[i])  

# 2)
fruits = ["apple", "banana", "cherry", "grape", "kiwi", "orange"]
for i in range(2, 4): print(fruits[i])

# 3)
numbers = [3,4,5,6,7,1,2,9,8,11]
n = int(input("შეიყვანე ინდექსი (0-10): "))
for i in range(10):
    if n == i: print(numbers[i]); break
else: print("you entered negative or more than 10 number")

# 4)
words = ["dog","most","is","angry","running","forest","fast","in","cat","human","very"]

for i in [-11,-9,-7,-4,-6,-1]: print(words[i], end=" ")
print()
for i in [0,2,4,7,5,10]: print(words[i], end=" ")
print()
for i in [8,2,10,3]: print(words[i], end=" ")
print()

# 5)
animals = ["dog","cat","horse","cow","sheep","goat"]
m = int(input("შეიყვანე ინდექსი (0-5): "))
for i in range(6):
    if m == i:
        print("შენ აირჩიე კატა" if animals[i]=="cat" else "შენ აირჩიე თხა" if animals[i]=="goat" else "სხვა ცხოველი აირჩიე")
        break
else: print("არასწორი ინდექსი შეიყვანე")
#6
cities = ["Tbilisi", "Batumi", "Kutaisi", "Rustavi", "Telavi", "Zugdidi"]

a = int(input("შეიყვანე პირველი ინდექსი: "))
b = int(input("შეიყვანე მეორე ინდექსი: "))

if a < b:
    print("ამ ინდექსებზე არის:", cities[a], "და", cities[b])
elif b < a:
    print("შეცვალე ინდექსები ადგილებით")
    print("ამ შემთხვევაში ესენი იქნებიან:", cities[b], "და", cities[a])
else:
    print("ორივე ინდექსი ერთნაირია")
    print("ეს არის:", cities[a])
#7
word = input("შეიყვანე სიტყვა: ")

if word[0].lower() == "a":
    print("სიტყვა იწყება a-თი")
elif word[-1].lower() == "z":
    print("სიტყვა მთავრდება z-ით")
else:
    print("სიტყვა არც a-თი იწყება და არც z-ით მთავრდება")
#8
word = input("შეიყვანე სიტყვა: ")

if word[0] == word[-1]:
    print("პირველი და ბოლო ასო ერთნაირია")
else:
    print("პირველი და ბოლო ასო განსხვავებულია")
#9
letters = "agivorsbgitr"

goga = letters[2] + letters[0] + letters[2] + letters[0]
print("პირველი სიტყვა:", goga)

saba = letters[7] + letters[0] + letters[1] + letters[0]
print("მეორე სიტყვა:", saba)

bativar = letters[1] + letters[0] + letters[3] + letters[1] + letters[5] + letters[0] + letters[6]
print("მესამე სიტყვა:", bativar)
#10
text = "giorgi"

print("for ციკლით:")
for letter in text:
    print(letter)

print("\nwhile ციკლით:")
i = 0
while i < len(text):
    print(text[i])
    i += 1
