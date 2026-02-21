# Given two numbers, positive or negative, add up the sume of all the numbers between them incuding the two numbers.
# If a and b are equal return a.
def get_sum(a,b):
    
    total = 0
    
    if a == b:
        return a
    
    if a > b:
        while b <= a:
            total += b
            b+= 1
    else:
        while a <= b:
            total += a
            a+= 1
    return total