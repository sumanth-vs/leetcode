<<<<<<< HEAD
def rev(x):
    rev_int = 0
    while(x != 0):
        print('x=',x)
        rev_int = rev_int*10 + x % 10
        print('rev_int =', rev_int)
        x = x//10
    return rev_int

=======
def rev(x):
    rev_int = 0
    while(x != 0):
        print('x=',x)
        rev_int = rev_int*10 + x % 10
        print('rev_int =', rev_int)
        x = x//10
    return rev_int

>>>>>>> 2fc906c56a2d54da2a34984edcef9675e90ca218
print(rev(-123))