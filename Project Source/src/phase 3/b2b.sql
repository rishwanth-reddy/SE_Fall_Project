/*
SQLyog - Free MySQL GUI v5.0
Host - 5.0.45-community-nt : Database - b2b
***********************
Server version : 5.0.45-community-nt
*/

/Developed by Divya Kumbham & Rishwanth Reddy/
create database if not exists `b2b`;

USE `b2b`;

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) default NULL,
  `session_data` longtext,
  `expire_date` datetime default NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

insert into `django_session` values 

('b74fm8g1rbqpr4lhdszxr89a1qwyk11c','MmY2ZWFjYjY0M2JjYTA0NTBiNjUyNzNmODQ5YjAxODAyYjk0ODc4ODp7Im93bmlkIjoidGVqYSIsImxvZ2dlZHVzZXIiOiJ0ZWphIiwiZW1haWwiOiJ0ZWp1ZGF0YXBvaW50NUBnbWFpbC5jb20ifQ==','2019-08-28 10:56:42'),

('kwe5g5eh5oi3nn6c2yhkx217mmi82104','OTliMDFmZmE2NzZkODA5Zjg3ODM2Y2U3ZTZiMmQ0YjdlZDExZjVkYjp7Im93bmlkIjoiTWVnaGFuYSIsImxvZ2dlZHVzZXIiOiJqYXlhIiwiZW1haWwiOiJqYXlhQGdtYWlsLmNvbSIsInVzZXJpZCI6ImpheWEifQ==','2019-09-02 05:32:22'),

('1n6qogue8d64lur780e1yvscdkcthhkz','Y2Y0OTUxYmIxYWQ1OTg3MDBhNDY2Yjg1Njc2MmE4YmI1ODM4OTAxMzp7InVzZXJpZCI6ImpheWEiLCJsb2dnZWR1c2VyIjoiamF5YSIsImVtYWlsIjoiamF5YUBnbWFpbC5jb20ifQ==','2019-09-02 10:15:13'),

('n63zqzli3ul5oja996wl793dmurfkvbh','M2IwYTI1NGI4NDFiZTI2YjQ4ZmVmYzg1NTEwYjM0NWRjNjcyMzU4NTp7InVzZXJpZCI6ImpheWEiLCJsb2dnZWR1c2VyIjoiamF5YSIsImVtYWlsIjoiamF5YUBnbWFpbC5jb20iLCJvd25pZCI6Ik1lZ2hhbmEifQ==','2019-09-02 11:25:06'),

('kxiv18n2lnosgs2ifjouceg7h4jzjmhc','ZWRkZTI0MWFhNjg2NDIyMjMwYzNjYWNhZGI5MmQzNjJiNjczYjU2Yjp7InVzZXJpZCI6Imp5byIsImxvZ2dlZHVzZXIiOiJqeW8iLCJlbWFpbCI6Imp5b0BnbWFpbC5jb20ifQ==','2019-09-03 05:41:16'),

('9p6nmxinwfj3l6m7ty12dogoq8uklcc7','ZGZmYzQ4ZmNkMTRlZTY1MTZiODE5MWM5M2Q5YWM5MWZkMGJhZDA3MTp7InVzZXJpZCI6Imp5byIsImxvZ2dlZHVzZXIiOiJqeW8iLCJlbWFpbCI6Imp5b0BnbWFpbC5jb20iLCJvd25pZCI6Ik1lZ2hhbmEifQ==','2019-09-03 07:07:16'),

('pynugueevxct0ug3aqdtqp1mauoeusnb','Y2Y0OTUxYmIxYWQ1OTg3MDBhNDY2Yjg1Njc2MmE4YmI1ODM4OTAxMzp7InVzZXJpZCI6ImpheWEiLCJsb2dnZWR1c2VyIjoiamF5YSIsImVtYWlsIjoiamF5YUBnbWFpbC5jb20ifQ==','2019-09-03 08:34:54'),

('341126nka06rc7tob7ldok18bd2lemsr','Y2Y0OTUxYmIxYWQ1OTg3MDBhNDY2Yjg1Njc2MmE4YmI1ODM4OTAxMzp7InVzZXJpZCI6ImpheWEiLCJsb2dnZWR1c2VyIjoiamF5YSIsImVtYWlsIjoiamF5YUBnbWFpbC5jb20ifQ==','2019-09-03 08:59:02'),

('qt8mtb9onq2ekoxpo3pkcz6hg1c2rqm9','Y2Y0OTUxYmIxYWQ1OTg3MDBhNDY2Yjg1Njc2MmE4YmI1ODM4OTAxMzp7InVzZXJpZCI6ImpheWEiLCJsb2dnZWR1c2VyIjoiamF5YSIsImVtYWlsIjoiamF5YUBnbWFpbC5jb20ifQ==','2019-09-03 09:43:37'),

('5j3gspmy64tuo8libm6apog372nv913c','ZWRkZTI0MWFhNjg2NDIyMjMwYzNjYWNhZGI5MmQzNjJiNjczYjU2Yjp7InVzZXJpZCI6Imp5byIsImxvZ2dlZHVzZXIiOiJqeW8iLCJlbWFpbCI6Imp5b0BnbWFpbC5jb20ifQ==','2019-09-04 03:46:35'),

('exkp1o3oyzowc4t7uh23l2m5ys0py5pp','ZWRkZTI0MWFhNjg2NDIyMjMwYzNjYWNhZGI5MmQzNjJiNjczYjU2Yjp7InVzZXJpZCI6Imp5byIsImxvZ2dlZHVzZXIiOiJqeW8iLCJlbWFpbCI6Imp5b0BnbWFpbC5jb20ifQ==','2019-09-04 04:12:37'),

('a4lq1d3jpqwehrhq6zrdbcu3htsuxhfo','ZWRkZTI0MWFhNjg2NDIyMjMwYzNjYWNhZGI5MmQzNjJiNjczYjU2Yjp7InVzZXJpZCI6Imp5byIsImxvZ2dlZHVzZXIiOiJqeW8iLCJlbWFpbCI6Imp5b0BnbWFpbC5jb20ifQ==','2019-09-04 05:33:28'),

('1lx7gwfknoceeh03wo00cyukqpra1qsx','ZWRkZTI0MWFhNjg2NDIyMjMwYzNjYWNhZGI5MmQzNjJiNjczYjU2Yjp7InVzZXJpZCI6Imp5byIsImxvZ2dlZHVzZXIiOiJqeW8iLCJlbWFpbCI6Imp5b0BnbWFpbC5jb20ifQ==','2019-09-04 06:20:01'),

('0n0oh27zpkc1aw2bomcxmxpk5o7xmpfu','ODEzYzY4M2VmMmU2YjVlNjYxYmQ2ZjgwOWQ2YzEwZDRhYTA3MjY4OTp7InVzZXJpZCI6Imp5byIsImxvZ2dlZHVzZXIiOiJNZWdoYW5hIiwiZW1haWwiOiJtZWdoYW5hQGdtYWlsLmNvbSIsIm93bmlkIjoiTWVnaGFuYSIsImlkIjo0fQ==','2019-09-13 08:43:28'),

('kshrimvnnmdqzck4wny1i1x61c2wt6ep','ZGZmYzQ4ZmNkMTRlZTY1MTZiODE5MWM5M2Q5YWM5MWZkMGJhZDA3MTp7InVzZXJpZCI6Imp5byIsImxvZ2dlZHVzZXIiOiJqeW8iLCJlbWFpbCI6Imp5b0BnbWFpbC5jb20iLCJvd25pZCI6Ik1lZ2hhbmEifQ==','2019-09-19 10:14:59'),

('3gsscbyo5d54vdd4j3p99y4c82p4ljxd','ZGZmYzQ4ZmNkMTRlZTY1MTZiODE5MWM5M2Q5YWM5MWZkMGJhZDA3MTp7InVzZXJpZCI6Imp5byIsImxvZ2dlZHVzZXIiOiJqeW8iLCJlbWFpbCI6Imp5b0BnbWFpbC5jb20iLCJvd25pZCI6Ik1lZ2hhbmEifQ==','2019-09-20 04:41:12'),

('55bjbifg6x53d16pedf1y6gcsqm1mpuo','ZWRkZTI0MWFhNjg2NDIyMjMwYzNjYWNhZGI5MmQzNjJiNjczYjU2Yjp7InVzZXJpZCI6Imp5byIsImxvZ2dlZHVzZXIiOiJqeW8iLCJlbWFpbCI6Imp5b0BnbWFpbC5jb20ifQ==','2019-09-20 04:42:17'),

('fojd8nlwbtgpwv1f2a3f6sl7fyileo3t','ZWRkZTI0MWFhNjg2NDIyMjMwYzNjYWNhZGI5MmQzNjJiNjczYjU2Yjp7InVzZXJpZCI6Imp5byIsImxvZ2dlZHVzZXIiOiJqeW8iLCJlbWFpbCI6Imp5b0BnbWFpbC5jb20ifQ==','2019-09-20 05:04:18'),

('5ithpvwdaeqdez0h8g0sldkn129sqzfq','YzViOThmZDQ0ZGFmN2IxMWZlOTk3Njk2YmUxYzExNGIxYzU2YTU5Mjp7InVzZXJpZCI6Imp5byIsImxvZ2dlZHVzZXIiOiJqeW8iLCJlbWFpbCI6Imp5b0BnbWFpbC5jb20iLCJvd25pZCI6Ik1lZ2hhbmEiLCJpZCI6MX0=','2019-09-20 08:34:45'),

('457qv2z7icyv4ydfh9i6nmkt1pekzf0m','YjhlODZhYTJjZDY0YTkzZDdhYWFhZWNiZTQ2NGE3MGQxMDA1MGFjNzp7InVzZXJpZCI6Imp5byIsImxvZ2dlZHVzZXIiOiJqeW8iLCJlbWFpbCI6Imp5b0BnbWFpbC5jb20iLCJpZCI6MSwib3duaWQiOiJNZWdoYW5hIn0=','2019-09-20 11:37:30'),

('4ny6qb9itl3a03tcf0vn6muwrjbi42sw','NTdhYWIyMmM3ZmI4NWZjMWFhZDM3MzE5MjQ3NTgxYjRlMzk5MzMxYTp7Im93bmlkIjoic2hhYW4iLCJsb2dnZWR1c2VyIjoiYWxleCIsImVtYWlsIjoibHgxNjBjbUBnbWFpbC5jb20iLCJ1c2VyaWQiOiJhbGV4IiwiaWQiOjEyfQ==','2019-09-21 11:02:11'),

('fnc548jsspef94q1d8c9xu4zh6f1shb8','NTdhZWVjMzYzOWIxNzM0MTUzZTFiNjJkOWZkNzMzYmQ2OGI2ODE2Zjp7InVzZXJpZCI6InNvbnkiLCJsb2dnZWR1c2VyIjoic29ueSIsImVtYWlsIjoic29ueUBnbWFpbC5jb20iLCJpZCI6OH0=','2019-09-21 12:13:41'),

('9a9gydiw7zrmvmisvssjlswzvofmtfwj','Yzc1YzdmMzY2N2ZjYjIzZTEwNmY1ZTVkMjI2OTBlMGUyYzA1OTUyNDp7Im93bmlkIjoiYW1nb3RoIiwibG9nZ2VkdXNlciI6ImFtZ290aCIsImVtYWlsIjoiYW1nb3RoMTIzQGdtYWlsLmNvbSIsInVzZXJpZCI6InNpcmkiLCJpZCI6MTN9','2019-09-30 11:54:02');

/*Table structure for table `simpleb2b_orderproductsmodel` */

DROP TABLE IF EXISTS `simpleb2b_orderproductsmodel`;

CREATE TABLE `simpleb2b_orderproductsmodel` (
  `id` int(100) NOT NULL auto_increment,
  `name` varchar(100) default NULL,
  `productname` varchar(100) default NULL,
  `address` varchar(100) default NULL,
  `mobilenumber` varchar(100) default NULL,
  `bankname` varchar(100) default NULL,
  `accountnumber` varchar(100) default NULL,
  `amount` int(50) default NULL,
  `date` date default NULL,
  `time` time default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=latin1;

/*Data for the table `simpleb2b_orderproductsmodel` */

insert into `simpleb2b_orderproductsmodel` values 

(25,'alex','Xiaomy Note 7','Hyderabd','9849555','SBI','15225',9999,'2019-09-07','16:55:00'),

(26,'ramya','Xiaomy Note 7','guntur','987456123','andra','1122335567',9999,'2019-09-07','16:50:00'),

(28,'jyo','blackcar','repalle','8989898989','SBI','11001000011',220000,'2019-09-07','17:26:00'),

(29,'sunny','bluecar','guntur','8910101010','andra','1000010000',540000,'2019-09-07','17:28:00'),

(30,'sunny','whitebike','tenali','8911001100','ICIC','10029900000',120000,'2019-09-07','17:30:00'),

(31,'jyo','whitebike','repalle','8912000111','ICIC','110000101001',120000,'2019-09-07','17:33:00'),

(32,'siri','pinkscooty','guntur','9877660099','SBI','11000100101',60000,'2019-09-07','17:41:00'),

(33,'sony','pinkscooty','tenali','9800002627','ICIC','100000000',60000,'2019-09-07','17:44:00'),

(34,'kalpana','BWMcar','#102,Sree Street','98490458960','SBI','58902215485',5000000,'2019-09-16','05:58:00'),

(35,'kalpana','Duke Bike','#102,Sree Street','98490458960','SBI','58902215485',285000,'2019-09-16','05:58:00'),

(36,'siri','Duke Bike','#103 Meghana merchent','9849056586','SBI','898554555',285000,'2019-09-16','05:58:00');

/*Table structure for table `simpleb2b_sellerregistrationmodel` */

DROP TABLE IF EXISTS `simpleb2b_sellerregistrationmodel`;

CREATE TABLE `simpleb2b_sellerregistrationmodel` (
  `id` int(100) NOT NULL auto_increment,
  `name` varchar(100) NOT NULL,
  `loginid` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `authkey` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
