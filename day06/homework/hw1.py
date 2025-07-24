#1)მომხმარებელს შემოატანინეთ ორი რიცხვი,შეადარეთ ეს ორი რიცხვი ერთმანეთს(გამოიყენეთ შედარების ოპერატორები(>, <, ==)
number1=int(input("enter first"))
number2=int(input("enter second"))
print(number1>number2)
print(number1<number2)
print(number1==number2)



#2)შექმენით 5 ცვლადი,3 ცვლადში შეინახეთ რიცხვები რომლებიც იქნებაინ სტრინგის ტიპის,დანარჩენ 2 ცვლადში შეინახეთ ჩვეულებრიბი ინტეჯერები,შენი დავალებაა იპოვო ამ ხუთი რიცხვის ნამრავლი,შემდეგ ეს ნამრავლი გაყავი რიცხვების რაოდენობაზე და დაპრინტე საბოლოო შედეგი,გამოიყენე შეაბამისი ფუნქცია რომ გადააქციო სტრინგი რიცხვები ინტეჯერად
num1="50"
num2="67"
num3="86"
num4=56
num5=98
print((int(num1))*int(num2)*int(num3)*(num4)*(num5)/5)

#3)მომხმარებელს შემოატანინეთ სამი სტრინგ ტიპის მნიშვნელობა ასევე შემოატანინეთ ერთი ინტეჯერი,თქენი დავალებაა მომხმარებლის მიერ შემოყვანილ სამ სტრინგზე მოახდინოთ კონკატინაცია და შეინახოთ ცალკე ცვლადში ეს სამი გადაბმული სტრინგი,კონკატინაციის შემდეგ კი გაამრავლეთეს ეს მთლიანი სტრინგი მომხმარებლის მიერ შემოყვანილ რიცხვზე
name1=input("enter first name")
name2=input("enter second name")
name3=input("enter third name")
num1=int(input("enter number"))

word1=name1+name2+name3
print(word1+num1)


#5)გვერდით მიუწერეთ რას გამოიტანს შემეგი ოპერაციები
#
# (and)                                     (or)
#True and True -- ...  answer--> TRUE|   True or True -- ... answer-->TRUE        
#True and False -- ...  answer--> FALSE|   True or False -- ...answer-->FALSE
#False and True -- ...  answer-->  FALSE|   False or True -- ...answer-->TRUE
#False and False -- ...  answer--> FALSE |   False or False -- ... answer> FALSE


#6)მოიყვანე მაგალითები and და or ოპერატორებზე,დაპრინტე და გაუშვით ტერმინალში და ნახეთ შედეგი
print(True or True)
print( True or False)
print(False or True)
print(False or  False)
print(True and True)
print( True and False)
print(False and True)
print(False and False)


#გავლილი მასალა:
#7)შექმენი 4 ცვლადი სადაც შეინახავთ სხვადასხვა მონაცემთა ტიპებს და შენი დავალებაა რომ გაიგო ამ ცვლადებში შენახული მონაცემების ტიპები(გამოიყენეთ შესაბამისი ფუნქცია)
str="goa"
int=99
float=1.3
boolean=False
print(type(str))
print(type(int))
print(type(float))
print(type(boolean))
