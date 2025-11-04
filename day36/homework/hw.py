word = input("შეიყვანე სიტყვა: ")

for i in range(len(word)):
    if word[i] == "e" or word[i] == "E":
        break  
    print(word[i])
#-------------------------------------------------
text = input("შეიყვანე წინადადება: ")

if "bad" in text:
    print("აკრძალული სიტყვა!")
else:
    print("ყველაფერი რიგზეა")
#-----------------------------------------------------------------------------------------
sentence = input("შეიყვანე წინადადება: ")

for char in sentence:
    if char == " ":
        continue
    print(char)
#-----------------------------------------------------------------------------
text = input("შეიყვანე წინადადება: ")

for char in text:
    if char.lower() in ["a", "e", "i", "o", "u"]:
        continue
    print(char)
#---------------------------------------------------------------------
while True:
    text = input("შეიყვანე ტექსტი: ")
    if text == "python is best":
        break
    print("you should learn python")
