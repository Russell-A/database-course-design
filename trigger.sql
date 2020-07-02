USE air
GO
CREATE TRIGGER tr_flight
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