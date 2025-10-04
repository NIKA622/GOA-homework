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
