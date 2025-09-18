# 1) კომენტარის სახით ახსენით თუ რა არის index და რაში ვიყენებთ მას
#  Index არის სიის ელემენტი ნომერი, რომელიც იწყება 0-დან.
#  მას ვიყენებთ კონკრეტულ ელემენტზე მისასვლელად ან მის შესაცვლელად.

# 2) შექმენით სია და იმუშავეთ ინდექსებით
numbers = [4, 6, 1, 5, 9, 8, 4]

print(numbers[0] + numbers[1]) 
print(numbers[2] + numbers[2])  
print(numbers[4] + numbers[3])  
print(numbers[5] + numbers[5])  
print(numbers[6] - numbers[6])  
print(numbers[2] + numbers[5])  
print(numbers[4] + numbers[5] + numbers[1])  

# 3) 10 სახელის სია
names = ["Nika", "Ana", "Gio", "Luka", "Mariam", "Dato", "Nino", "Sandro", "Tako", "Elene"]

print(names[5])  
print(names[9])  
print(names[3]) 
print(names[7])  
print(names[1])  

# 4) სტრინგების სია და გამოტანა for და while loop-ით
words = ["hello", "world", "python", "list", "index"]

# for loop
for w in words:
    print(w)

# while loop
i = 0
while i < len(words):
    print(words[i])
    i += 1

# 5) 7 ელემენტის სია და შეცვლები
items = ["aaa", "bbb", "ccc", "ddd", "eee", "fff", "ggg"]
items[3] = "vashli"
items[6] = "msxali"
items[4] = "atami"
print(items)

# 6) საბოლოო პასუხი → ლოგიკური გამოთვლა
result = True and False or False and True or False and False or True
print(result)  # → True

# 7) ცხოველების სია და შემოწმება
animals = ["dog", "cat", "lion", "tiger", "elephant"]

if animals[3] == "lion":
    print("there is lion on index 3")
else:
    print("there is no lion on index 3")

# 8) basket
basket = ["ვაშლი", "ბანანი", "საზამთრო", "ატამი", "ყურძენი"]

print(basket[0]) 
print(basket[2])  
basket[1] = "მანგო"  

print(basket[0])
print(basket[1])
print(basket[2])
print(basket[3])
print(basket[4])

# 9) letters
letters = ["ა", "ბ", "გ", "ო", "ლ", "ა", "მ", "ა", "ტ", "ე"]

print(letters[2])       
print(letters[4], letters[5])  
print(letters[-1])      

# სიტყვა "მამა"
word1 = letters[6] + letters[7] + letters[6] + letters[7]
print(word1) 

# სიტყვა "გოლა"
word2 = letters[2] + letters[3] + letters[4] + letters[5]
print(word2) 

# სიტყვა "გოგა"
word3 = letters[2] + letters[3] + letters[2] + letters[5]
print(word3) 
