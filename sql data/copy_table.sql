USE air
GO

CREATE PROC copy_table  @flight_no int
AS
SELECT * INTO 隐私查询 FROM 订票 WHERE 航程号 = @flight_no
ALTER TABLE 隐私查询 ADD mid int
EXEC('UPDATE 隐私查询 SET mid = 机票编号')
ALTER TABLE 隐私查询 DROP COLUMN 机票编号
exec sp_rename '隐私查询.mid','机票编号'
ALTER TABLE 隐私查询 ADD 序号 int IDENTITY(1,1)
