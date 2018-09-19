import sys
import itertools

def main():
    print('Number of arguments:', len(sys.argv))
    print('They are:', str(sys.argv))

    strSZ= sys.argv[0]

    print(strSZ)
    print(sys.argv[1])
    print(sys.argv[2])
    print(sys.argv[3])
    print(sys.argv[len(sys.argv)-1])

    # python
    # 排列组合（破解密码） - CSDN博客
    # https: // blog.csdn.net / lm_is_dc / article / details / 80174742

    mylist = list(itertools.permutations([1, 2, 3, 4], 2))
    print(mylist)
    print(len(mylist))

    mylist1 = list(itertools.product("0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm", repeat=2))
    print(mylist1)
    print(len(mylist1))

if __name__ == '__main__':
    main()