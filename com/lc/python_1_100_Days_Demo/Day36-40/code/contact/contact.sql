/*
 Navicat Premium Data Transfer

 Source Server         : ecs-lc-sh-mysql-localhost-root-root
 Source Server Type    : MySQL
 Source Server Version : 50523
 Source Host           : ip:3306
 Source Schema         : contact

 Target Server Type    : MySQL
 Target Server Version : 50523
 File Encoding         : 65001

 Date: 15/11/2018 15:20:06
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for tb_contacter
-- ----------------------------
DROP TABLE IF EXISTS `tb_contacter`;
CREATE TABLE `tb_contacter`  (
  `conid` int(11) NOT NULL AUTO_INCREMENT,
  `conname` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `contel` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `conemail` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`conid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of tb_contacter
-- ----------------------------
INSERT INTO `tb_contacter` VALUES (1, 'ahviplc', '110', '1@qq.com');
INSERT INTO `tb_contacter` VALUES (2, 'LC', '120', '2@qq.com');

SET FOREIGN_KEY_CHECKS = 1;
