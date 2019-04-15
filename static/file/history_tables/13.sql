-- 插入商品间规则关系表 3-427行[0, 1, 4, 5, 6, 7, 8]//[0, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12]
-- 将商品ID为130080008809的商品与商品ID为130000000653-130000000652的商品互斥
--0
insert into ucr_iupc.PM_OFFER_REL (REL_ID, OFFER_ID, REL_TYPE, REL_OFFER_ID, VALID_DATE, EXPIRE_DATE, DONE_CODE, CREATE_DATE, DONE_DATE, OP_ID, ORG_ID, REMARK)
values ('100000971864', '130080008809', '0', '130000000653', to_date('01-05-2005', 'dd-mm-yyyy'), to_date('31-12-2050', 'dd-mm-yyyy'), '18011700011224', to_date('17-01-2018 21:40:54', 'dd-mm-yyyy hh24:mi:ss'), to_date('17-01-2018 21:40:54', 'dd-mm-yyyy hh24:mi:ss'), 'HNSJ1213', '35541', '');
--1
insert into ucr_iupc.PM_OFFER_REL (REL_ID, OFFER_ID, REL_TYPE, REL_OFFER_ID, VALID_DATE, EXPIRE_DATE, DONE_CODE, CREATE_DATE, DONE_DATE, OP_ID, ORG_ID, REMARK)
values ('100000971865', '130080008809', '0', '130000000654', to_date('01-05-2005', 'dd-mm-yyyy'), to_date('31-12-2050', 'dd-mm-yyyy'), '18011700011224', to_date('17-01-2018 21:40:54', 'dd-mm-yyyy hh24:mi:ss'), to_date('17-01-2018 21:40:54', 'dd-mm-yyyy hh24:mi:ss'), 'HNSJ1213', '35541', '');
--4
insert into ucr_iupc.PM_OFFER_REL (REL_ID, OFFER_ID, REL_TYPE, REL_OFFER_ID, VALID_DATE, EXPIRE_DATE, DONE_CODE, CREATE_DATE, DONE_DATE, OP_ID, ORG_ID, REMARK)
values ('100000971868', '130080008809', '0', '130000000658', to_date('01-05-2005', 'dd-mm-yyyy'), to_date('31-12-2050', 'dd-mm-yyyy'), '18011700011224', to_date('17-01-2018 21:40:54', 'dd-mm-yyyy hh24:mi:ss'), to_date('17-01-2018 21:40:54', 'dd-mm-yyyy hh24:mi:ss'), 'HNSJ1213', '35541', '');
--5
insert into ucr_iupc.PM_OFFER_REL (REL_ID, OFFER_ID, REL_TYPE, REL_OFFER_ID, VALID_DATE, EXPIRE_DATE, DONE_CODE, CREATE_DATE, DONE_DATE, OP_ID, ORG_ID, REMARK)
values ('100000971869', '130080008809', '0', '130000000659', to_date('01-05-2005', 'dd-mm-yyyy'), to_date('31-12-2050', 'dd-mm-yyyy'), '18011700011224', to_date('17-01-2018 21:40:54', 'dd-mm-yyyy hh24:mi:ss'), to_date('17-01-2018 21:40:54', 'dd-mm-yyyy hh24:mi:ss'), 'HNSJ1213', '35541', '');
--6
insert into ucr_iupc.PM_OFFER_REL (REL_ID, OFFER_ID, REL_TYPE, REL_OFFER_ID, VALID_DATE, EXPIRE_DATE, DONE_CODE, CREATE_DATE, DONE_DATE, OP_ID, ORG_ID, REMARK)
values ('100000971870', '130080008809', '0', '130000000660', to_date('01-05-2005', 'dd-mm-yyyy'), to_date('31-12-2050', 'dd-mm-yyyy'), '18011700011224', to_date('17-01-2018 21:40:54', 'dd-mm-yyyy hh24:mi:ss'), to_date('17-01-2018 21:40:54', 'dd-mm-yyyy hh24:mi:ss'), 'HNSJ1213', '35541', '');
--7
insert into ucr_iupc.PM_OFFER_REL (REL_ID, OFFER_ID, REL_TYPE, REL_OFFER_ID, VALID_DATE, EXPIRE_DATE, DONE_CODE, CREATE_DATE, DONE_DATE, OP_ID, ORG_ID, REMARK)
values ('100000971871', '130080008809', '0', '130000000661', to_date('01-05-2005', 'dd-mm-yyyy'), to_date('31-12-2050', 'dd-mm-yyyy'), '18011700011224', to_date('17-01-2018 21:40:54', 'dd-mm-yyyy hh24:mi:ss'), to_date('17-01-2018 21:40:54', 'dd-mm-yyyy hh24:mi:ss'), 'HNSJ1213', '35541', '');
--8
insert into ucr_iupc.PM_OFFER_REL (REL_ID, OFFER_ID, REL_TYPE, REL_OFFER_ID, VALID_DATE, EXPIRE_DATE, DONE_CODE, CREATE_DATE, DONE_DATE, OP_ID, ORG_ID, REMARK)
values ('100000971872', '130080008809', '0', '130000000662', to_date('01-05-2005', 'dd-mm-yyyy'), to_date('31-12-2050', 'dd-mm-yyyy'), '18011700011224', to_date('17-01-2018 21:40:54', 'dd-mm-yyyy hh24:mi:ss'), to_date('17-01-2018 21:40:54', 'dd-mm-yyyy hh24:mi:ss'), 'HNSJ1213', '35541', '');
-- t1
insert into ucr_iupc.PM_PRICE (PRICE_ID, PRICE_NAME, FEE, UNIT, DESCRIPTION, STATUS, DONE_CODE, CREATE_DATE, DONE_DATE, OP_ID, ORG_ID, REMARK)
values ('500000026044', '', '0', '1', '', '1', '18011700011223', to_date('17-01-2018 21:34:57', 'dd-mm-yyyy hh24:mi:ss'), to_date('17-01-2018 21:34:57', 'dd-mm-yyyy hh24:mi:ss'), 'HNSJ1213', '35541', '');
-- t4
insert into ucr_iupc.PM_PRICE_PRICEPLAN_REL (REL_ID, PRICE_ID, PRICE_PLAN_ID, VALID_DATE, EXPIRE_DATE, DONE_CODE, CREATE_DATE, DONE_DATE, OP_ID, ORG_ID, REMARK)
values ('100000032826', '500000026044', '300030004944', to_date('17-01-2018 18:13:41', 'dd-mm-yyyy hh24:mi:ss'), to_date('31-12-2050', 'dd-mm-yyyy'), '18011700011223', to_date('17-01-2018 21:34:57', 'dd-mm-yyyy hh24:mi:ss'), to_date('17-01-2018 21:34:57', 'dd-mm-yyyy hh24:mi:ss'), 'HNSJ1213', '35541', '');
-- t5
insert into ucr_iupc.PM_OFFER_PRICE_REL (REL_ID, OFFER_ID, PRICE_ID, IS_NEG, EXPIRE_DATE, VALID_DATE, DONE_CODE, CREATE_DATE, DONE_DATE, OP_ID, ORG_ID, REMARK)
values ('100000219749', '130080008808', '500000026044', '', to_date('31-12-2050', 'dd-mm-yyyy'), to_date('17-01-2018 18:13:41', 'dd-mm-yyyy hh24:mi:ss'), '18011700011223', to_date('17-01-2018 21:34:57', 'dd-mm-yyyy hh24:mi:ss'), to_date('17-01-2018 21:34:57', 'dd-mm-yyyy hh24:mi:ss'), 'HNSJ1213', '35541', '');
--t6
insert into ucr_iupc.PM_PROD_SPEC (PROD_SPEC_ID, PROD_TYPE, PROD_NAME, DESCRIPTION, PROD_VERSION, STATUS, DONE_CODE, CREATE_DATE, DONE_DATE, OP_ID, ORG_ID, REMARK)
values ('300000004607', 'D', '4G·ÉÏí138ÔªÌ×²Í', '4G·ÉÏí138ÔªÌ×²Í£¨ÔÂ·Ñ138Ôª£¬Ò»´ÎÐÔÊÕÈ¡£¬º¬À´µçÏÔÊ¾¡¢450·ÖÖÓ¹úÄÚ²¦´ò¹úÄÚµç»°Ê±³¤£»¹úÄÚ½ÓÌý0Ôª£»³¬³öÌ×²Íºó£¬¹úÄÚ²¦´ò¹úÄÚµç»°0.19Ôª/·ÖÖÓ¡£¹úÄÚÒµÎñ²»º¬¸Û°ÄÌ¨ÒµÎñ£©', '', '1', '18011700011224', to_date('17-01-2018 21:40:54', 'dd-mm-yyyy hh24:mi:ss'), to_date('17-01-2018 21:40:54', 'dd-mm-yyyy hh24:mi:ss'), 'HNSJ1213', '35541', '');
-- t7
insert into ucr_iupc.PM_OFFER_PROD_REL (REL_ID, OFFER_ID, PROD_SPEC_ID, VALID_DATE, EXPIRE_DATE, DONE_CODE, CREATE_DATE, DONE_DATE, OP_ID, ORG_ID, REMARK)
values ('100000167807', '130080008808', '300000004606', to_date('17-01-2018 18:13:41', 'dd-mm-yyyy hh24:mi:ss'), to_date('31-12-2050', 'dd-mm-yyyy'), '18011700011223', to_date('17-01-2018 21:34:57', 'dd-mm-yyyy hh24:mi:ss'), to_date('17-01-2018 21:34:57', 'dd-mm-yyyy hh24:mi:ss'), 'HNSJ1213', '35541', '');
-- t8
insert into ucr_iupc.PM_PROD_SPEC (PROD_SPEC_ID, PROD_TYPE, PROD_NAME, DESCRIPTION, PROD_VERSION, STATUS, DONE_CODE, CREATE_DATE, DONE_DATE, OP_ID, ORG_ID, REMARK)
values ('300000004606', 'D', '4G·ÉÏí138ÔªÌ×²ÍÔùËÍ7GB¹úÄÚÁ÷Á¿', '4G·ÉÏí138ÔªÌ×²ÍÔùËÍ7GB¹úÄÚÁ÷Á¿£¨Ì×²ÍÉúÐ§Ç°12¸öÔÂ£¬Ã¿ÔÂÔùËÍ7GB¹úÄÚÁ÷Á¿£©', '', '1', '18011700011223', to_date('17-01-2018 21:34:57', 'dd-mm-yyyy hh24:mi:ss'), to_date('17-01-2018 21:34:57', 'dd-mm-yyyy hh24:mi:ss'), 'HNSJ1213', '35541', '');
--t9
insert into ucr_iupc.PM_OFFER (OFFER_ID, OFFER_TYPE, OFFER_CODE, OFFER_NAME, DESCRIPTION, BRAND_ID, CATEGORY_ID, OFFER_DETAILS, ORDER_MODE, STATUS, VALID_DATE, EXPIRE_DATE, IS_COMP, IS_MAIN, VERSION_NO, OFFER_LINE_ID, DONE_CODE, CREATE_DATE, DONE_DATE, OP_ID, ORG_ID, REMARK)
values ('130080008808', 'D', '80008808', '4G·ÉÏí138ÔªÌ×²ÍÔùËÍ7GB¹úÄÚÁ÷Á¿', '4G·ÉÏí138ÔªÌ×²ÍÔùËÍ7GB¹úÄÚÁ÷Á¿£¨Ì×²ÍÉúÐ§Ç°12¸öÔÂ£¬Ã¿ÔÂÔùËÍ7GB¹úÄÚÁ÷Á¿£©', '100000000001', '100000000118', '', '', '5', to_date('17-01-2018 18:13:41', 'dd-mm-yyyy hh24:mi:ss'), to_date('31-12-2050', 'dd-mm-yyyy'), '0', '0', '', '', '18011700011223', to_date('17-01-2018 21:34:57', 'dd-mm-yyyy hh24:mi:ss'), to_date('17-01-2018 21:34:57', 'dd-mm-yyyy hh24:mi:ss'), 'HNSJ1213', '35541', '');
--t10
insert into ucr_iupc.PM_OFFER_JOIN_REL (REL_ID, REL_TYPE, OFFER_ID, REL_OFFER_ID, ROLE_CODE, SELECT_FLAG, VALID_DATE, EXPIRE_DATE, DONE_CODE, CREATE_DATE, DONE_DATE, OP_ID, ORG_ID, REMARK)
values ('110000040118', '0', '110084007239', '110010002000', null, null, to_date('01-05-2011 15:37:11', 'dd-mm-yyyy hh24:mi:ss'), to_date('31-12-2099', 'dd-mm-yyyy'), '18011800013429', to_date('28-05-2017 21:00:08', 'dd-mm-yyyy hh24:mi:ss'), to_date('28-05-2017 21:00:08', 'dd-mm-yyyy hh24:mi:ss'), 'yinhq', '00000', '²úÉÌÆ·ÖÐÐÄÊý¾Ýµ¹»»');
--t11
insert into ucr_iupc.PM_OFFER_GROUP_REL (REL_ID, OFFER_ID, GROUP_ID, ROLE_CODE, SELECT_FLAG, LIMIT_TYPE, MAX_NUM, MIN_NUM, VALID_DATE, EXPIRE_DATE, DONE_CODE, CREATE_DATE, DONE_DATE, OP_ID, ORG_ID, REMARK)
values ('110000015401', '110084007239', '10000961', '0', '2', null, '-1', '-1', to_date('27-02-2012 03:02:05', 'dd-mm-yyyy hh24:mi:ss'), to_date('31-12-2050 12:12:00', 'dd-mm-yyyy hh24:mi:ss'), '18011800013429', to_date('18-01-2018 16:27:25', 'dd-mm-yyyy hh24:mi:ss'), to_date('18-01-2018 16:27:25', 'dd-mm-yyyy hh24:mi:ss'), null, null, null);
--t12
insert into ucr_iupc.PM_ENABLE_MODE_REL (REL_ID, REL_OBJECT, REL_OBJECT_ID, ENABLE_MODE_ID, VALID_DATE, EXPIRE_DATE, DONE_CODE, CREATE_DATE, DONE_DATE, OP_ID, ORG_ID, REMARK)
values ('110000031266', '2', '110000040118', '100000000049', to_date('18-01-2018 16:45:16', 'dd-mm-yyyy hh24:mi:ss'), to_date('31-12-2050', 'dd-mm-yyyy'), '18011800013429', to_date('18-01-2018 16:45:16', 'dd-mm-yyyy hh24:mi:ss'), to_date('18-01-2018 16:45:16', 'dd-mm-yyyy hh24:mi:ss'), 'HNSJ1213', '35541', null);
