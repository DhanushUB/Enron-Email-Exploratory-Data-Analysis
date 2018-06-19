Load:

use enron;
drop table if exists enron_emails;
CREATE EXTERNAL TABLE enron_emails(
        email_date string, 
        sender string, 
        reciever string, 
        subject string, 
        id int)
      ROW FORMAT DELIMITED 
        FIELDS TERMINATED BY '\t' 
        LINES TERMINATED BY '\n' 
      STORED AS INPUTFORMAT 
        'org.apache.hadoop.mapred.TextInputFormat' 
      OUTPUTFORMAT 
        'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
      LOCATION
        'hdfs:///user/training/result_mr';

Queries:

1.************ Top 15 mail recipients in the company: *******************
select reciever, count(*) as count from enron_emails 
group by reciever
order by count desc 
limit 15;

2.************Top 15 mail senders in the company : *******************
select sender, count(*) as count from enron_emails 
group by sender 
order by count desc 
limit 15;

3. ********** Average emails recieved by the top 15 recipients**********
select avg(count) from (select reciever, count(*) as count from enron_emails 
group by reciever
order by count desc 
limit 15)enron_emails;

4.********** Average emails sent by the top 20 sender **********
select avg(count) from (select sender, count(*) as count from enron_emails 
group by sender
order by count desc 
limit 15)enron_emails;

5.***********Number of senders with same subject line*************

select sender,subject, count(*) AS CountOf
    from enron_emails
    group by sender,subject
    having count(*)>1
