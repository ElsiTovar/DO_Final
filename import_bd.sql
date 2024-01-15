use kaggle
go

if not exists (select * from sys.tables where object_id=object_id(N'dbo.starbucks'))

create table dbo.Starbucks(
				baverage_category varchar(50),
				baverage varchar(100),
				baverage_prep varchar(50),
				calories decimal(6,3),
				total_fat_g varchar(10),
				trans_fat_g decimal(6,3),
				saturated_fat_g decimal(6,3),
				sodium_mg decimal(6,3),
				total_carbohydrates_g decimal(6,3),
				cholesterol_mg decimal(6,3),
				dietary_fibre_g decimal(6,3),
				sugar_g decimal(6,3),
				protein_g decimal(6,3),
				vitamin_a_pct varchar(10),
				vitamin_c_pct varchar(10),
				calcium_pct varchar(10),
				iron_pct varchar(10),
				cafeine_mg varchar(10)
)
go

truncate table dbo.starbucks
go

bulk insert dbo.starbucks
from 'C:\Proyecto01\dataset\starbucks.csv'
with
(
	firstrow =2,
	fieldterminator=',',
	rowterminator ='0x0a'
	)

go


