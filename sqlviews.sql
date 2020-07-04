--一些修改： 创建几个视图 ； 
use air
GO

--插入几条数据删着玩玩
INSERT INTO 订票
VALUES
(1,'首都机场','黄沙机场','021','经济舱','余夏','test1','男','老人','4135402196402122371','13837439823'),
(1,'首都机场','双流机场','022','经济舱','地平线~','test2','男','残疾','423001199902122391','13837434523'),
(6,'南苑机场','虹桥机场','011','经济舱','余夏','test3','女','小孩','311002201402122321','13823879823'),
(7,'南苑机场','虹桥机场','012','经济舱','余夏','test4','男','病人','311002197302122361','13823879823'),
(5,'首都机场','高崎机场','011','商务舱','余夏','test5','女','成人','311002197603132491','13928376273')
GO


if exists (select table_name from INFORMATION_SCHEMA.VIEWS where TABLE_NAME = '用户购票信息')
	drop view 用户购票信息
go


--出发-经停机场……
if exists (select table_name from INFORMATION_SCHEMA.VIEWS where TABLE_NAME = '出发经停')
	drop view 出发经停
go
Create view 出发经停
AS
select a.航班编号,a.出发机场 AS 出发地,c.经停机场 AS 目的地 from (select b1.航班编号 , b2.机场名 AS 出发机场  from 航班  b1 inner join 机场 b2 on b1.出发机场代码 = b2.机场代码) a
   inner join (select b1.航班编号 , b2.机场名 AS 经停机场  from 航班  b1 inner join 机场 b2 on b1.经停机场代码 = b2.机场代码) c
on a.航班编号 = c.航班编号
GO

--经停-到达机场……
if exists (select table_name from INFORMATION_SCHEMA.VIEWS where TABLE_NAME = '经停到达')
	drop view 经停到达
go
Create view 经停到达
AS
select a.航班编号,a.经停机场 AS 出发地 ,c.终到机场 AS 目的地 from (select b1.航班编号 , b2.机场名 AS 经停机场  from 航班  b1 inner join 机场 b2 on b1.经停机场代码 = b2.机场代码) a
   inner join (select b1.航班编号 , b2.机场名 AS 终到机场  from 航班  b1 inner join 机场 b2 on b1.到达机场代码 = b2.机场代码) c
on a.航班编号 = c.航班编号
GO

--出发-到达机场的所有名称……
if exists (select table_name from INFORMATION_SCHEMA.VIEWS where TABLE_NAME = '出发到达')
	drop view 出发到达
go
Create view 出发到达
AS
select a.航班编号,a.出发机场 AS 出发地,c.终到机场 AS 目的地 from (select b1.航班编号 , b2.机场名 AS 出发机场  from 航班  b1 inner join 机场 b2 on b1.出发机场代码 = b2.机场代码) a
   inner join (select b1.航班编号 , b2.机场名 AS 终到机场  from 航班  b1 inner join 机场 b2 on b1.到达机场代码 = b2.机场代码) c
on a.航班编号 = c.航班编号
GO

if exists (select table_name from INFORMATION_SCHEMA.VIEWS where TABLE_NAME = '订票表与飞行计划整合')
	drop view 订票表与飞行计划整合
GO
--订票与飞行计划整合
create view 订票表与飞行计划整合
As
select a.航班编号,a.计划出发时间,a.计划从经停机场出发时间,a.计划到达经停机场时间,a.计划到达时间,a.[票价（开始-到达，商务舱）], a.[票价（开始-到达，头等舱）],a.[票价（开始-到达，经济舱）],
a.[票价（开始-经停，商务舱）],a.[票价（开始-经停，头等舱）],a.[票价（开始-经停，经济舱）],a.[票价（经停-到达，商务舱）],a.[票价（经停-到达，头等舱）],a.[票价（经停-到达，经济舱）],b.*
  from 飞行计划安排 a inner join 订票 b  ON a.航程号=b.航程号
go

--最终的视图： 用户购票信息
create view 用户购票信息
AS
(select a1.机票编号,a1.计划出发时间 As 出发时间, a1.计划到达经停机场时间 AS 到达时间,a1.乘客姓名,a1.乘客类别,a1.[乘客身份证号/护照号],a1.用户名,a1.航程号,a1.舱位,a1.[票价（开始-经停，商务舱）] AS 票价,a2.出发地, a2.目的地 
 from 订票表与飞行计划整合 a1 inner join 出发经停  a2
	ON a1.航班编号 = a2.航班编号  where a1.目的机场 = a2.目的地 and  a1.出发机场 = a2.出发地 and a1.舱位 = '商务舱')
Union
(select a1.机票编号 , a1.计划从经停机场出发时间 As 出发时间, a1.计划到达时间 AS 到达时间,a1.乘客姓名,a1.乘客类别,a1.[乘客身份证号/护照号],a1.用户名,a1.航程号,a1.舱位, a1.[票价（经停-到达，商务舱）] AS 票价 , a2.出发地, a2.目的地 
from 订票表与飞行计划整合 a1 inner join 经停到达  a2
	ON a1.航班编号 = a2.航班编号  where a1.目的机场 = a2.目的地 and  a1.出发机场 = a2.出发地 and a1.舱位 = '商务舱')
Union
(select a1.机票编号,a1.计划出发时间 As 出发时间, a1.计划到达时间 AS 到达时间,a1.乘客姓名,a1.乘客类别,a1.[乘客身份证号/护照号],a1.用户名,a1.航程号,a1.舱位,a1.[票价（开始-到达，商务舱）] AS 票价,a2.出发地, a2.目的地 
 from 订票表与飞行计划整合 a1 inner join 出发到达  a2
	ON a1.航班编号 = a2.航班编号  where a1.目的机场 = a2.目的地 and  a1.出发机场 = a2.出发地 and a1.舱位 = '商务舱')
Union
(select a1.机票编号,a1.计划出发时间 As 出发时间, a1.计划到达经停机场时间 AS 到达时间,a1.乘客姓名,a1.乘客类别,a1.[乘客身份证号/护照号],a1.用户名,a1.航程号,a1.舱位,a1.[票价（开始-经停，头等舱）] AS 票价,a2.出发地, a2.目的地 
 from 订票表与飞行计划整合 a1 inner join 出发经停  a2
	ON a1.航班编号 = a2.航班编号  where a1.目的机场 = a2.目的地 and  a1.出发机场 = a2.出发地 and a1.舱位 = '头等舱')
Union
(select a1.机票编号, a1.计划从经停机场出发时间 As 出发时间, a1.计划到达时间 AS 到达时间 , a1.乘客姓名,a1.乘客类别,a1.[乘客身份证号/护照号],a1.用户名,a1.航程号,a1.舱位, a1.[票价（经停-到达，头等舱）] AS 票价 , a2.出发地, a2.目的地 
 from 订票表与飞行计划整合 a1 inner join 经停到达  a2
	ON a1.航班编号 = a2.航班编号  where a1.目的机场 = a2.目的地 and  a1.出发机场 = a2.出发地 and a1.舱位 = '头等舱')
Union
(select a1.机票编号, a1.计划出发时间 As 出发时间, a1.计划到达时间 AS 到达时间,a1.乘客姓名, a1.乘客类别, a1.[乘客身份证号/护照号],a1.用户名,a1.航程号,a1.舱位,a1.[票价（开始-到达，头等舱）] AS 票价,a2.出发地, a2.目的地 
 from 订票表与飞行计划整合 a1 inner join 出发到达  a2
	ON a1.航班编号 = a2.航班编号  where a1.目的机场 = a2.目的地 and  a1.出发机场 = a2.出发地 and a1.舱位 = '头等舱')
Union
(select a1.机票编号,a1.计划出发时间 As 出发时间, a1.计划到达经停机场时间 AS 到达时间,a1.乘客姓名,a1.乘客类别,a1.[乘客身份证号/护照号],a1.用户名,a1.航程号,a1.舱位,a1.[票价（开始-经停，经济舱）] AS 票价,a2.出发地, a2.目的地 
 from 订票表与飞行计划整合 a1 inner join 出发经停  a2
	ON a1.航班编号 = a2.航班编号  where a1.目的机场 = a2.目的地 and  a1.出发机场 = a2.出发地 and a1.舱位 = '经济舱')
Union
(select a1.机票编号, a1.计划从经停机场出发时间 As 出发时间, a1.计划到达时间 AS 到达时间, a1.乘客姓名,a1.乘客类别,a1.[乘客身份证号/护照号],a1.用户名,a1.航程号,a1.舱位, a1.[票价（经停-到达，经济舱）] AS 票价 , a2.出发地, a2.目的地 
from 订票表与飞行计划整合 a1 inner join 经停到达  a2
	ON a1.航班编号 = a2.航班编号  where a1.目的机场 = a2.目的地 and  a1.出发机场 = a2.出发地 and a1.舱位 = '经济舱')
Union
(select a1.机票编号,a1.计划出发时间 As 出发时间, a1.计划到达时间 AS 到达时间,a1.乘客姓名,a1.乘客类别,a1.[乘客身份证号/护照号],a1.用户名,a1.航程号,a1.舱位,a1.[票价（开始-到达，经济舱）] AS 票价,a2.出发地, a2.目的地 
 from 订票表与飞行计划整合 a1 inner join 出发到达  a2
	ON a1.航班编号 = a2.航班编号  where a1.目的机场 = a2.目的地 and  a1.出发机场 = a2.出发地 and a1.舱位 = '经济舱')
GO


