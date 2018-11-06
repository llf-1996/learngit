INSERT INTO test1 VALUES('4','3','3','3');
SELECT * FROM test1;

CREATE DATABASE 正则采集;

USE 正则采集;

# 建新浪新闻表
CREATE TABLE sina(
id INT PRIMARY KEY AUTO_INCREMENT,
url VARCHAR(100),
title VARCHAR(200)
);

/*
alter table sina
	add column collect_time datetime;
	
alter table sina
	modify url varchar(100);
alter table sina
	modify title varchar(200);
*/
# 
SELECT * FROM sina;
DESC sina;



# 
