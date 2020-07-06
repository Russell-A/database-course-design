import pyodbc

conn = pyodbc.connect('DRIVER={SQL SERVER NATIVE CLIENT 10.0};SERVER=127.0.0.1;DATABASE=master;UID=sa;PWD=123456',autocommit= True)
cursor = conn.cursor()
sql = '''if exists(select * from sys.databases where name = 'air')
 DROP database air
create database air
 '''
cursor.execute(sql)
conn.close()


conn = pyodbc.connect('DRIVER={SQL SERVER NATIVE CLIENT 10.0};SERVER=127.0.0.1;DATABASE=air;UID=sa;PWD=123456')
cursor = conn.cursor()

sql = '''if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('航班') and o.name = 'FK_航班_FK_飞机编号_飞机登记')
alter table 航班
   drop constraint FK_航班_FK_飞机编号_飞机登记

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('航班') and o.name = 'FK_航班_机场代码_出发_机场')
alter table 航班
   drop constraint FK_航班_机场代码_出发_机场

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('航班') and o.name = 'FK_航班_机场代码_到达_机场')
alter table 航班
   drop constraint FK_航班_机场代码_到达_机场

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('航班') and o.name = 'FK_航班_机场代码_经停_机场')
alter table 航班
   drop constraint FK_航班_机场代码_经停_机场

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('订票') and o.name = 'FK_订票_用户名_用户表')
alter table 订票
   drop constraint FK_订票_用户名_用户表

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('订票') and o.name = 'FK_订票_航程号_飞行计划安排')
alter table 订票
   drop constraint FK_订票_航程号_飞行计划安排

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('飞机登记') and o.name = 'FK_飞机登记_机型_飞机表')
alter table 飞机登记
   drop constraint FK_飞机登记_机型_飞机表

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('飞行计划安排') and o.name = 'FK_飞行计划安排_航班编号_航程_航班')
alter table 飞行计划安排
   drop constraint FK_飞行计划安排_航班编号_航程_航班

if exists (select 1
            from  sysobjects
           where  id = object_id('机场')
            and   type = 'U')
   drop table 机场

if exists (select 1
            from  sysobjects
           where  id = object_id('用户表')
            and   type = 'U')
   drop table 用户表

if exists (select 1
            from  sysobjects
           where  id = object_id('航班')
            and   type = 'U')
   drop table 航班
if exists (select 1
            from  sysobjects
           where  id = object_id('订票')
            and   type = 'U')
   drop table 订票

if exists (select 1
            from  sysobjects
           where  id = object_id('飞机登记')
            and   type = 'U')
   drop table 飞机登记

if exists (select 1
            from  sysobjects
           where  id = object_id('飞机表')
            and   type = 'U')
   drop table 飞机表

if exists (select 1
            from  sysobjects
           where  id = object_id('飞行计划安排')
            and   type = 'U')
   drop table 飞行计划安排
'''
cursor.execute(sql)
cursor.commit()

sql = ''' create table 机场 (
   机场代码                 varchar(20)          not null,
   机场名                  varchar(50)          not null,
   所在城市                 varchar(20)          not null,
   constraint PK_机场 primary key (机场代码)
)
create table 用户表 (
   用户名                  varchar(20)          not null,
   用户密码                 varchar(20)          not null,
   用户权限                 int                  not null,
   用户联系方式               varchar(20)          not null,
   constraint PK_用户表 primary key (用户名)
)
create table 航班 (
   航班编号                 varchar(10)          not null,
   出发机场代码               varchar(20)          not null,
   经停机场代码               varchar(20)          null,
   到达机场代码               varchar(20)          not null,
   飞机编号                 varchar(10)          null,
   constraint PK_航班 primary key (航班编号),
   constraint AK_UQ_飞机编号_航班 unique (飞机编号)
)
create table 订票 (
   机票编号                 int                  identity,
   航程号                  int                  not null,
   出发机场                 varchar(20)          not null,
   目的机场                 varchar(20)          not null,
   座位编号                 varchar(6)           not null,
   舱位                   varchar(6)           not null,
   用户名                  varchar(20)          not null,
   乘客姓名                 varchar(50)          not null,
   乘客性别                 varchar(2)           not null
      constraint CKC_乘客性别_订票 check (乘客性别 in ('男','女')),
   乘客类别                 varchar(10)          not null
      constraint CKC_乘客类别_订票 check (乘客类别 in ('老人','小孩','孕妇','成人','残疾','病人','<Val8>')),
   "乘客身份证号/护照号"         varchar(20)          not null,
   乘客联系方式               varchar(20)          not null,
   constraint PK_订票 primary key (机票编号)
)
create table 飞机登记 (
   飞机编号                 varchar(10)          not null,
   机型                   varchar(50)          not null,
   注册日期                 smalldatetime        not null,
   使用年限                 tinyint              not null,
   其他信息                 text                 null,
   constraint PK_飞机登记 primary key (飞机编号)
)
create table 飞机表 (
   机型                   varchar(50)          not null,
   商务舱数量                smallint             null,
   头等舱数量                smallint             null,
   经济舱数量                smallint             null,
   载重量                  real                 not null,
   最大里程                 real                 not null,
   constraint PK_飞机表 primary key (机型)
)
create table 飞行计划安排 (
   航程号                  int                  identity,
   航班编号                 varchar(10)          not null,
   计划出发时间               datetime             not null,
   计划到达经停机场时间           datetime             null,
   计划从经停机场出发时间          datetime             null,
   计划到达时间               datetime             not null,
   "经济舱（开始-到达）剩余座位"     smallint             null,
   "商务舱（开始-到达）剩余座位"     smallint             null,
   "头等舱（开始-到达）剩余座位"     smallint             null,
   "经济舱（经停-到达）剩余座位"     smallint             null,
   "商务舱（经停-到达）剩余座位"     smallint             null,
   "头等舱（经停-到达）剩余座位"     smallint             null,
   "经济舱（开始-经停）剩余座位"     smallint             null,
   "商务舱（开始-经停）剩余座位"     smallint             null,
   "头等舱（开始-经停）剩余座位"     smallint             null,
   "票价（开始-到达，经济舱）"      money                null,
   "票价（开始-经停，经济舱）"      money                null,
   "票价（经停-到达，经济舱）"      money                null,
   "票价（开始-到达，商务舱）"      money                null,
   "票价（开始-经停，商务舱）"      money                null,
   "票价（经停-到达，商务舱）"      money                null,
   "票价（开始-到达，头等舱）"      money                null,
   "票价（开始-经停，头等舱）"      money                null,
   "票价（经停-到达，头等舱）"      money                null,
   constraint PK_飞行计划安排 primary key (航程号)
)
alter table 航班
   add constraint FK_航班_FK_飞机编号_飞机登记 foreign key (飞机编号)
      references 飞机登记 (飞机编号)
alter table 航班
   add constraint FK_航班_机场代码_出发_机场 foreign key (出发机场代码)
      references 机场 (机场代码)
alter table 航班
   add constraint FK_航班_机场代码_到达_机场 foreign key (到达机场代码)
      references 机场 (机场代码)
alter table 航班
   add constraint FK_航班_机场代码_经停_机场 foreign key (经停机场代码)
      references 机场 (机场代码)
alter table 订票
   add constraint FK_订票_用户名_用户表 foreign key (用户名)
      references 用户表 (用户名)
alter table 订票
   add constraint FK_订票_航程号_飞行计划安排 foreign key (航程号)
      references 飞行计划安排 (航程号)
alter table 飞机登记
   add constraint FK_飞机登记_机型_飞机表 foreign key (机型)
      references 飞机表 (机型)
alter table 飞行计划安排
   add constraint FK_飞行计划安排_航班编号_航程_航班 foreign key (航班编号)
      references 航班 (航班编号)
INSERT INTO 机场(机场代码,机场名,所在城市)
VALUES
('01','首都机场','北京'),
('02','双流机场','成都'),
('03','高崎机场','香港'),
('04','太平机场','哈尔滨'),
('05','江北机场','海南'),
('06','虹桥机场','上海'),
('07','龙嘉机场','长春'),
('08','中川机场','兰州'),
('09','白云机场','广州'),
('10','黄沙机场','长沙'),
('11','昌北机场','南昌'),
('12','南苑机场','北京')
INSERT INTO 用户表(用户名
      ,用户密码
      ,用户权限
      ,用户联系方式)
VALUES
('复旦大学','310226199',0,'1321231278'),
('上海市文化街','31022612873',0,'18888888888'),
('郑州绿博园','zzlby2010',0,'13543276895'),
('余夏','1274111',0,'18917260800'),
('地平线~','dpx123321',0,'1891739856'),
('铁柱','1274111',0,'18917260800'), 
('乌托邦','seiclhiqcaa',0,'13876392037'),
('aa','asdfghjkl',0,'18217461800'),
('机场管理员a','kseh23Gke9',1,'13972654267'),
('机场管理员b','AShs195ose',1,'13232604267'),
('管理员a','123456',1,'13972397267')	        
INSERT INTO 飞机表
VALUES
('空客319',0,8,120,68,7200),
('空客321',12,0,173,83,5600),
('空客330',20,16,255,230,7400),
('波音747',42,8,261,148,13890),
('波音777',54,15,299,178,12400)
INSERT INTO 飞机登记
VALUES
('001','空客319',2015-08-01,5,null),
('002','空客319',2015-08-01,5,null),
('003','空客319',2015-08-01,5,null),
('004','空客321',2016-09-01,4,null),
('005','空客321',2016-09-01,4,null),
('006','空客321',2016-09-01,4,null),
('007','空客330',2017-10-22,3,null),
('008','空客330',2017-10-22,3,null),
('009','空客330',2017-10-22,3,null),
('010','波音777',2014-01-01,6,null),
('011','波音777',2014-01-01,6,null),
('012','波音777',2014-01-01,6,null),
('013','波音747',2018-01-01,2,null),
('014','波音747' ,2018-01-01,2,null),
('015','波音747',2018-01-01,2,null)
INSERT INTO 航班(航班编号,出发机场代码,经停机场代码,到达机场代码,飞机编号)
VALUES
('0001','01',null,'02','001'),
('0002','01',null,'03','002'),
('0003','05','12','06','004'),     
('0004','08',null,'09','005'),
('0005','08','12','10','007'),
('0006','12',null,'11','008'),
('0007','01',null,'02','009'),
('0008','01',null,'12','010'),
('0009','01',null,'11','011')
INSERT INTO 飞行计划安排(航班编号,计划出发时间,计划到达经停机场时间,计划从经停机场出发时间,计划到达时间,[经济舱（开始-到达）剩余座位],[商务舱（开始-到达）剩余座位],[头等舱（开始-到达）剩余座位],[经济舱（经停-到达）剩余座位],[商务舱（经停-到达）剩余座位],[头等舱（经停-到达）剩余座位],[经济舱（开始-经停）剩余座位],[商务舱（开始-经停）剩余座位],[头等舱（开始-经停）剩余座位],[票价（开始-到达，经济舱）],[票价（开始-经停，经济舱）],[票价（经停-到达，经济舱）],[票价（开始-到达，商务舱）],[票价（开始-经停，商务舱）],[票价（经停-到达，商务舱）],[票价（开始-到达，头等舱）],[票价（开始-经停，头等舱）],[票价（经停-到达，头等舱）])
VALUES
('0001','2019-01-01 08:00:00',null,null,'2019-01-01 10:30:00',118,0,8,null,null,null,null,null,null,500,null,null,800,null,null,1100,null,null),
('0001','2019-01-03 08:00:00',null,null,'2019-01-01 10:30:00',120,0,8,null,null,null,null,null,null,500,null,null,800,null,null,1100,null,null),
('0001','2019-01-05 08:00:00',null,null,'2019-01-01 10:30:00',120,0,8,null,null,null,null,null,null,500,null,null,800,null,null,1100,null,null),
('0002','2019-01-02 13:00:00',null,null,'2019-01-02 16:30:00',118,0,8,null,null,null,null,null,null,500,null,null,800,null,null,1100,null,null),
('0002','2019-01-06 13:00:00',null,null,'2019-01-06 16:30:00',120,0,7,null,null,null,null,null,null,500,null,null,800,null,null,1100,null,null),
('0003','2019-01-01 10:00:00','2019-01-01 12:00:00','2019-01-01 13:00:00','2019-01-01 14:30:00',172,12,0,171,12,0,172,12,0,500,300,200,800,600,500,1100,900,800),
('0003','2019-01-04 10:00:00','2019-01-04 12:00:00','2019-01-04 13:00:00','2019-01-04 14:30:00',173,12,0,173,12,0,173,12,0,500,300,200,800,600,500,1100,900,800),
('0003','2019-01-07 10:00:00','2019-01-07 12:00:00','2019-01-07 13:00:00','2019-01-07 14:30:00',173,12,0,173,12,0,173,12,0,500,300,200,800,600,500,1100,900,800),
('0004','2019-01-05 17:00:00',null,null,'2019-01-05 20:30:00',255,20,16,null,null,null,null,null,null,670,null,null,970,null,null,1270,null,null),
('0005','2019-01-01 15:00:00','2019-01-01 17:00:00','2019-01-01 18:00:00','2019-01-01 20:30:00',260,41,8,260,42,8,260,41,8,600,300,300,900,450,450,1200,600,600),
('0005','2019-01-04 15:00:00','2019-01-04 17:00:00','2019-01-04 18:00:00','2019-01-04 20:30:00',261,42,8,261,42,8,261,42,8,600,300,300,900,450,450,1200,600,600),
('0005','2019-01-07 15:00:00','2019-01-07 17:00:00','2019-01-07 18:00:00','2019-01-07 20:30:00',261,42,8,261,42,8,261,42,8,600,300,300,900,450,450,1200,600,600),
('0006','2019-01-02 08:00:00',null,null,'2019-01-02 13:30:00',255,20,16,null,null,null,null,null,null,670,null,null,1100,null,null,1570,null,null),
('0006','2019-01-06 08:00:00',null,null,'2019-01-06 13:30:00',255,20,16,null,null,null,null,null,null,670,null,null,1100,null,null,1570,null,null),
('0007','2019-01-03 09:30:00',null,null,'2019-01-03 13:00:00',299,54,15,null,null,null,null,null,null,670,null,null,970,null,null,1270,null,null),
('0008','2019-01-04 08:30:00',null,null,'2019-01-04 10:30:00',299,54,14,null,null,null,null,null,null,400,null,null,700,null,null,1000,null,null),
('0009','2019-01-06 11:30:00',null,null,'2019-01-03 15:00:00',297,54,15,null,null,null,null,null,null,570,null,null,870,null,null,1170,null,null)
INSERT INTO 订票
VALUES
(1,'首都机场','双流机场','001','经济舱','余夏','李铁柱','男','老人','411002196402122371','13837439823'),
(1,'首都机场','双流机场','002','经济舱','地平线~','张三','男','残疾','411001199902122391','13837434523'),
(4,'首都机场','高崎机场','001','经济舱','余夏','李可可','女','小孩','311002201402122381','13823879823'),
(4,'首都机场','高崎机场','002','经济舱','余夏','李见','男','病人','311002197302122311','13823879823'),
(5,'首都机场','高崎机场','001','商务舱','余夏','朱欣','女','成人','311002197603132481','13928376273'),
(6,'太平机场','江北机场','001','经济舱','铁柱','李四','男','小孩','411001201702122371','13829386483'),
(6,'太平机场','黄沙机场','002','经济舱','铁柱','张光北','男','成人','321001198603022371','13922946483'),
(10,'虹桥机场','江北机场','001','经济舱','复旦大学','张武','男','病人','411001198412212371','15723126483'),
(10,'江北机场','中川机场','002','商务舱','复旦大学','李四','男','成人','411001198809212331','15629386483'),
(16,'首都机场','黄沙机场','001','头等舱','aa','温蒂','女','成人','312001199302122362','15702986483'),
(17,'首都机场','昌北机场','001','经济舱','郑州绿博园','王文倩','女','老人','411001196802222381','17827362817'),
(17,'首都机场','昌北机场','002','经济舱','上海市文化街','贺天成','男','成人','332001199409122372','13892836483')
'''
cursor.execute(sql)
cursor.commit()
sql = '''CREATE PROC copy_table  @flight_no int
AS
SELECT * INTO 隐私查询 FROM 订票 WHERE 航程号 = @flight_no
ALTER TABLE 隐私查询 ADD mid int
EXEC('UPDATE 隐私查询 SET mid = 机票编号')
ALTER TABLE 隐私查询 DROP COLUMN 机票编号
exec sp_rename '隐私查询.mid','机票编号'
ALTER TABLE 隐私查询 ADD 序号 int IDENTITY(1,1)'''
cursor.execute(sql)
cursor.commit()
sql = '''CREATE PROC pd_search
AS
DECLARE @sum float, @sensitivity float,@budget float,@row_num int,@rand_num float,@i int,@tic_num int,@class1 float,@class2 float,@class3 float,@class4 float,@class5 float,@class6 float
SET @sensitivity = 1
SET @budget = 0.1
SET @i = 0
SET @sum = 0
SELECT @row_num =COUNT(*) FROM 隐私查询

SELECT @class1 =COUNT(*) FROM 隐私查询 WHERE 乘客类别 = '病人'
SET @class1 = 0.5 * @class1 * @budget/ @sensitivity 
SET @class1 = POWER(2.71828,@class1)
SELECT @class2 =COUNT(*) FROM 隐私查询 WHERE 乘客类别 = '残疾'
SET @class2 = 0.5 * @class2 * @budget/ @sensitivity 
SET @class2 = POWER(2.71828,@class2)
SELECT @class3 =COUNT(*) FROM 隐私查询 WHERE 乘客类别 = '成人'
SET @class3 = 0.5 * @class3 * @budget/ @sensitivity 
SET @class3 = POWER(2.71828,@class3)
SELECT @class4 =COUNT(*) FROM 隐私查询 WHERE 乘客类别 = '孕妇'
SET @class4 = 0.5 * @class4 * @budget/ @sensitivity 
SET @class4 = POWER(2.71828,@class4)
SELECT @class5 =COUNT(*) FROM 隐私查询 WHERE 乘客类别 = '小孩'
SET @class5 = 0.5 * @class5 * @budget/ @sensitivity 
SET @class5 = POWER(2.71828,@class5)
SELECT @class6 =COUNT(*) FROM 隐私查询 WHERE 乘客类别 = '老人'
SET @class6 = 0.5 * @class6 * @budget/ @sensitivity 
SET @class6 = POWER(2.71828,@class6)


SET @sum = @class1 + @class2 + @class3 + @class4 + @class5 + @class6
SET @class1 = @class1/@sum
SET @class2 = @class2/@sum
SET @class3 = @class3/@sum
SET @class4 = @class4/@sum
SET @class5 = @class5/@sum
SET @class6 = @class6/@sum


SELECT TOP 1 @tic_num = 机票编号 from 隐私查询 

WHILE @i < @row_num BEGIN
	SELECT @rand_num = RAND()
	SET @sum = 0
	SET @sum = @sum + @class1
	IF @rand_num < @sum BEGIN
		UPDATE 隐私查询 SET 乘客类别 = '病人' WHERE 机票编号 = @tic_num + @i
		SET @i = @i + 1
		CONTINUE END
	SET @sum = @sum + @class2
	IF @rand_num < @sum 
	BEGIN
		UPDATE 隐私查询 SET 乘客类别 = '残疾' WHERE 机票编号 = @tic_num + @i
		SET @i = @i + 1
		CONTINUE
	END
	SET @sum = @sum + @class3
	IF @rand_num < @sum 
	BEGIN
		UPDATE 隐私查询 SET 乘客类别 = '成人' WHERE 机票编号 = @tic_num + @i
		SET @i = @i + 1
		CONTINUE
	END
	SET @sum = @sum + @class4
	IF @rand_num < @sum 
	BEGIN
		UPDATE 隐私查询 SET 乘客类别 = '孕妇' WHERE 机票编号 = @tic_num + @i
		SET @i = @i + 1
		CONTINUE
	END
	SET @sum = @sum + @class5
	IF @rand_num < @sum 
	BEGIN
		UPDATE 隐私查询 SET 乘客类别 = '小孩' WHERE 机票编号 = @tic_num + @i
		SET @i = @i + 1
		CONTINUE
	END
	SET @sum = @sum + @class6
	IF @rand_num < @sum 
	BEGIN
		UPDATE 隐私查询 SET 乘客类别 = '老人' WHERE 机票编号 = @tic_num + @i
		SET @i = @i + 1
		CONTINUE
	END
	
END'''
cursor.execute(sql)
cursor.commit()
sql = '''INSERT INTO 订票
VALUES
(1,'首都机场','黄沙机场','021','经济舱','余夏','test1','男','老人','4135402196402122371','13837439823'),
(1,'首都机场','双流机场','022','经济舱','地平线~','test2','男','残疾','423001199902122391','13837434523'),
(6,'南苑机场','虹桥机场','011','经济舱','余夏','test3','女','小孩','311002201402122321','13823879823'),
(7,'南苑机场','虹桥机场','012','经济舱','余夏','test4','男','病人','311002197302122361','13823879823'),
(5,'首都机场','高崎机场','011','商务舱','余夏','test5','女','成人','311002197603132491','13928376273')
if exists (select table_name from INFORMATION_SCHEMA.VIEWS where TABLE_NAME = '用户购票信息')
	drop view 用户购票信息
if exists (select table_name from INFORMATION_SCHEMA.VIEWS where TABLE_NAME = '出发经停')
	drop view 出发经停
if exists (select table_name from INFORMATION_SCHEMA.VIEWS where TABLE_NAME = '经停到达')
	drop view 经停到达
if exists (select table_name from INFORMATION_SCHEMA.VIEWS where TABLE_NAME = '出发到达')
	drop view 出发到达
if exists (select table_name from INFORMATION_SCHEMA.VIEWS where TABLE_NAME = '订票表与飞行计划整合')
	drop view 订票表与飞行计划整合
'''
cursor.execute(sql)
cursor.commit()
sql = '''
Create view 出发经停
AS
select a.航班编号,a.出发机场 AS 出发地,c.经停机场 AS 目的地 from (select b1.航班编号 , b2.机场名 AS 出发机场  from 航班  b1 inner join 机场 b2 on b1.出发机场代码 = b2.机场代码) a
   inner join (select b1.航班编号 , b2.机场名 AS 经停机场  from 航班  b1 inner join 机场 b2 on b1.经停机场代码 = b2.机场代码) c
on a.航班编号 = c.航班编号
'''
cursor.execute(sql)
cursor.commit()

sql = '''Create view 经停到达
AS
select a.航班编号,a.经停机场 AS 出发地 ,c.终到机场 AS 目的地 from (select b1.航班编号 , b2.机场名 AS 经停机场  from 航班  b1 inner join 机场 b2 on b1.经停机场代码 = b2.机场代码) a
   inner join (select b1.航班编号 , b2.机场名 AS 终到机场  from 航班  b1 inner join 机场 b2 on b1.到达机场代码 = b2.机场代码) c
on a.航班编号 = c.航班编号'''
cursor.execute(sql)
cursor.commit()

sql = '''Create view 出发到达
AS
select a.航班编号,a.出发机场 AS 出发地,c.终到机场 AS 目的地 from (select b1.航班编号 , b2.机场名 AS 出发机场  from 航班  b1 inner join 机场 b2 on b1.出发机场代码 = b2.机场代码) a
   inner join (select b1.航班编号 , b2.机场名 AS 终到机场  from 航班  b1 inner join 机场 b2 on b1.到达机场代码 = b2.机场代码) c
on a.航班编号 = c.航班编号'''
cursor.execute(sql)
cursor.commit()

sql = '''create view 订票表与飞行计划整合
As
select a.航班编号,a.计划出发时间,a.计划从经停机场出发时间,a.计划到达经停机场时间,a.计划到达时间,a.[票价（开始-到达，商务舱）], a.[票价（开始-到达，头等舱）],a.[票价（开始-到达，经济舱）],
a.[票价（开始-经停，商务舱）],a.[票价（开始-经停，头等舱）],a.[票价（开始-经停，经济舱）],a.[票价（经停-到达，商务舱）],a.[票价（经停-到达，头等舱）],a.[票价（经停-到达，经济舱）],b.*
  from 飞行计划安排 a inner join 订票 b  ON a.航程号=b.航程号'''
cursor.execute(sql)
cursor.commit()

sql = '''create view 用户购票信息
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
	ON a1.航班编号 = a2.航班编号  where a1.目的机场 = a2.目的地 and  a1.出发机场 = a2.出发地 and a1.舱位 = '经济舱')'''
cursor.execute(sql)
cursor.commit()

sql = '''CREATE TRIGGER tr_flight
ON 飞行计划安排 AFTER INSERT
AS
DECLARE @flight_no varchar(50), @flight_type varchar(50), @plane_num varchar(50), @fly_no int
DECLARE @first_num int, @business_num int, @economy_num int
set @fly_no = (SELECT 航程号 from inserted)
set @flight_no = (SELECT 航班编号 from inserted)
set @plane_num = (SELECT 飞机编号 FROM 航班 WHERE 航班编号 = @flight_no)
set @flight_type = (SELECT 机型 FROM 飞机登记 where 飞机编号 = @plane_num )
set @first_num = (SELECT 头等舱数量 FROM 飞机表 WHERE 机型 = @flight_type)
set @business_num = (SELECT 商务舱数量 FROM 飞机表 WHERE 机型 = @flight_type)
set @economy_num = (SELECT 经济舱数量 FROM 飞机表 WHERE 机型 = @flight_type)
IF @economy_num = 0
SET @economy_num = null
IF @business_num = 0
SET @business_num = null
IF @first_num = 0
SET @first_num = null
update 飞行计划安排
set [商务舱（开始-到达）剩余座位] = @business_num, [商务舱（开始-经停）剩余座位] =@business_num, [商务舱（经停-到达）剩余座位] = @business_num,
[经济舱（开始-到达）剩余座位] = @economy_num, [经济舱（开始-经停）剩余座位]  = @economy_num, [经济舱（经停-到达）剩余座位]  = @economy_num,
[头等舱（开始-到达）剩余座位]  = @first_num,[头等舱（开始-经停）剩余座位]   = @first_num,[头等舱（经停-到达）剩余座位]   = @first_num
where 航程号 = @fly_no
'''
cursor.execute(sql)
cursor.commit()

sql = '''CREATE trigger tr_refund_ticket
ON 订票 AFTER DELETE
AS
Declare @seat varchar(20), @flight1 varchar(20) ,@flight2 varchar(20),@begin varchar(20), @terminal varchar(20) --flight1 航程号 flight2 航班号 /出发、到达机场
select @flight1 = 航程号,@seat = 舱位, @begin = 出发机场, @terminal = 目的机场  from deleted
select @flight2 = 航班编号 from 飞行计划安排 where 航程号 = @flight1

IF exists (select * from 出发经停 where 出发地 = @begin and 目的地 = @terminal and 航班编号 = @flight2)
BEGIN
	IF @seat = '商务舱'
		Update 飞行计划安排
			set [商务舱（开始-经停）剩余座位] = [商务舱（开始-经停）剩余座位] + 1  where 航程号 = @flight1
	ELSE IF @seat = '头等舱'
		Update 飞行计划安排
			set [头等舱（开始-经停）剩余座位] = [头等舱（开始-经停）剩余座位] + 1  where 航程号 = @flight1
	ELSE
	Update 飞行计划安排
			set [经济舱（开始-经停）剩余座位] = [经济舱（开始-经停）剩余座位] + 1  where 航程号 = @flight1
END
IF exists (select * from 经停到达 where 出发地 = @begin and 目的地 = @terminal and 航班编号 = @flight2)
BEGIN
	IF @seat = '商务舱'
		Update 飞行计划安排
			set [商务舱（经停-到达）剩余座位] = [商务舱（经停-到达）剩余座位] + 1  where 航程号 = @flight1
	ELSE IF @seat = '头等舱'
		Update 飞行计划安排
			set [头等舱（经停-到达）剩余座位] = [头等舱（经停-到达）剩余座位] + 1  where 航程号 = @flight1
	ELSE
	Update 飞行计划安排
			set [经济舱（经停-到达）剩余座位] = [经济舱（经停-到达）剩余座位] + 1  where 航程号 = @flight1
END
IF exists (select * from 出发到达 where 出发地 = @begin and 目的地 = @terminal and 航班编号 = @flight2)
BEGIN
	IF @seat = '商务舱'
	begin
		Update 飞行计划安排
			set [商务舱（开始-到达）剩余座位] = [商务舱（开始-到达）剩余座位] + 1  where 航程号 = @flight1
		UPdate 飞行计划安排
			set [商务舱（开始-经停）剩余座位] = [商务舱（开始-经停）剩余座位] + 1  where 航程号 = @flight1 and [商务舱（开始-经停）剩余座位] is not NULL
		Update 飞行计划安排
			set [商务舱（经停-到达）剩余座位] = [商务舱（经停-到达）剩余座位] + 1  where 航程号 = @flight1 and [商务舱（经停-到达）剩余座位] is not NULL
	end
	IF @seat = '头等舱'
	BEGIN
		Update 飞行计划安排
			set [头等舱（开始-到达）剩余座位] = [头等舱（开始-到达）剩余座位] + 1  where 航程号 = @flight1
		Update 飞行计划安排
			set [头等舱（开始-经停）剩余座位] = [头等舱（开始-经停）剩余座位] + 1  where 航程号 = @flight1 and [头等舱（开始-经停）剩余座位] is not NULL
		Update 飞行计划安排
			set [头等舱（经停-到达）剩余座位] = [头等舱（经停-到达）剩余座位] + 1  where 航程号 = @flight1 and [头等舱（经停-到达）剩余座位] is not NULL
	END
	IF @seat = '经济舱'
	BEGIN
	Update 飞行计划安排
			set [经济舱（开始-到达）剩余座位] = [经济舱（开始-到达）剩余座位] + 1  where 航程号 = @flight1
	Update 飞行计划安排
			set [经济舱（开始-经停）剩余座位] = [经济舱（开始-经停）剩余座位] + 1  where 航程号 = @flight1 and [经济舱（开始-经停）剩余座位] is not NULL
	Update 飞行计划安排
			set [经济舱（经停-到达）剩余座位] = [经济舱（经停-到达）剩余座位] + 1  where 航程号 = @flight1 and [经济舱（经停-到达）剩余座位] is not NULL
	END
END'''
cursor.execute(sql)
cursor.commit()
conn.close()


