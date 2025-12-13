#3
words = ["Apple", "banana", "Orange", "grape", "HELLO", "school"]

for word in words[:]:
    if len(word) < 6 or word[-1].isupper():
        words.remove(word)

print(words)
#4
numbers = [5.5, 12.3, 45.7, 9.9, 100.1, 76.4, 150.0, 33.3, 88.8, 2.2]
new_list = []

for num in numbers:
    if num > 10 and num < 100:
        new_list.append(num)

print(new_list)
