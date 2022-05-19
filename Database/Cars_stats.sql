CREATE TABLE [dbo].[Cars_stats]
(
	Car_id int primary key,
	Car_spawn_ticks int not null check(Car_spawn_ticks >=0),
	Car_exit_ticks int not null check(Car_exit_ticks >=0)
)
