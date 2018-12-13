/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306-root-root
 Source Server Type    : MySQL
 Source Server Version : 50640
 Source Host           : localhost:3306
 Source Schema         : demo

 Target Server Type    : MySQL
 Target Server Version : 50640
 File Encoding         : 65001

 Date: 13/12/2018 13:47:13
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 37 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO `auth_permission` VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES (24, 'Can view session', 6, 'view_session');
INSERT INTO `auth_permission` VALUES (25, 'Can add 学科', 7, 'add_subject');
INSERT INTO `auth_permission` VALUES (26, 'Can change 学科', 7, 'change_subject');
INSERT INTO `auth_permission` VALUES (27, 'Can delete 学科', 7, 'delete_subject');
INSERT INTO `auth_permission` VALUES (28, 'Can view 学科', 7, 'view_subject');
INSERT INTO `auth_permission` VALUES (29, 'Can add 讲师', 8, 'add_teacher');
INSERT INTO `auth_permission` VALUES (30, 'Can change 讲师', 8, 'change_teacher');
INSERT INTO `auth_permission` VALUES (31, 'Can delete 讲师', 8, 'delete_teacher');
INSERT INTO `auth_permission` VALUES (32, 'Can view 讲师', 8, 'view_teacher');
INSERT INTO `auth_permission` VALUES (33, 'Can add 用户', 9, 'add_user');
INSERT INTO `auth_permission` VALUES (34, 'Can change 用户', 9, 'change_user');
INSERT INTO `auth_permission` VALUES (35, 'Can delete 用户', 9, 'delete_user');
INSERT INTO `auth_permission` VALUES (36, 'Can view 用户', 9, 'view_user');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `first_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES (1, 'pbkdf2_sha256$120000$PmIUfBPO0G0s$KpxpifradFp4eZ/2PaDWLRFY8QcqI/Yu0rBwoNvaKXY=', '2018-12-13 05:14:35.541010', 1, 'ahviplc', '', '', 'ahlc@sina.cn', 1, 1, '2018-12-13 05:13:44.665419');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id`, `group_id`) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id`, `permission_id`) USING BTREE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NULL,
  `object_id` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 14 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES (1, '2018-12-13 05:15:05.009021', '1', '数学', 1, '[{\"added\": {}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (2, '2018-12-13 05:15:25.986722', '2', '计算机', 1, '[{\"added\": {}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (3, '2018-12-13 05:16:22.276811', '1', 'Teacher object (1)', 1, '[{\"added\": {}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (4, '2018-12-13 05:25:33.216985', '2', 'Teacher object (2)', 1, '[{\"added\": {}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (5, '2018-12-13 05:25:38.825675', '1', 'Teacher object (1)', 2, '[]', 8, 1);
INSERT INTO `django_admin_log` VALUES (6, '2018-12-13 05:26:31.631226', '3', 'Teacher object (3)', 1, '[{\"added\": {}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (7, '2018-12-13 05:28:02.704339', '3', 'Teacher object (3)', 2, '[{\"changed\": {\"fields\": [\"photo\"]}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (8, '2018-12-13 05:28:33.991851', '3', 'Teacher object (3)', 2, '[{\"changed\": {\"fields\": [\"photo\"]}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (9, '2018-12-13 05:28:47.231211', '3', 'Teacher object (3)', 2, '[{\"changed\": {\"fields\": [\"photo\"]}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (10, '2018-12-13 05:29:12.401807', '3', 'Teacher object (3)', 2, '[{\"changed\": {\"fields\": [\"photo\"]}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (11, '2018-12-13 05:30:03.591191', '3', 'Teacher object (3)', 2, '[{\"changed\": {\"fields\": [\"name\", \"photo\"]}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (12, '2018-12-13 05:31:27.265105', '1', 'Teacher object (1)', 2, '[{\"changed\": {\"fields\": [\"photo\"]}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (13, '2018-12-13 05:32:12.227123', '2', 'Teacher object (2)', 2, '[{\"changed\": {\"fields\": [\"photo\"]}}]', 8, 1);

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (7, 'demo', 'subject');
INSERT INTO `django_content_type` VALUES (8, 'demo', 'teacher');
INSERT INTO `django_content_type` VALUES (9, 'demo', 'user');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `applied` datetime(6) NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 21 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2018-12-13 05:10:14.793810');
INSERT INTO `django_migrations` VALUES (2, 'auth', '0001_initial', '2018-12-13 05:10:16.011483');
INSERT INTO `django_migrations` VALUES (3, 'admin', '0001_initial', '2018-12-13 05:10:16.299147');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2018-12-13 05:10:16.316102');
INSERT INTO `django_migrations` VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2018-12-13 05:10:16.332087');
INSERT INTO `django_migrations` VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2018-12-13 05:10:16.494824');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0002_alter_permission_name_max_length', '2018-12-13 05:10:16.619581');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0003_alter_user_email_max_length', '2018-12-13 05:10:16.720410');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0004_alter_user_username_opts', '2018-12-13 05:10:16.732406');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0005_alter_user_last_login_null', '2018-12-13 05:10:16.812185');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0006_require_contenttypes_0002', '2018-12-13 05:10:16.817157');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0007_alter_validators_add_error_messages', '2018-12-13 05:10:16.829125');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0008_alter_user_username_max_length', '2018-12-13 05:10:16.924989');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0009_alter_user_last_name_max_length', '2018-12-13 05:10:17.037885');
INSERT INTO `django_migrations` VALUES (15, 'demo', '0001_initial', '2018-12-13 05:10:17.237607');
INSERT INTO `django_migrations` VALUES (16, 'demo', '0002_auto_20180704_1117', '2018-12-13 05:10:17.450426');
INSERT INTO `django_migrations` VALUES (17, 'demo', '0003_auto_20180704_1118', '2018-12-13 05:10:17.507257');
INSERT INTO `django_migrations` VALUES (18, 'demo', '0004_auto_20180705_1017', '2018-12-13 05:10:17.684777');
INSERT INTO `django_migrations` VALUES (19, 'demo', '0005_auto_20180706_1458', '2018-12-13 05:10:17.816424');
INSERT INTO `django_migrations` VALUES (20, 'sessions', '0001_initial', '2018-12-13 05:10:17.900201');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `expire_date` datetime(6) NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('dolfqw9hq6lnpoiklhqkb93k72tamle8', 'ZTBiODdiMGE0MDVjYzBjNDU3YTQ3OGJiZmQ4Mzk3ZmQzYTlkY2RjMjqABJWtAQAAAAAAAH2UKIwNX2F1dGhfdXNlcl9pZJSMATGUjBJfYXV0aF91c2VyX2JhY2tlbmSUjClkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZJSMD19hdXRoX3VzZXJfaGFzaJSMKDgzZjI2NTIwNGM1YWZjZjkyMGYzNTNjZWM2ZGIzNTFkMWY2MjFmODeUjAR1c2VylIwVZGphbmdvLmRiLm1vZGVscy5iYXNllIwObW9kZWxfdW5waWNrbGWUk5SMBGRlbW+UjARVc2VylIaUhZRSlH2UKIwGX3N0YXRllGgIjApNb2RlbFN0YXRllJOUKYGUfZQojAZhZGRpbmeUiYwCZGKUjAdkZWZhdWx0lHVijAJub5RLAYwIdXNlcm5hbWWUjAdzaHZpcGxjlIwIcGFzc3dvcmSUjCgwZGE2M2MyNjdlMjliYmM2MjI3OGVkNDU1MDkwYzFiMzgxZDRkMTRjlIwFZW1haWyUjA1haGxjQHNvaHUuY29tlIwHY291bnRlcpRLAIwPX2RqYW5nb192ZXJzaW9ulIwFMi4xLjOUdWJ1Lg==', '2018-12-13 06:15:03.046107');

-- ----------------------------
-- Table structure for tb_subject
-- ----------------------------
DROP TABLE IF EXISTS `tb_subject`;
CREATE TABLE `tb_subject`  (
  `sno` int(11) NOT NULL AUTO_INCREMENT,
  `sname` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sintro` varchar(511) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`sno`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of tb_subject
-- ----------------------------
INSERT INTO `tb_subject` VALUES (1, '数学', '数学，你的逻辑天堂');
INSERT INTO `tb_subject` VALUES (2, '计算机', '用计算机思维改变世界');

-- ----------------------------
-- Table structure for tb_teacher
-- ----------------------------
DROP TABLE IF EXISTS `tb_teacher`;
CREATE TABLE `tb_teacher`  (
  `tno` int(11) NOT NULL AUTO_INCREMENT,
  `tname` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `tintro` varchar(1023) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `tmotto` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `tphoto` varchar(511) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `tmanager` tinyint(1) NOT NULL,
  `sno` int(11) NOT NULL,
  `tbcount` int(11) NOT NULL,
  `tgcount` int(11) NOT NULL,
  PRIMARY KEY (`tno`) USING BTREE,
  INDEX `tb_teacher_sno_74961b88_fk_tb_subject_sno`(`sno`) USING BTREE,
  CONSTRAINT `tb_teacher_sno_74961b88_fk_tb_subject_sno` FOREIGN KEY (`sno`) REFERENCES `tb_subject` (`sno`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of tb_teacher
-- ----------------------------
INSERT INTO `tb_teacher` VALUES (1, 'LC', '一人一世界，一树一菩提！~LC', '你好好学，我好好教！~LC', 'images/卑鄙的我.jpg', 1, 2, 0, 3);
INSERT INTO `tb_teacher` VALUES (2, 'mwh', '我不会告诉你我很厉害的', '自己先学，先思考', 'images/卑鄙的我3.jpg', 0, 2, 0, 0);
INSERT INTO `tb_teacher` VALUES (3, 'andrew', '数学大神', '数学,你的逻辑天堂', 'images/andrew.png', 0, 1, 0, 0);

-- ----------------------------
-- Table structure for tb_user
-- ----------------------------
DROP TABLE IF EXISTS `tb_user`;
CREATE TABLE `tb_user`  (
  `uno` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `counter` int(11) NOT NULL,
  PRIMARY KEY (`uno`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of tb_user
-- ----------------------------
INSERT INTO `tb_user` VALUES (1, 'shviplc', '0da63c267e29bbc62278ed455090c1b381d4d14c', 'ahlc@sohu.com', 0);

SET FOREIGN_KEY_CHECKS = 1;
