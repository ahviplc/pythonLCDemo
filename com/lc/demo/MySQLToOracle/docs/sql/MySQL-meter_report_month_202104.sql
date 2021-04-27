/*
 Navicat Premium Data Transfer

 Source Server         : mysql server2 localhost-3306 sql
 Source Server Type    : MySQL
 Source Server Version : 50720
 Source Host           : localhost:3306
 Source Schema         : htiot_qinghaixn_report

 Target Server Type    : MySQL
 Target Server Version : 50720
 File Encoding         : 65001

 Date: 27/04/2021 10:20:37
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
) ENGINE = InnoDB AUTO_INCREMENT = 49665 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
