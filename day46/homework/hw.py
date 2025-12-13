#1
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in nums[:]:
    index = nums.index(i)
    if i % 2 == 0 or index % 2 == 1:
        nums.remove(i)
print(nums)
#2
words = ["apple", "banana", "cherry"]

for word in words[:]:
    words.append(word)

print(words)
#3
strings = ["a", "b", "c"]
numbers = [10, 25, 40, 55, 70]

for num in numbers:
    if num > 20 and num < 50:
        strings.append(str(num))

print(strings)
#4
words = ["apple", "Banana", "cherry", "Dog", "elephant"]

for i in range(len(words)):
    if words[i][0].islower():
        words[i] = words[i].capitalize()

print(words)
#5
#append()
#ამატებს ახალ ელემენტს სიის ბოლოში.

#remove()
#შლის კონკრეტულ ელემენტს სიიდან მისი მნიშვნელობის მიხედვით.

#pop()
#შლის ელემენტს ინდექსის მიხედვით და ამოღებულ ელემენტს აბრუნებს.

#index()
#აბრუნებს ელემენტის ინდექსს სიაში.

#len()
#გვეუბნება რამდენი ელემენტია სიაში ან რამდენი სიმბოლოა სტრინგში.

#capitalize()
#სტრინგის პირველ ასოს ხდის დიდს, დანარჩენს — პატარას.

#islower()
#ამოწმებს არის თუ არა სიმბოლო ან ასო პატარა.

#upper() / lower()
#upper() სტრინგს მთლიანად დიდ ასოებად აქცევს,
#lower() — მთლიანად პატარა ასოებად.#