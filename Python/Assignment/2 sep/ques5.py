def check(x):
    if x+1 is 1+x:
        return False
    if x+2 is not 2+x:
        return False
    return True

print(check(-7))

#value of x is -7 in order to make this function return True.
