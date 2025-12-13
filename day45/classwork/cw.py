
names = ["გუგა", "შოთაძე", "ოთხაძე", "გიო", "ნანდო", "ქორა", "გიგა", "ნიკა"]

for i in names[0:-1]:   
    if len(i) > 5:
        names.remove(i)

print(names)
