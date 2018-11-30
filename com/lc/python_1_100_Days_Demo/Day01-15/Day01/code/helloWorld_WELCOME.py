#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
helloworld程序-画出WELCOME

Version: 0.1
Author: LC
DateTime: 2018年11月30日10:46:54
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""
import sys
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format
cprint(figlet_format('WELCOME',font='starwars'),'yellow','on_blue',attrs=['bold'])
cprint(figlet_format('LC',font='starwars'),'yellow','on_blue',attrs=['bold'])
cprint('LC', 'yellow', 'on_blue',attrs=['bold','underline'])
cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)
cprint(figlet_format(text='LC',font='bear'))
cprint(figlet_format(text='LC',font='cola'))

"""
更多的font尽在
pyfiglet/pyfiglet/fonts at master · pwaller/pyfiglet
https://github.com/pwaller/pyfiglet/tree/master/pyfiglet/fonts

"""

"""
____    __    ____  _______  __        ______   ______   .___  ___.  _______ 
\   \  /  \  /   / |   ____||  |      /      | /  __  \  |   \/   | |   ____|
 \   \/    \/   /  |  |__   |  |     |  ,----'|  |  |  | |  \  /  | |  |__   
  \            /   |   __|  |  |     |  |     |  |  |  | |  |\/|  | |   __|  
   \    /\    /    |  |____ |  `----.|  `----.|  `--'  | |  |  |  | |  |____ 
    \__/  \__/     |_______||_______| \______| \______/  |__|  |__| |_______|

"""



"""
 __        ______ 
|  |      /      |
|  |     |  ,----'
|  |     |  |     
|  `----.|  `----.
|_______| \______|

"""

"""
LC
Attention!
"""