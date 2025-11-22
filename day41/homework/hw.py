#2
numbers = [1, 2, 3, 4, 5]
numbers.append(10)
print(numbers)
#3
names = ["goga", "saba", "luka"]
names.append("nika")   
print(names)
#4
names = ["goga", "saba", "luka"]

user_name = input("შეიყვანე სახელი: ")

names.append(user_name)

print(names)
#5
names = ["ana", "goga", "sandro", "luka", "mate"]

names.insert(3, "nika")   
print(names)
names = ["ana", "goga", "sandro", "luka", "mate"]

names.insert(3, "nika")  
print(names)

#7
fruits = ["apple", "banana"]
fruits.insert(1, "orange")
print(fruits)
#8
names = ["goga", "saba", "luka"]
names.insert(2, "irakli")   
print(names)
#9
foods = ["bread", "milk", "cheese"]
foods.insert(0, "water")
print(foods)
#10
numbers = [5, 10, 15]
numbers.pop()    
print(numbers)
#11
fruits = ["apple", "banana", "orange"]
fruits.pop(1)
print(fruits)
#12
names = ["goga", "saba", "luka"]
names.pop(1)
print(names)
#13
colors = ["red", "green", "blue", "yellow", "black", "purple"]

colors.pop(0)    

colors.pop(3)   

print(colors)
#14
index_num = int(input("შეიყვანე რიცხვი 0-დან 3-მდე: "))

items = ["pen", "pencil", "book", "eraser"]

items.pop(index_num)

print(items)
#15
fruits = ["apple", "banana", "orange"]

fruits.remove("banana")

print(fruits)
#16
nums = [3, 5, 3, 7]

nums.remove(3)

print(nums) 
#17
colors = ["red", "blue", "green"]

colors.remove("blue")

print(colors)
#18
names = ["goga", "saba", "luka"]

user_choice = input("რომელი სახელი გინდა წაშალო (goga/saba/luka): ")

names.remove(user_choice)

print(names)

