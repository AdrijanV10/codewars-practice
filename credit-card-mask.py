# return masked string leaving the last 4 characters.
def maskify(cc):
    if len(cc) <= 4:
        return cc
     
    return "#" * (len(cc) - 4) + cc[-4:]