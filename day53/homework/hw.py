#2) შექმენით სიტყვებით სავსე სია, თუ სიტყვის ყველა ასო არის პატარა და პირველი ასო არის g, მაშინ ახალ სიაში ჩაამატეთ სახელი "Goga", თუ სიტყვის ყველა ასო არის დიდი ან იწყება ასო N-თი, მაშინ სიაში ჩაამატეთ სახელი "Nika", სხვა შემთხვევაში სიაში ჩაამატეთ სიტყვა "ლიდერი". დაპრინტეთ მიღებული სია.


sia=["gaga", "Nika", "leader"]
newsia=[]
for i in sia:
    if i[0].islower() and i[0]=="g":
        newsia.append("Goga")
    elif i[0].isupper() or i[0]=="N":
        newsia.append("Nika")
    else:
        newsia.append("ლიდერი")
print(newsia)




#3)  შექმენით რიცხვებით სავსე სია, თუ რიცხვი არის ლუწი ან დგას ლუწ ინდექსზე, ჩაამატეთ მისი კვადრატი ახალ სიაში - გამოიყენეთ შესაბამისი მათემატიკური ოპერატორი, ხოლო თუ რიცხვი არის კენტი ან დგას კენტ ინდექსზე, ახალ სიაში ჩაამატეთ 2-ჯერ დიდი რიცხვი. გამოიყენეთ while ციკლი.




gahhh=[1,2,3,4,5,6,7,8,9,10]

haag=[]


i=0

while i<len(gahhh):
    if gahhh[i]%2==0 or i%2==0:
        haag.append(gahhh[i]**2)
    else:
        haag.append(gahhh[i]*2)
    i+=1
print(haag)




#4) შექმენით სიტყვებით სავსე სია, თუ სიტყვის სიგრძე არის 6-ზე მეტი ან მისი ყველა ასო არის დიდი, ამ სიტყვის ყველა ასო გახადეთ პატარა და ჩაამატეთ ახალ სიაში. ყველა სხვა შემთხვევაში ახალ სიაში ჩაამატეთ შეუცვლელი სიტყვა ოღონდ გადაბმულად ორჯერ, მაგალითად თუ მოცემული იქნება სიტყვა "Nika", ჩაამატეთ "NikaNika". გამოიყენეთ while ციკლი.

words=["sandro", "irakli", "nino", "gafrindi", "salome", "ilia"]
newwords=[]

i=0
while i<len(words):
    if len(words[i])>6 or words[i].isupper():
        newwords.append(words[i].lower())
    else:
        newwords.append(words[i]*2)
    i+=1

print(newwords)




#5) მოცემული გაქვთ სტრინგის ცვლადი: numbers = "0123456789", ამ სტრინგიდან ახალ სიაში ჩაამატეთ ყველა ის რიცხვი რომელიც დგას ამ სტრინგის ლუწ ინდექსზე ან არის 7-ზე მეტი, სიაში ეს რიცხვები იყოს როგორც integer ტიპის მონაცემები და არა სტრინგები. დაწერეთ ორივე ხერხით, for ციკლით და while ციკლით.

numbers="0123456789"
newnumbers=[]

for i in range(len(numbers)):
    arr=int(numbers[i])
    if i%2==0 or arr>7:
        newnumbers.append(arr)

print(newnumbers)       



numbers="0123456789"
newnumbers=[]

i=0
while i<len(numbers):
    arr=int(numbers[i])
    if i%2==0 or arr>7:
        newnumbers.append(arr)
    i+=1
print(newnumbers)



