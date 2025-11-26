# 1) შექმენი სია ხილებზე და დაამატე მასში კიდევ 2 ხილი extend()-ით.
fruits = ["apple", "banana", "orange"]
fruits.extend(["mango", "pear"])
print(fruits)

# 2) შექმენი სია numbers და დაამატე მასში [40, 50] extend()-ით.
numbers = [10, 20, 30]
numbers.extend([40, 50])
print(numbers)

# 3) შექმენი სია names და შეაბრუნე reverse()-ით.
names = ["nika", "ana", "luka"]
names.reverse()
print(names)

# 4) შექმენი nums და დათვალე რამდენი ცალი 5 არის მასში count()-ით.
nums = [5, 1, 5, 2, 5, 3]
print(nums.count(5))

# 5) letters = ["a","b","a","c"] 
letters = ["a", "b", "a", "c"]
print(letters.count("a"))
# 6) შექმენი names და იპოვე "saba"-ს ინდექსი
names = ["nika", "saba", "luka"]
print(names.index("saba"))

# 7) list = ["red","green","blue"] იპოვე რომელ ინდექსზეა "blue"
colors = ["red", "green", "blue"]
print(colors.index("blue"))

# 8) nums + extend([7, 8, 9])
nums = [1, 2, 3]
nums.extend([7, 8, 9])
print(nums)

# 9) foods დააბრუნე შებრუნებული reverse()-ით
foods = ["pizza", "burger", "fries"]
foods.reverse()
print(foods)

# 10) cities და იპოვე "tbilisi" ინდექსი
cities = ["batumi", "tbilisi", "kutaisi"]
print(cities.index("tbilisi"))

# 11) animals-ში დაითვალე რამდენი "cat" არის
animals = ["cat", "dog", "cat", "cow"]
print(animals.count("cat"))
# 12) append-ით დაამატე "grape"
fruits = ["apple", "banana"]
fruits.append("grape")
print(fruits)

# 13) extend()-ით დაამატე [4, 5]
numbers = [1, 2, 3]
numbers.extend([4, 5])
print(numbers)

# 14) insert()-ით ჩასვი "luka" პირველ ინდექსზე
names = ["goga", "saba"]
names.insert(1, "luka")
print(names)

# 15) pop()-ით წაშალე ბოლო ელემენტი
items = ["pen", "pencil", "eraser"]
items.pop()
print(items)

# 16) remove()-ით წაშალე "green"
colors = ["red", "green", "blue"]
colors.remove("green")
print(colors)

#17
foods = ["bread", "milk"]

if len(foods) >= 2:
    foods.append("cheese")
else:
    foods.append("meat")

print(foods)
#18n
nums = [10, 20, 30]

number = int(input("შეიყვანე მთელი რიცხვი: "))

if number in nums:
    print("Already in list")
else:
    nums.append(40)
    print(nums)
#20
values = [1, 2, 3, 4]

index = int(input("შეიყვანე ინდექსი: "))

if 0 <= index < len(values):
    values.pop(index)
else:
    print("Index out of range")

print(values)


# 21) 
pets = ["cat", "dog", "hamster"]


pet_name = input("შეიყვანე შინაური ცხოველის სახელი: ")


if pet_name in pets:
    pets.remove(pet_name)
    print("Removed")
else:
    print("Not found")


print(pets)

# 23) სია
queue = ["first", "second"]


new_item = input("შეიყვანე ახალი ელემენტი: ")


queue.insert(0, new_item)


if len(queue) > 5:
    queue.pop()          
    print(queue)
else:
    print(queue[-1])    




    
# 24) სია
nums = [2, 4, 6]


num = int(input("შეიყვანე რიცხვი: "))


if num > 0:
    nums.append(num)
else:
    print("Only positive allowed")


print(nums)
