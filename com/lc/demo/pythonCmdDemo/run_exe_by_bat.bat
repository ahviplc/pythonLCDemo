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