
--weekend/evenings

update taskcategory set weight = 5 where id = 20;  -- saas
update taskcategory set weight = 0 where id = 15 ; -- aws
update taskcategory set weight = 5 where id = 14 ;-- coding
update taskcategory set weight = 15 where id = 16 ; -- leisure
update taskcategory set weight = 15 where id = 19 ; -- art
update taskcategory set weight = 10 where id = 17; -- housework
select * from taskcategory


--daytime/cherry
update taskcategory set weight = 15 where id = 20; -- #saas
update taskcategory set weight = 40 where id = 15; -- #aws
update taskcategory set weight = 10 where id = 14;  --#coding
update taskcategory set weight = 0 where id = 16;  --#leisure
update taskcategory set weight = 0 where id = 19; -- #art
update taskcategory set weight = 0 where id = 17; -- housework
select * from taskcategory

--homeworking
update taskcategory set weight = 25 where id = 20; -- #saas
update taskcategory set weight = 25 where id = 15; -- #aws
update taskcategory set weight = 5 where id = 14;  --#coding
update taskcategory set weight = 5 where id = 16;  --#leisure
update taskcategory set weight = 5 where id = 19; -- #art
update taskcategory set weight = 5 where id = 17; -- housework
select * from taskcategory





