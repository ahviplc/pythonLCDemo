两种写法，比如是 test.exe程序

一种
test.exe

二种
start test.exe

第一种批处理会等待test.exe程序执行完后才会运行下面的语句

第二种不会等待.

bat批处理获取当前所在目录的绝对路径方法 – 在情岛  
>https://www.inqingdao.cn/1143.html

example:  
```shell
@echo off
echo run exe is successful ...

rem bat脚本 run_exe_by_bat.bat
rem 输出变量
rem 获取当前CMD默认目录：%cd%
set CD_HOME=%cd% 
echo %CD_HOME%
cd /d %CD_HOME%
ls
echo run parsing_message_app_king_print_log_version_all_ok.exe
echo -----------------------------
parsing_message_app_king_print_log_version_all_ok.exe
rem start parsing_message_app_king_print_log_version_all_ok.exe
echo -----------------------------
echo run over
pause
```

example2:
```shell
@echo off
echo run exe is successful ...

rem bat脚本 run_exe_by_bat.bat
rem 输出变量
rem 获取当前CMD默认目录：%cd%
set CD_HOME=%cd% 
echo %CD_HOME%
cd /d %CD_HOME%
ls
echo run hello.exe
echo -----------------------------
hello.exe
rem start hello.exe
echo -----------------------------
echo run over
pause
```