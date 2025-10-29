# 1)
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("პირველი 5 ელემენტი:", lst[:5])        
print("ბოლო 3 ელემენტი:", lst[-3:])          
print("ელემენტები 3-დან 7-მდე:", lst[3:8])    

# 2) 
lst2 = list(range(1, 16))

print("\nპირველი 6 ელემენტი (უარყოფითი ინდექსებით):", lst2[:-9])  
print("ბოლო 10 ელემენტი:", lst2[-10:])                             
print("7-დან 14-მდე ინდექსები (უარყოფითი):", lst2[-8:-1])          

# 3) 
word = "თვითმფრინავი"
print("\n'ნავი':", word[-4:])      

# 4)
word2 = "Programmer"
print("\n'Pro' (დადებითი):", word2[:3])
print("'Pro' (უარყოფითი):", word2[:-8])   

# 5) 
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# 
print("\nსამუშაო დღეები (დადებითი):", week[:5])
print("სამუშაო დღეები (უარყოფითი):", week[:-2])

#
print("დასვენების დღეები (დადებითი):", week[5:])
print("დასვენების დღეები (უარყოფითი):", week[-2:])

# 6)
sentence = "Python slicing is very powerful"

print("\n'Python' (დადებითი):", sentence[:6])
print("'slicing' (დადებითი):", sentence[7:14])
print("'powerful' (უარყოფითი):", sentence[-8:])
