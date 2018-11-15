
"""
Version: 0.1
Author: LC
DateTime: 2018年11月15日15:04:46
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

def main():
    persons = [True] * 30
    counter = 0
    index = 0
    number = 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                number = 0
                counter += 1
        index += 1
        index %= len(persons)
    for person in persons:
	    print('基' if person else '非', end='')
    print()


if __name__ == '__main__':
    main()

