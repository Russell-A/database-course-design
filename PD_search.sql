USE air
GO
CREATE PROC pd_search
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
	
END