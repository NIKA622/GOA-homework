text = input("shemoagde: ")

if "a" in text or "A" in text:
    print("ari 'a' an'A'")
else:
    print("ar ari 'a' an 'A'")

if "car" not in text:
    print("ar ari car")
else:
    print("ari car")


text = input("shemoiyvane: ")

for i in range(len(text)):
    if text[i] == "a" or text[i] == "A":
        continue  
    print(text[i])
