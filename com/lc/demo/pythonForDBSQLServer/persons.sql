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

 Date: 23/02/2019 14:08:59
*/


-- ----------------------------
-- Table structure for persons
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[persons]') AND type IN ('U'))
	DROP TABLE [dbo].[persons]
GO

CREATE TABLE [dbo].[persons] (
  [id] int  NOT NULL,
  [name] varchar(100) COLLATE Chinese_PRC_CI_AS  NULL,
  [salesrep] varchar(100) COLLATE Chinese_PRC_CI_AS  NULL
)
GO

ALTER TABLE [dbo].[persons] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Records of [persons]
-- ----------------------------
INSERT INTO [dbo].[persons]  VALUES (N'1', N'John Smith', N'John Doe')
GO

INSERT INTO [dbo].[persons]  VALUES (N'2', N'Jane Doe', N'Joe Dog')
GO

INSERT INTO [dbo].[persons]  VALUES (N'3', N'Mike T.', N'Sarah H.')
GO


-- ----------------------------
-- Primary Key structure for table persons
-- ----------------------------
ALTER TABLE [dbo].[persons] ADD CONSTRAINT [PK__persons__3213E83F0406723C] PRIMARY KEY CLUSTERED ([id])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO

