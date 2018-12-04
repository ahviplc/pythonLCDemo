from abs import absVal
def absMin(x):
    """
    >>absMin([0,5,1,11])
    0
    >>absMin([3,-10,-2])
    -2
    """
    j = x[0]
    for i in x:
        if absVal(i) < absVal(j):
            j = i
    return j

def main():
    a = [-3,-1,2,-11]
    print(absMin(a))  # = -1

if __name__ == '__main__':
    main()

"""
print abs Min
absmax.py and absmin.py bugs fixed. I think absmin.py, are the Numbers with the max output absolute value and the min output absolute value.
And my version output example : absMin.py【 a = [-3,-1,2,-11] print(absMin(a)) # = -1】， this absMin print -1 . please check it.

"""