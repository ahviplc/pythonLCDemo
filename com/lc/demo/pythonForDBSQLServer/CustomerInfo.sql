/*
 Navicat Premium Data Transfer

 Source Server         : SQL SERVER-sa-lmt123
 Source Server Type    : SQL Server
 Source Server Version : 10504042
 Source Host           : Server\SQLEXPRESS:1433
 Source Catalog        : HTGasMeterSystemSHLMT
 Source Schema         : dbo

 Target Server Type    : SQL Server
 Target Server Version : 10504042
 File Encoding         : 65001

 Date: 23/02/2019 14:55:14
*/


-- ----------------------------
-- Table structure for CustomerInfo
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[CustomerInfo]') AND type IN ('U'))
	DROP TABLE [dbo].[CustomerInfo]
GO

CREATE TABLE [dbo].[CustomerInfo] (
  [customerNo] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NOT NULL,
  [customerType] int  NULL,
  [contractNo] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [customerName] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [telNo] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [mobileNo] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [certNo] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [estateNo] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [address] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [houseNo] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [cellNo] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [roomNo] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [useState] int  NULL,
  [defineNo1] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [defineNo2] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [defineNo3] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [remark] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [payWay] int  NULL,
  [bankNo] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [bankAuthNo] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [accountNo] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [accountName] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [bankCheck] int  NULL,
  [taxNo] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [enterpriseNo] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [buildTime] datetime  NULL,
  [editTime] datetime  NULL,
  [Operator] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [loginName] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [Password] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [BranchNo] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL
)
GO

ALTER TABLE [dbo].[CustomerInfo] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Records of [CustomerInfo]
-- ----------------------------
INSERT INTO [dbo].[CustomerInfo]  VALUES (N'0000000001', N'0', N'合同号', N'客户名称', N'固定电话', N'手机', N'证件号码', N'0000000000', N'详细地址', N'楼号', N'单元号', N'室号', N'1', N'自定义编号1', N'自定义编号2', N'自定义编号3', N'备注', N'1', N'', N'银行授权码', N'银行账号', N'银行账户名', N'0', N'税号', N'01', N'2018-03-07 09:44:02.220', N'2018-03-07 09:46:58.250', N'管理员', N'', N'', N'0000000000')
GO

INSERT INTO [dbo].[CustomerInfo]  VALUES (N'0000000002', N'0', N'合同号', N'客户名称', N'固定电话', N'手机', N'证件号码', N'0000000000', N'详细地址', N'楼号', N'单元号', N'室号', N'0', N'1', N'2', N'3', N'备注', N'0', N'', N'银行授权码', N'银行账号', N'银行账户名', N'0', N'税号', N'01', N'2018-03-09 09:47:26.683', N'2018-03-09 09:47:26.683', N'管理员', N'123', N'CAF1A3DFB505FFED0D024130F58C5CFA', N'0000000000')
GO


-- ----------------------------
-- Primary Key structure for table CustomerInfo
-- ----------------------------
ALTER TABLE [dbo].[CustomerInfo] ADD CONSTRAINT [PK__CustomerInfo__09353BAD] PRIMARY KEY CLUSTERED ([customerNo])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO

