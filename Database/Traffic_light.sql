CREATE TABLE [dbo].[Traffic_light]
(
	ID_light INT NOT NULL PRIMARY KEY,
	Car_count_full_run int  not null check(Car_count_full_run >=0),
	Car_average_in_minute int not null check(Car_average_in_minute >=0),
	Count_color_switches int not null check(Count_color_switches >=0)
)
