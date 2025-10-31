# 1)
nums = [1, 2, 3, 4, 5, 6]
nums[2:4] = [10, 20, 30]
print(nums)

# 2)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits[0:2] = ["pear", "plum"]
print(fruits)

# 3)
letters = ["a", "b", "c", "d", "e", "f"]
letters[-3:] = ["x", "y", "z"]
print(letters)

# 4)
colors = ["red", "green", "blue", "yellow", "black", "white"]
colors[2:6] = ["purple", "orange"]
print(colors)

# 5)
names = ["გიორგი", "ირმა", "საბა"]
names = ["red", "green", "blue", "yellow", "black", "white"]
print(names)

# ===========================================

# 6)
num = int(input("შეიყვანე რიცხვი: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 7)
numbers = [5, 8, 12, 9, 15]
if numbers[3] % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# 8)
nums = [12, 25, 47, 52, 68]
last = nums[-1]
if last % 2 == 0 and last > 50:
    print("ეს რიცხვი არის ლუწი და მეტი 50 ზე")
elif last % 2 != 0 and last < 50:
    print("ეს რიცხვი არის კენტი და ნაკლები 50 ზე")

# 9)
nums = [10, 25, 90, 77, 88, 120, 60]
if nums[5] % 2 == 0 or nums[5] > 100:
    print("even or more than 100")
elif nums[3] % 2 != 0 or nums[3] < 100:
    print("odd or less than 100")

# =============================================================

# 10)
str1 = "hello"
str2 = "world"

if str1 != str2:
    print("სტრინგები განსხვავდება")
else:
    print("სტრინგები ტოლია")
