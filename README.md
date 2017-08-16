##爬取阿里小号
---
**爬取阿里小号，将归属地及手机号保存到pg数据库的如下的表里面**

*表结构如下：*

	DROP SEQUENCE IF EXISTS
	"public"."ali_phone_id_seq";
	CREATE SEQUENCE "public"."ali_phone_id_seq"
	INCREMENT 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	START 1
	CACHE 1;

	DROP TABLE IF EXISTS "public"."ali_phone_info";
	CREATE TABLE "public"."ali_phone_info" (
			"id" int4 DEFAULT nextval('ali_phone_id_seq'::regclass) NOT NULL,
			"addr" varchar(64) COLLATE "default" NOT NULL,
			"phone_num" varchar(32) COLLATE "default" NOT NULL
			)
	WITH (OIDS=FALSE)

	;
	COMMENT ON COLUMN "public"."ali_phone_info"."id" IS '手机号码信息ID';
	COMMENT ON COLUMN "public"."ali_phone_info"."addr" IS '号码归属地';
	COMMENT ON COLUMN "public"."ali_phone_info"."phone_num" IS '手机号码';

	-- ----------------------------
	-- Alter Sequences Owned By
	-- ----------------------------

	-- ----------------------------
	-- Primary Key structure for table ali_phone_info
	-- ----------------------------
	ALTER TABLE "public"."ali_phone_info" ADD PRIMARY KEY ("id");

**环境信息**
* CentOS Linux release 7.3.1611
* python 2.7.5
* pip install request
* pip install sqlalchemy
* pip install psycopg2
* psql (9.2.18, server 9.5.0)
