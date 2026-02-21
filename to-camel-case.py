# Complete the method/function so that it converts dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). 
# The next words should be always capitalized.
# hello_world --> helloWorld
def to_camel_case(text):
    result = ""
    capitalize_next = False
    
    for char in text:
        if char in '-_':
            capitalize_next = True
        else:
            if capitalize_next:
                result += char.upper()
                capitalize_next = False
            else:
                result += char
    
    return result