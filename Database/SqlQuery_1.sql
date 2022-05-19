create database WS

create table Traffic_light(
ID_light int primary key,
Car_count_full_run int  not null check(Car_count_full_run >=0),
Car_average_in_minute int not null check(Car_average_in_minute >=0),
Count_color_switches int not null check(Count_color_switches >=0)
);

create table Cars_stats(
Car_id int primary key,
Car_spawn_ticks int not null check(Car_spawn_ticks >=0),
Car_exit_ticks int not null check(Car_exit_ticks >=0)
);

select * from Traffic_light