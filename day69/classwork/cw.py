""" def make_negative(number):
    if number > 0:
        return -number
    else:
        return number """



def repeat_str(n, s):
    result = ""        
    for i in range(n): 
        result += s    
    return result