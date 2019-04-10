# 月 后付费结算单/付款通知单-计算写入数据库oracle的账单脚本
#### 1. python_fi_balance_bill_monthly_app_king2.py 加强版本 封装了月账单对象类以及将取自动递增流水方法提取到工具db_utils文件中,集成监听所有的print到log日志的封装类

运行方法：
> python python_fi_balance_bill_monthly_app_king2.py

其他配置说明:

1:配置oracle数据库信息代码位置，请自行更改ip,port,user,password,sid
com/lc/demo/pythonFiBalanceBillDemo/fiBalanceBillMonthlyKingDemo/python_fi_balance_bill_monthly_app_king2.py:40

2:记录ID-取自动递增流水号 设置序列号名称代码位置(机构号改为传入了)
com/lc/demo/pythonFiBalanceBillDemo/fiBalanceBillMonthlyKingDemo/python_fi_balance_bill_monthly_app_king2.py:679

3:是否开启将print msg打印内容导出至log文件(如需打印，将此行注释隐掉即可)
com/lc/demo/pythonFiBalanceBillDemo/fiBalanceBillMonthlyKingDemo/python_fi_balance_bill_monthly_app_king2.py:854

4:设置param org_id 要查询机构号，months 0代表当前月 +n代表n月后 -n代表n月前，默认为-1 跑上个月的数据
com/lc/demo/pythonFiBalanceBillDemo/fiBalanceBillMonthlyKingDemo/python_fi_balance_bill_monthly_app_king2.py:876

**欢迎来到 [LC博客-一加壹博客最Top](http://www.oneplusone.vip)**

**欢迎来到 [LC-Gitlab](https://gitlab.com/ahviplc)**

**欢迎来到 [LC-Github](https://github.com/ahviplc)**

**欢迎来到 [LC-Github-pythonLCDemo](https://github.com/ahviplc/pythonLCDemo)**

> ### LC最寄语：永远不要放弃自己心中最初的最初的理想！什么才是真正的人生？也许人生的意义就在此时思考的片刻！~LC

> from **2019年4月10日16:00:11**

> to **future**