use air
create table 进程数 (
航程号 int not null,
数量 int default 0,
foreign key(航程号) references 飞行计划安排(航程号) on delete cascade on update cascade
)
go
insert into 进程数(航程号) select 航程号 from 飞行计划安排
go