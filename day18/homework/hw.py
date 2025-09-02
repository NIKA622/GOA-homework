# 1) ორი რიცხვის შედარება
num1 = 15
num2 = 10

if num1 > num2:
    print("first is more than second")
elif num1 < num2:
    print("first is less than second")
else:
    print("first number equal to second number")


# 2) სახელების შედარება
user_name = "Nika"
my_name = "Nika"   # შეგიძლია შეცვალო სახელი

if user_name == my_name:
    print("სეხნიები ვართ")
else:
    print("სხვადასხვა სახელები გვაქვს")


# 3) ორი რიცხვის დადებით/უარყოფითობაზე შემოწმება
x= -7
y = -2

if x > 0 and y > 0:
    print("ორივე რიცხვი დადებითია")
elif x < 0 and y < 0:
    print("ორივე რიცხვი არის უარყოფითი")
else:
    print("ეს რა ჯანდაბაა")

# 4) for loop 50-დან 100-მდე 2-ის გამოტოვებით
for i in range(50, 101, 2):   # 50-დან იწყება, 101-მდე, ყოველ ნაბიჯზე +2
    print(i)


# 5) while loop 20-დან 40-მდე
num = 20
while num <= 40:
    print(num)
    num += 1
