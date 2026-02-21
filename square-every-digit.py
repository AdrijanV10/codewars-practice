# Square every digit of a number and concatenate them.
def square_digits(num):
    str_num = str(num)
    result = ""
    
    for i in str_num:
        squared = int(i) ** 2
        result += str(squared)
    return int(result)