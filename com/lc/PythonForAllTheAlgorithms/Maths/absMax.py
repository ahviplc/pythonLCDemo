from abs import absVal

def absMax(x):
    """
    >>absMax([0,5,1,11])
    11
    >>absMax([3,-10,-2])
    -10
    """
    j =x[0]
    for i in x:
        if absVal(i) > absVal(j):
            j = i
    return j
    #BUG: i is apparently a list, TypeError: '<' not supported between instances of 'list' and 'int' in absVal
    #BUG fix

def main():
    a = [-13, 2, -11, -12]
    print(absMax(a)) # = -13

if __name__ == '__main__':
    main()

"""
print abs Max

absmax.py and absmin.py bugs fixed. I think absmax.py are the Numbers with the max output absolute value and the min output absolute value.
And my version output example : absMax.py【a = [-13, 2, -11, -12] print(absMax(a)) # = -13】， this absMax print -13 ; 
 please check it.

"""
