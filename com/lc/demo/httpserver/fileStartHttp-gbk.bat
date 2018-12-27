@echo off
echo "欢迎执行一个简单的文件服务器！~LC"
pause
echo begin cmd
echo cmd: python -m http.server 10087
python -m http.server 10087
echo cmd over

::文件格式编码:gbk 不乱码