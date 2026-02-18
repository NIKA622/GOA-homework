# 2) ორი რიცხვის ჯამი
def sum_numbers(num1, num2):
    return num1 + num2

print(sum_numbers(5, 3))
print(sum_numbers(10, 20))
print(sum_numbers(7, 8))


# 3) რიცხვის კვადრატი
def square(num):
    return num ** 2

print(square(4))
print(square(7))
print(square(10))


# 4) სრულწლოვანება
def check_age(age):
    if age >= 18:
        return "სრულწლოვანი ხარ"
    else:
        return "არ ხარ სრულწლოვანი"

print(check_age(20))
print(check_age(15))
print(check_age(18))


# 5) ტექსტის სიმბოლოების რაოდენობა
def count_characters(string):
    print("სიმბოლოების რაოდენობაა:", len(string))

count_characters("Hello")
count_characters("Python")
count_characters("Nika")


# 6) ნამრავლი
def multiply(num1, num2):
    return num1 * num2

print(multiply(4, 5))
print(multiply(3, 7))
print(multiply(10, 2))


# 7) ქულის შეფასება
def check_score(score):
    if score >= 90:
        return "შესანიშნავი ქულა"
    elif score >= 70 and score <= 89:
        return "კარგი ქულა"
    elif score >= 50 and score <= 69:
        return "დამაკმაყოფილებელი ქულა"
    else:
        return "ჩაჭრილი"

print(check_score(95))
print(check_score(75))
print(check_score(60))
print(check_score(40))


# 8) ლუწი თუ კენტი
def even_or_odd(number):
    if number % 2 == 0:
        return "ლუწია"
    else:
        return "კენტია"

print(even_or_odd(4))
print(even_or_odd(7))
print(even_or_odd(10))


# 9) პირველი ასო
def first_letter(name):
    return name[0]

print(first_letter("Giorgi"))
print(first_letter("Nika"))
print(first_letter("Ana"))


# 10) საშუალო არითმეტიკული
def average(num1, num2, num3):
    return (num1 + num2 + num3) / 3

print(average(3, 6, 9))
print(average(10, 20, 30))
print(average(5, 7, 8))