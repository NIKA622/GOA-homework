word = input("შეიყვანე სიტყვა: ")

count_exact_two = 0
i = 0

while i < len(word):
    current_char = word[i]
    counter = 1
    j = i + 1
    
    while j < len(word) and word[j] == current_char:
        counter += 1
        j += 1
    
    if counter == 2:
        count_exact_two += 1
    
    i = j

print(count_exact_two)
#----------------------------------------------------------------
text = input("შეიყვანე სტრინგი: ")

total = 0

for char in text:
    if char.isdigit():
        total += int(char)

print("რიცხვების ჯამია:", total)
#---------------------------------------------
sentence = input("შეიყვანე წინადადება: ")

words = sentence.split()
clean_sentence = ""

for i in range(len(words)):
    clean_sentence += words[i]
    if i != len(words) - 1:
        clean_sentence += " "

print(clean_sentence)
#---------------------------------------------------------
nums = [1, 3, 2, 4, 6, 5]

count = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        count += 1

print(count)
#------------------------------------------------
text = input("შეიყვანე ტექსტი: ")

max_count = 1
current_count = 1

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        current_count += 1
        if current_count > max_count:
            max_count = current_count
    else:
        current_count = 1

print(max_count)
#------------------------------------------------------------
word = input("შეიყვანე სიტყვა: ")

for i in range(len(word)):
    count = 0
    for j in range(len(word)):
        if word[i] == word[j]:
            count += 1
    if count == 1:
        print(word[i])
        break
#---------------------------------------------------------------
sentence = input("შეიყვანე წინადადება: ")
words = sentence.split()

for word in words:
    if word.isalpha():
        print(word)
