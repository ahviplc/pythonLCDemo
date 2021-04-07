# MySQLToOracle

> 一款mysql向oracle的数据转移app.

## 安装驱动

> pip install pony  
> pip install PyMySQL   
> pip install cx-Oracle  

```markdown
mysql

PyMySQL · PyPI
https://pypi.org/project/PyMySQL/

GitHub - PyMySQL/PyMySQL: Pure Python MySQL Client
https://github.com/PyMySQL/PyMySQL

Welcome to PyMySQL’s documentation! — PyMySQL 0.7.2 documentation
https://pymysql.readthedocs.io/en/latest/

oracle

cx-Oracle · PyPI
https://pypi.org/project/cx-Oracle/

GitHub - oracle/python-cx_Oracle: Python interface to Oracle Database conforming to the Python DB API 2.0 specification.
https://github.com/oracle/python-cx_Oracle

cx_Oracle - Python Interface for Oracle Database
https://oracle.github.io/python-cx_Oracle/
```

## orm框架 
```markdown
Getting Started with Pony — Pony ORM documentation
https://docs.ponyorm.org/firststeps.html

API Reference — Pony ORM documentation
https://docs.ponyorm.org/api_reference.html#oracle

Getting Started with Pony — Pony ORM documentation
https://docs.ponyorm.org/firststeps.html#pony-examples

pony/pony/orm/examples at orm · ponyorm/pony · GitHub
https://github.com/ponyorm/pony/tree/orm/pony/orm/examples

ponyorm/pony - GitHub1s - 在1s的vscode编辑器中打开
https://github1s.com/ponyorm/pony/blob/orm/pony/orm/examples/demo.py
```

## 其他链接
```markdown
python3对MySQL数据库操作进行封装_统哥哥的博客-CSDN博客-基于pymysql
https://blog.csdn.net/weixin_43935187/article/details/85763356

Python的魔法ORM --《PonyORM教程》 1.连接,声明和查询 - 简书
https://www.jianshu.com/p/11b9cdace3b2

PonyORM教程1 连接,声明和查询_justonlyyo的博客-CSDN博客-这个包含教程5-更全-其他和上面一样.
https://blog.csdn.net/justonlyyo/article/details/102523401

PonyORM教程 5 钩子函数和实体方法扩展_justonlyyo的博客-CSDN博客
https://blog.csdn.net/justonlyyo/article/details/102523602

随笔之pymysql查询结果转字典dict_家住海边，见过大风大浪-CSDN博客
https://blog.csdn.net/u014487025/article/details/88684541

只有Python魔法少女才知道的PonyORM
https://farer.org/2018/07/09/ponyorm/

Python 线程安全（同步锁Lock）详解 - 说的不错 - 【utils/cx_Oracle_db_utils.py:26】
http://c.biancheng.net/view/2617.html

详解python的ORM中Pony用法_python_脚本之家 对应源码【https://github.com/flowpig/daily_demos】
https://www.jb51.net/article/134781.htm
pony学习 - 【https://github.com/flowpig/daily_demos/tree/master/Pony%E5%AD%A6%E4%B9%A0】

py 全局变量_paulkg12的博客-CSDN博客_py全局变量
https://blog.csdn.net/paulkg12/article/details/88660994

Python random() 函数 | 菜鸟教程
https://www.runoob.com/python/func-number-random.html

Python练习题-判断某一个字符串是否是小数_oito_菜鸟-CSDN博客_python 判断字符串是小数 这个很不错
https://blog.csdn.net/wls666/article/details/96038402

Python range() 函数 | 菜鸟教程
https://www.runoob.com/python/python-func-range.html

Python 3 实现定义跨模块的全局变量和使用 - _Suwings - 博客园
https://www.cnblogs.com/suwings/p/6358061.html
```

## 两个核心SQL脚本

> 一个MySQL(数据提供者),一个Oracle(数据接收者).下面数据库脚本,对应数据域执行,即可建表.

### MySQL
```mysql
/*
 Navicat Premium Data Transfer

 Source Server         : 192.168.0.17 - mysql - root -###
 Source Server Type    : MySQL
 Source Server Version : 50720
 Source Host           : 192.168.0.17:3306
 Source Schema         : htiot_qinghaixn_report

 Target Server Type    : MySQL
 Target Server Version : 50720
 File Encoding         : 65001

 Date: 07/04/2021 13:39:03
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for meter_report_month_202104
-- ----------------------------
DROP TABLE IF EXISTS `meter_report_month_202104`;
CREATE TABLE `meter_report_month_202104`  (
  `report_id` int(11) NOT NULL AUTO_INCREMENT,
  `company_no` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `meter_comm_no` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `device_type` int(11) NULL DEFAULT NULL,
  `factory_code` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `meter_area_no` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `meter_define_no1` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `meter_define_no2` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `meter_define_no3` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `meter_define_no4` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `report_year` int(11) NULL DEFAULT NULL,
  `report_month` int(11) NULL DEFAULT NULL,
  `report_day` int(11) NULL DEFAULT NULL,
  `report_gen_time` datetime(0) NULL DEFAULT NULL,
  `std_sum` decimal(18, 3) NULL DEFAULT NULL,
  `work_sum` decimal(18, 3) NULL DEFAULT NULL,
  `this_day_sum` decimal(18, 3) NULL DEFAULT NULL,
  `last_day_sum` decimal(18, 3) NULL DEFAULT NULL,
  `this_cycle_sum` decimal(18, 3) NULL DEFAULT NULL,
  `last_cycle_sum` decimal(18, 3) NULL DEFAULT NULL,
  `remain_money` decimal(18, 3) NULL DEFAULT NULL,
  `remain_volume` decimal(18, 3) NULL DEFAULT NULL,
  `curr_price` decimal(18, 3) NULL DEFAULT NULL,
  `meter_state` int(11) NULL DEFAULT NULL,
  `meter_stat_emsg` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `rssi` int(11) NULL DEFAULT NULL,
  `battery_voltage` decimal(18, 3) NULL DEFAULT NULL,
  `battery_level` int(11) NULL DEFAULT NULL,
  `ext_data` json NULL,
  `ext_data2` json NULL,
  `ext_data3` json NULL,
  `ext_data4` json NULL,
  PRIMARY KEY (`report_id`) USING BTREE,
  INDEX `idx_company_no`(`company_no`) USING BTREE,
  INDEX `idx_factory_code`(`factory_code`) USING BTREE,
  INDEX `idx_meter_area_no`(`meter_area_no`) USING BTREE,
  INDEX `idx_year_month`(`report_year`, `report_month`) USING BTREE,
  INDEX `idx_meter_report_month_1`(`meter_comm_no`) USING BTREE,
  INDEX `idx_meter_report_month_2`(`report_year`, `report_month`, `report_day`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 72332 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;

```

### Oracle
```oracle
/*
 Navicat Premium Data Transfer

 Source Server         : oracle-lmtplat-SCOTT-###
 Source Server Type    : Oracle
 Source Server Version : 110200
 Source Host           : 192.168.0.7:1521
 Source Schema         : SCOTT

 Target Server Type    : Oracle
 Target Server Version : 110200
 File Encoding         : 65001

 Date: 07/04/2021 13:38:46
*/


-- ----------------------------
-- Table structure for SCADA_REPORT_XN_MID
-- ----------------------------
DROP TABLE "SCOTT"."SCADA_REPORT_XN_MID";
CREATE TABLE "SCOTT"."SCADA_REPORT_XN_MID" (
  "SRXM_ORG_ID" VARCHAR2(6 BYTE) DEFAULT '' NOT NULL ,
  "SRXM_ID" VARCHAR2(20 BYTE) DEFAULT '' NOT NULL ,
  "FLMETER_NO" VARCHAR2(20 BYTE) ,
  "COMM_NO" VARCHAR2(20 BYTE) ,
  "REPORT_TIME" TIMESTAMP(6) ,
  "YEAR" VARCHAR2(10 BYTE) ,
  "MONTH" VARCHAR2(10 BYTE) ,
  "DAY" VARCHAR2(10 BYTE) ,
  "STD_SUM" VARCHAR2(18 BYTE) ,
  "WORK_SUM" VARCHAR2(18 BYTE) ,
  "PRICE" VARCHAR2(18 BYTE) ,
  "THIS_CYCLE_SUM" VARCHAR2(18 BYTE) ,
  "CYCLE_USE_MONEY" VARCHAR2(18 BYTE) ,
  "THIS_DAY_SUM" VARCHAR2(18 BYTE) ,
  "SUM_TOTAL_MONEY" VARCHAR2(18 BYTE) ,
  "TOTAL_BUY_VOLUME" VARCHAR2(18 BYTE) ,
  "TOTAL_BUY_MONEY" VARCHAR2(18 BYTE) ,
  "REMAIN_MONEY" VARCHAR2(18 BYTE) ,
  "REMAIN_VOLUME" VARCHAR2(18 BYTE) ,
  "FM_STATE" VARCHAR2(50 BYTE) ,
  "BATTERY_VOLTAGE" VARCHAR2(18 BYTE) ,
  "BATTERY_LEVEL" VARCHAR2(18 BYTE) ,
  "RSSI" VARCHAR2(10 BYTE) ,
  "FM_STATE_MSG" VARCHAR2(200 BYTE) 
)
TABLESPACE "USERS"
LOGGING
NOCOMPRESS
PCTFREE 10
INITRANS 1
STORAGE (
  INITIAL 65536 
  NEXT 1048576 
  MINEXTENTS 1
  MAXEXTENTS 2147483645
  BUFFER_POOL DEFAULT
)
PARALLEL 1
NOCACHE
DISABLE ROW MOVEMENT
;
COMMENT ON COLUMN "SCOTT"."SCADA_REPORT_XN_MID"."SRXM_ORG_ID" IS '机构号0080';
COMMENT ON COLUMN "SCOTT"."SCADA_REPORT_XN_MID"."SRXM_ID" IS '记录ID,20位，机构内连续，机构号4位，年月6位，流水10位';
COMMENT ON COLUMN "SCOTT"."SCADA_REPORT_XN_MID"."FLMETER_NO" IS '流量计编号，导入后从SCADA_FLMETER_INFO update';
COMMENT ON COLUMN "SCOTT"."SCADA_REPORT_XN_MID"."COMM_NO" IS '通讯编号，meter_comm_no';
COMMENT ON COLUMN "SCOTT"."SCADA_REPORT_XN_MID"."REPORT_TIME" IS '报表生成时间，report_gen_time';
COMMENT ON COLUMN "SCOTT"."SCADA_REPORT_XN_MID"."YEAR" IS '年（业务发生），report_year';
COMMENT ON COLUMN "SCOTT"."SCADA_REPORT_XN_MID"."MONTH" IS '月（业务发生），report_month';
COMMENT ON COLUMN "SCOTT"."SCADA_REPORT_XN_MID"."DAY" IS '日（业务发生），report_day';
COMMENT ON COLUMN "SCOTT"."SCADA_REPORT_XN_MID"."STD_SUM" IS '标况总量（期末数），std_sum';
COMMENT ON COLUMN "SCOTT"."SCADA_REPORT_XN_MID"."WORK_SUM" IS '工况总量（期末数），work_sum';
COMMENT ON COLUMN "SCOTT"."SCADA_REPORT_XN_MID"."PRICE" IS '单价（curr_price）';
COMMENT ON COLUMN "SCOTT"."SCADA_REPORT_XN_MID"."THIS_CYCLE_SUM" IS '周期内标况使用量（this_cycle_sum）';
COMMENT ON COLUMN "SCOTT"."SCADA_REPORT_XN_MID"."CYCLE_USE_MONEY" IS '周期内使用额（未启用）';
COMMENT ON COLUMN "SCOTT"."SCADA_REPORT_XN_MID"."THIS_DAY_SUM" IS '当天用量this_day_sum';
COMMENT ON COLUMN "SCOTT"."SCADA_REPORT_XN_MID"."SUM_TOTAL_MONEY" IS '总累计使用金额（未启用）';
COMMENT ON COLUMN "SCOTT"."SCADA_REPORT_XN_MID"."TOTAL_BUY_VOLUME" IS '累购气量（未启用）';
COMMENT ON COLUMN "SCOTT"."SCADA_REPORT_XN_MID"."TOTAL_BUY_MONEY" IS '累购金额（未启用）';
COMMENT ON COLUMN "SCOTT"."SCADA_REPORT_XN_MID"."REMAIN_MONEY" IS '剩余金额（remain_money）';
COMMENT ON COLUMN "SCOTT"."SCADA_REPORT_XN_MID"."REMAIN_VOLUME" IS '剩余数量（remain_volume）';
COMMENT ON COLUMN "SCOTT"."SCADA_REPORT_XN_MID"."FM_STATE" IS '流量计状态，按位存放（meter_state）';
COMMENT ON COLUMN "SCOTT"."SCADA_REPORT_XN_MID"."BATTERY_VOLTAGE" IS '电池电压（battery_voltage）';
COMMENT ON COLUMN "SCOTT"."SCADA_REPORT_XN_MID"."BATTERY_LEVEL" IS '电池电量（battery_level）';
COMMENT ON COLUMN "SCOTT"."SCADA_REPORT_XN_MID"."RSSI" IS '信号强度（rssi）';
COMMENT ON COLUMN "SCOTT"."SCADA_REPORT_XN_MID"."FM_STATE_MSG" IS '表状态解析（meter_stat_emsg）';
COMMENT ON TABLE "SCOTT"."SCADA_REPORT_XN_MID" IS '中间表，导入西宁远传膜表月报数据meter_report_month_yyyymm';

-- ----------------------------
-- Primary Key structure for table SCADA_REPORT_XN_MID
-- ----------------------------
ALTER TABLE "SCOTT"."SCADA_REPORT_XN_MID" ADD CONSTRAINT "SYS_C0086419" PRIMARY KEY ("SRXM_ORG_ID", "SRXM_ID");

-- ----------------------------
-- Checks structure for table SCADA_REPORT_XN_MID
-- ----------------------------
ALTER TABLE "SCOTT"."SCADA_REPORT_XN_MID" ADD CONSTRAINT "SYS_C0076989" CHECK ("SRXM_ORG_ID" IS NOT NULL) NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;
ALTER TABLE "SCOTT"."SCADA_REPORT_XN_MID" ADD CONSTRAINT "SYS_C0076990" CHECK ("SRXM_ID" IS NOT NULL) NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;
ALTER TABLE "SCOTT"."SCADA_REPORT_XN_MID" ADD CONSTRAINT "SYS_C0077294" CHECK ("SRXM_ORG_ID" IS NOT NULL) NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;
ALTER TABLE "SCOTT"."SCADA_REPORT_XN_MID" ADD CONSTRAINT "SYS_C0077295" CHECK ("SRXM_ID" IS NOT NULL) NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;
ALTER TABLE "SCOTT"."SCADA_REPORT_XN_MID" ADD CONSTRAINT "SYS_C0086417" CHECK ("SRXM_ORG_ID" IS NOT NULL) NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;
ALTER TABLE "SCOTT"."SCADA_REPORT_XN_MID" ADD CONSTRAINT "SYS_C0086418" CHECK ("SRXM_ID" IS NOT NULL) NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;
ALTER TABLE "SCOTT"."SCADA_REPORT_XN_MID" ADD CONSTRAINT "SYS_C0086685" CHECK ("SRXM_ORG_ID" IS NOT NULL) NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;
ALTER TABLE "SCOTT"."SCADA_REPORT_XN_MID" ADD CONSTRAINT "SYS_C0086686" CHECK ("SRXM_ID" IS NOT NULL) NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;
ALTER TABLE "SCOTT"."SCADA_REPORT_XN_MID" ADD CONSTRAINT "SYS_C0086696" CHECK ("SRXM_ORG_ID" IS NOT NULL) NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;
ALTER TABLE "SCOTT"."SCADA_REPORT_XN_MID" ADD CONSTRAINT "SYS_C0086697" CHECK ("SRXM_ID" IS NOT NULL) NOT DEFERRABLE INITIALLY IMMEDIATE NORELY VALIDATE;

-- ----------------------------
-- Indexes structure for table SCADA_REPORT_XN_MID
-- ----------------------------
CREATE INDEX "SCOTT"."COMM_NO_XN_MID"
  ON "SCOTT"."SCADA_REPORT_XN_MID" ("COMM_NO" ASC)
  LOGGING
  TABLESPACE "USERS"
  VISIBLE
PCTFREE 10
INITRANS 2
STORAGE (
  INITIAL 65536 
  NEXT 1048576 
  MINEXTENTS 1
  MAXEXTENTS 2147483645
  BUFFER_POOL DEFAULT
);
CREATE INDEX "SCOTT"."FLMETER_NO_XN_MID"
  ON "SCOTT"."SCADA_REPORT_XN_MID" ("FLMETER_NO" ASC)
  LOGGING
  TABLESPACE "USERS"
  VISIBLE
PCTFREE 10
INITRANS 2
STORAGE (
  INITIAL 65536 
  NEXT 1048576 
  MINEXTENTS 1
  MAXEXTENTS 2147483645
  BUFFER_POOL DEFAULT
);
CREATE INDEX "SCOTT"."SRM_ORG_ID_XN_MID"
  ON "SCOTT"."SCADA_REPORT_XN_MID" ("SRXM_ORG_ID" ASC)
  LOGGING
  TABLESPACE "USERS"
  VISIBLE
PCTFREE 10
INITRANS 2
STORAGE (
  INITIAL 65536 
  NEXT 1048576 
  MINEXTENTS 1
  MAXEXTENTS 2147483645
  BUFFER_POOL DEFAULT
);
```
