update subtasks set title = 'Meditation & Stretching' where id = 39


--weekend/evenings

update taskcategory set weight = 5 where id = 20;  -- saas
update taskcategory set weight = 0 where id = 15 ; -- aws
update taskcategory set weight = 5 where id = 14 ;-- coding
update taskcategory set weight = 20 where id = 16 ; -- leisure
update taskcategory set weight = 15 where id = 19 ; -- art
update taskcategory set weight = 10 where id = 17; -- housework
update taskcategory set weight = 10 where id = 12 ; -- chess
update taskcategory set weight = 15 where id = 13; -- blender
update taskcategory set weight = 5 where id = 21; -- health
update taskcategory set weight = 5 where id = 18; -- spanish
update taskcategory set weight = 2 where id = 2; -- cooking
update taskcategory set weight = 0 where id = 4; --work

select * from taskcategory


--daytime/cherry
update taskcategory set weight = 15 where id = 20; -- #saas
update taskcategory set weight = 30 where id = 15; -- #aws
update taskcategory set weight = 10 where id = 14;  --#coding
update taskcategory set weight = 0 where id = 16;  --#leisure
update taskcategory set weight = 0 where id = 19; -- #art
update taskcategory set weight = 0 where id = 17; -- housework
update taskcategory set weight = 3 where id = 12 ; -- chess
update taskcategory set weight = 5 where id = 13; -- blender
update taskcategory set weight = 2 where id = 21; -- health
update taskcategory set weight = 0 where id = 18; -- spanish
update taskcategory set weight = 0 where id = 2; -- cooking
update taskcategory set weight = 5 where id = 4; --work
select * from taskcategory

--homeworking
update taskcategory set weight = 30 where id = 20; -- #saas
update taskcategory set weight = 35 where id = 15; -- #aws
update taskcategory set weight = 10 where id = 14;  --#coding
update taskcategory set weight = 4 where id = 16;  --#leisure
update taskcategory set weight = 4 where id = 19; -- #art
update taskcategory set weight = 5 where id = 17; -- housework
update taskcategory set weight = 5 where id = 12 ; -- chess
update taskcategory set weight = 5 where id = 13; -- blender
update taskcategory set weight = 4 where id = 21; -- health
update taskcategory set weight = 2 where id = 18; -- spanish
update taskcategory set weight = 0 where id = 2; -- cooking
update taskcategory set weight = 5 where id = 4; --work
select * from taskcategory


delete from taskcategory where id = 3



update subtasks set title = 'Exercism Python' where id = 37;

update subtasks set weight = 10 where id = 22 ; -- puzz
update subtasks set weight = 10 where id = 32 ; -- port
update subtasks set weight = 10 where id = 28 ; -- tute 
update subtasks set weight = 10 where id = 34 ; -- water
update subtasks set weight = 15 where id = 30 ; -- game
update subtasks set weight = 15 where id = 26 ; -- model
update subtasks set weight = 5 where id = 41; -- python docs
update subtasks set weight = 10 where id = 37; -- exercism
select * from subtasks order by taskcategory_id


select * from subtasks


SELECT * FROM pg_stat_activity;