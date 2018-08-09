#!/bin/env python
#LC 2018年8月9日11:58:50

# shelve -- 用来持久化任意的Python对象 - 东西南北风 - 博客园
# https://www.cnblogs.com/frankzs/p/5949645.html

import time
import datetime
# import md5  貌似新版python废弃了这个   而是hashlib.md5(plain_pass.encode('utf-8')).hexdigest()使用
import hashlib
import shelve

LOGIN_TIME_OUT = 60
db = shelve.open('#Code/user_shelve.db', writeback=True)

def newuser():
    global db
    prompt = "login desired: "
    while True:
        name = input(prompt)
        if name in db:
            prompt = "name taken, try another: "
            continue
        elif len(name) == 0:
            prompt = "name should not be empty, try another: "
            continue
        else:
            break
    pwd = input("password: ")
    db[name] = {"password": md5_digest(pwd), "last_login_time": time.time()}
    #print '-->', db

def olduser():
    global db
    name = input("login: ")
    pwd = input("password: ")
    try:
        password = db.get(name).get('password')
    except AttributeError :
        print("\033[1;31;40mUsername '%s' doesn't existed\033[0m" % name)
        return
    if md5_digest(pwd) == password:
        login_time = time.time()
        last_login_time = db.get(name).get('last_login_time')
        if login_time - last_login_time < LOGIN_TIME_OUT:
            print("\033[1;31;40mYou already logged in at: <%s>\033[0m" % datetime.datetime.fromtimestamp(last_login_time).isoformat())

        db[name]['last_login_time'] = login_time
        print("\033[1;32;40mwelcome back\033[0m", name)
    else:
        print("\033[1;31;40mlogin incorrect\033[0m")


#md5加密 方法
# 使用python求字符串或文件的MD5 - weiman3389 - 博客园
# https://www.cnblogs.com/weiman3389/p/6056305.html

def md5_digest(plain_pass):
   return hashlib.md5(plain_pass.encode('utf-8')).hexdigest()

def showmenu():
    #print '>>>', db
    global db
    prompt = """
(N)ew User Login
(E)xisting User Login
(Q)uit
Enter choice: """
    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = "q"
                print("\nYou picked: [%s]" % choice)
            if choice not in "neq":
                print("invalid option, try again")
            else:
                chosen = True

        if choice == "q": done = True
        if choice == "n": newuser()
        if choice == "e": olduser()
    db.close()

if __name__ == "__main__":
    showmenu()



    # 测试用户1账户密码： 1  1
    # 测试用户2账户密码：2 2