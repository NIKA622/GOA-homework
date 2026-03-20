#3
# def quote(fighter):
#     fighter = fighter.lower()  
#     # lower() ყველა ასოს პატარად აქცევს
#     # მაგალითად: "GEorGE saINT PIErrE" -> "george saint pierre"

#     if fighter == "george saint pierre":  
#         # ვამოწმებთ თუ გამარჯვებული არის George Saint Pierre

#         return "I am not impressed by your performance."
#         # თუ მართალია, ვაბრუნებთ ამ ფრაზას

#     else:
#         # თუ George Saint Pierre არ არის, მაშინ ავტომატურად Conor McGregor არის

#         return "I'd like to take this chance to apologize.. To absolutely NOBODY!"
#         # ვაბრუნებთ კონორის ცნობილ ფრაზას


        #4

    #     def replace_exclamation(s):
    #     vowels = "aeiouAEIOU"   # აქ შევინახეთ ყველა ხმოვანი ასო
    #     result = ""             # ცარიელი სტრინგი სადაც საბოლოო ტექსტს შევაგროვებთ

    # for char in s:          # თითო სიმბოლოს ვამოწმებთ ტექსტში
    #     if char in vowels:  # თუ სიმბოლო ხმოვანია
    #         result += "!"   # დავამატოთ !
    #     else:
    #         result += char  # თუ არაა ხმოვანი, იგივე სიმბოლო დავამატოთ

    # return result           # დავაბრუნოთ საბოლოო ტექსტი



#5

# def stringy(size):
#     result = ""  # აქ შევაგროვებთ საბოლოო სტრინგს

#     for i in range(size):  # ციკლი იმუშავებს size-ჯერ
#         if i % 2 == 0:     # თუ ინდექსი ლუწია
#             result += "1"  # დავამატოთ 1
#         else:              # თუ ინდექსი კენტია
#             result += "0"  # დავამატოთ 0

#     return result          # დავაბრუნოთ საბოლოო სტრინგი
