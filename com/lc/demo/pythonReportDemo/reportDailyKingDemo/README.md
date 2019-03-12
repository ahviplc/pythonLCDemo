# 日报表-计算写入数据库oracle的报表脚本
#### 1. python_report_daily_app_king.py 加强版本 封装了日报表对象类以及将取自动递增流水方法提取到工具db_utils文件中,集成监听所有的print到log日志的封装类

运行方法：
> python python_report_daily_app_king.py

其他配置说明:

1:配置oracle数据库信息代码位置，请自行更改ip,port,user,password,sid
com/lc/demo/pythonReportDemo/reportDailyKingDemo/python_report_daily_app_king.py:35

2:记录ID-取自动递增流水号 设置序列号名称代码位置(机构号改为传入了)
com/lc/demo/pythonReportDemo/reportDailyKingDemo/python_report_daily_app_king.py:387

3:是否开启将print msg打印内容导出至log文件(如需打印，将此行注释隐掉即可)
com/lc/demo/pythonReportDemo/reportDailyKingDemo/python_report_daily_app_king.py:486

4:设置param org_id 要查询机构号，days 0代表今天 +n代表n天后 -n代表n天前，默认为-1 跑昨天的数据
com/lc/demo/pythonReportDemo/reportDailyKingDemo/python_report_daily_app_king.py:507

**欢迎来到 [LC博客-一加壹博客最Top](http://www.oneplusone.vip)**

**欢迎来到 [LC-Gitlab](https://gitlab.com/ahviplc)**

**欢迎来到 [LC-Github](https://github.com/ahviplc)**

**欢迎来到 [LC-Github-pythonLCDemo](https://github.com/ahviplc/pythonLCDemo)**

> ### LC最寄语：永远不要放弃自己心中最初的最初的理想！~LC

> from **2019年3月11日17:10:43**

> to **2019年3月12日11:52:06**