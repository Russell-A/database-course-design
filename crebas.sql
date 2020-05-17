/*==============================================================*/
/* DBMS name:      Microsoft SQL Server 2008                    */
/* Created on:     2020/05/17 22:03:27                          */
/*==============================================================*/


if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('航班') and o.name = 'FK_航班_机场代码(出发)_机场')
alter table 航班
   drop constraint "FK_航班_机场代码(出发)_机场"
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('航班') and o.name = 'FK_航班_机场代码(到达)_机场')
alter table 航班
   drop constraint "FK_航班_机场代码(到达)_机场"
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('航班') and o.name = 'FK_航班_机场代码(经停)_机场')
alter table 航班
   drop constraint "FK_航班_机场代码(经停)_机场"
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('订票') and o.name = 'FK_订票_用户名_用户表')
alter table 订票
   drop constraint FK_订票_用户名_用户表
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('订票') and o.name = 'FK_订票_航程号_飞行计划安排')
alter table 订票
   drop constraint FK_订票_航程号_飞行计划安排
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('飞机登记') and o.name = 'FK_飞机登记_机型_飞机表')
alter table 飞机登记
   drop constraint FK_飞机登记_机型_飞机表
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('飞机航班') and o.name = 'FK_飞机航班_航班编号(飞机)_航班')
alter table 飞机航班
   drop constraint "FK_飞机航班_航班编号(飞机)_航班"
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('飞机航班') and o.name = 'FK_飞机航班_飞机编号_飞机登记')
alter table 飞机航班
   drop constraint FK_飞机航班_飞机编号_飞机登记
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('飞行计划安排') and o.name = 'FK_飞行计划安排_航班编号(航程)_航班')
alter table 飞行计划安排
   drop constraint "FK_飞行计划安排_航班编号(航程)_航班"
go

if exists (select 1
            from  sysobjects
           where  id = object_id('机场')
            and   type = 'U')
   drop table 机场
go

if exists (select 1
            from  sysobjects
           where  id = object_id('用户表')
            and   type = 'U')
   drop table 用户表
go

if exists (select 1
            from  sysobjects
           where  id = object_id('航班')
            and   type = 'U')
   drop table 航班
go

if exists (select 1
            from  sysobjects
           where  id = object_id('订票')
            and   type = 'U')
   drop table 订票
go

if exists (select 1
            from  sysobjects
           where  id = object_id('飞机登记')
            and   type = 'U')
   drop table 飞机登记
go

if exists (select 1
            from  sysobjects
           where  id = object_id('飞机航班')
            and   type = 'U')
   drop table 飞机航班
go

if exists (select 1
            from  sysobjects
           where  id = object_id('飞机表')
            and   type = 'U')
   drop table 飞机表
go

if exists (select 1
            from  sysobjects
           where  id = object_id('飞行计划安排')
            and   type = 'U')
   drop table 飞行计划安排
go

/*==============================================================*/
/* Table: 机场                                                    */
/*==============================================================*/
create table 机场 (
   机场代码                 varchar(20)          not null,
   机场名                  varchar(50)          not null,
   所在城市                 varchar(20)          not null,
   constraint PK_机场 primary key (机场代码)
)
go

/*==============================================================*/
/* Table: 用户表                                                   */
/*==============================================================*/
create table 用户表 (
   用户名                  varchar(20)          not null,
   用户密码                 varchar(20)          not null,
   用户权限                 int                  not null,
   用户联系方式               varchar(20)          not null,
   constraint PK_用户表 primary key (用户名)
)
go

/*==============================================================*/
/* Table: 航班                                                    */
/*==============================================================*/
create table 航班 (
   航班编号                 varchar(10)          not null,
   出发机场代码               varchar(20)          not null,
   经停机场代码               varchar(20)          null,
   到达机场代码               varchar(20)          not null,
   constraint PK_航班 primary key (航班编号)
)
go

/*==============================================================*/
/* Table: 订票                                                    */
/*==============================================================*/
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
go

/*==============================================================*/
/* Table: 飞机登记                                                  */
/*==============================================================*/
create table 飞机登记 (
   飞机编号                 varchar(10)          not null,
   机型                   varchar(50)          not null,
   注册日期                 smalldatetime        not null,
   使用年限                 tinyint              not null,
   其他信息                 text                 null,
   constraint PK_飞机登记 primary key (飞机编号)
)
go

/*==============================================================*/
/* Table: 飞机航班                                                  */
/*==============================================================*/
create table 飞机航班 (
   航班编号                 varchar(10)          not null,
   飞机编号                 varchar(10)          not null,
   constraint PK_飞机航班 primary key (航班编号, 飞机编号)
)
go

/*==============================================================*/
/* Table: 飞机表                                                   */
/*==============================================================*/
create table 飞机表 (
   机型                   varchar(50)          not null,
   商务舱数量                smallint             null,
   头等舱数量                smallint             null,
   经济舱数量                smallint             null,
   载重量                  real                 not null,
   最大里程                 real                 not null,
   constraint PK_飞机表 primary key (机型)
)
go

/*==============================================================*/
/* Table: 飞行计划安排                                                */
/*==============================================================*/
create table 飞行计划安排 (
   航程号                  int                  identity,
   航班编号                 varchar(10)          not null,
   计划出发时间               datetime             not null,
   计划到达经停机场时间           datetime             null,
   计划从经停机场出发时间          datetime             null,
   计划到达时间               datetime             not null,
   "经济舱（开始-到达）剩余座位"     smallint             not null,
   "商务舱（开始-到达） 剩余座位"    smallint             not null,
   "头等舱（开始-到达） 剩余座位"    smallint             not null,
   "经济舱（经停-到达）剩余座位"     smallint             null,
   "商务舱（经停-到达） 剩余座位"    smallint             null,
   "头等舱（经停-到达） 剩余座位"    smallint             null,
   "经济舱（开始-经停）剩余座位"     smallint             null,
   "商务舱（开始-经停） 剩余座位"    smallint             null,
   "头等舱（开始-经停） 剩余座位"    smallint             not null,
   "票价（开始-到达，经济舱）"      money                null,
   "票价（开始-经停，经济舱）"      money                null,
   "票价（经停-到达，经济舱）"      money                null,
   "票价（开始-到达，商务舱）"      money                not null,
   "票价（开始-经停，商务舱）"      money                null,
   "票价（经停-到达，商务舱）"      money                null,
   "票价（开始-到达，头等舱）"      money                not null,
   "票价（开始-经停，头等舱）"      money                null,
   "票价（经停-到达，头等舱）"      money                null,
   constraint PK_飞行计划安排 primary key (航程号)
)
go

alter table 航班
   add constraint "FK_航班_机场代码(出发)_机场" foreign key (出发机场代码)
      references 机场 (机场代码)
go

alter table 航班
   add constraint "FK_航班_机场代码(到达)_机场" foreign key (到达机场代码)
      references 机场 (机场代码)
go

alter table 航班
   add constraint "FK_航班_机场代码(经停)_机场" foreign key (经停机场代码)
      references 机场 (机场代码)
go

alter table 订票
   add constraint FK_订票_用户名_用户表 foreign key (用户名)
      references 用户表 (用户名)
go

alter table 订票
   add constraint FK_订票_航程号_飞行计划安排 foreign key (航程号)
      references 飞行计划安排 (航程号)
go

alter table 飞机登记
   add constraint FK_飞机登记_机型_飞机表 foreign key (机型)
      references 飞机表 (机型)
go

alter table 飞机航班
   add constraint "FK_飞机航班_航班编号(飞机)_航班" foreign key (航班编号)
      references 航班 (航班编号)
go

alter table 飞机航班
   add constraint FK_飞机航班_飞机编号_飞机登记 foreign key (飞机编号)
      references 飞机登记 (飞机编号)
go

alter table 飞行计划安排
   add constraint "FK_飞行计划安排_航班编号(航程)_航班" foreign key (航班编号)
      references 航班 (航班编号)
go

