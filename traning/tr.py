num=[]
for i in range(1, 6):
    num.append(i)
    print(num)



items = ["pen", "book", "phone"]
for i in range(1):
    items.pop()
print(items)



names = ["ana", "nika", "luka", "nika"]
for i in range(1):
    names.remove('nika')
print(names)



a = [1, 2, 3]
b = [4, 5, 6]


a.extend(b)
print(a)

