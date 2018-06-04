# -*- coding: utf-8 -*-
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

def power2(x):
    return x * x

def power(x,n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)

# 递归
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)