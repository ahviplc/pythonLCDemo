/*
 Navicat Premium Data Transfer

 Source Server         : 数据库 腾讯云 43.142.58.153 端口 3306 账户 root 密码 *****
 Source Server Type    : MySQL
 Source Server Version : 80029
 Source Host           : 43.142.58.153:3306
 Source Schema         : reality-tv-search

 Target Server Type    : MySQL
 Target Server Version : 80029
 File Encoding         : 65001

 Date: 22/02/2023 18:17:10
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for tvideo
-- ----------------------------
DROP TABLE IF EXISTS `tvideo`;
CREATE TABLE `tvideo`  (
  `id` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT 'id 主键',
  `abv_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT 'B站视频AV/BV号',
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '视频标题',
  `bili_url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '视频播放url',
  `descs` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '简介',
  `watch_counts` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '观看量',
  `danmu_counts` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '弹幕数量',
  `up_time` int(0) NOT NULL COMMENT '上传时间 时间戳形式',
  `up_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '上传up主昵称',
  `tv_pic` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '封面图片',
  `real_url` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '真实播放地址',
  `tv_duration` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '时长 单位是秒',
  `tv_category` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '视频分类 all 代表综合排序 | click代表最多点击 | pubdate代表最新发布|dm代表最多弹幕|stow代表最多收藏',
  `del_flag` int(0) NULL DEFAULT 0 COMMENT '刪除标识符',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `abv_id`(`abv_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tvideo
-- ----------------------------
INSERT INTO `tvideo` VALUES ('57885eeb-23d2-4ccb-af16-30fc37f5e2e3', 'BV1mj411G7iF', '综艺《关于郑恺不小心把鼻叫成妈这件事》哈哈', 'https://www.bilibili.com/video/BV1mj411G7iF', '简介', '0', '0', 1677022491, '七七七星瓢虫', 'http://i2.hdslb.com/bfs/archive/d4714f39a52e057066668d383f8f50d7bcbcdd02.jpg', 'http://localhost:9527/BV1mj411G7iF-new.mp4', '35', 'pubdate', 0);
INSERT INTO `tvideo` VALUES ('f5686271-c002-46aa-b022-3be4588a0cf9', 'BV1zX4y1X7ts', '影视杂谈男人的头装进50只蜘蛛的玻璃盒子里，挑战极限的真人秀节目', 'https://www.bilibili.com/video/BV1zX4y1X7ts', '', '1', '0', 1677060589, '火鸟说电影', 'http://i1.hdslb.com/bfs/archive/65a61ee23b2224176d0cf52098f1d3f768cca6c3.jpg', 'http://localhost:9527/BV1zX4y1X7ts-new.mp4', '152', 'pubdate', 0);
INSERT INTO `tvideo` VALUES ('f9eb5e06-206f-4d1b-bb79-469694dc19f5', 'BV12v4y1Y7Ay', '粉丝创作相信吸引力法则', 'https://www.bilibili.com/video/BV12v4y1Y7Ay', '简介2', '2', '0', 1677020182, '胜凯盟', 'http://i2.hdslb.com/bfs/archive/3e81e1590b4fc9aec7b7dda160ee6d6774c141f5.jpg', 'http://localhost:9527/BV12v4y1Y7Ay-new.mp4', '24', 'pubdate', 0);

SET FOREIGN_KEY_CHECKS = 1;
