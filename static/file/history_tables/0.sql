-- 插入商品间规则关系表 3-427行//0,1,4
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
