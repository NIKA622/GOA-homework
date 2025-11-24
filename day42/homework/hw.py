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

# 5) letters = ["a","b","a","c"] – დაითვალე რამდენი “a” არის.
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
