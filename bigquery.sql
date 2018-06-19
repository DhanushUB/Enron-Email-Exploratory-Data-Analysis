1.************ Top 15 mail recipients in the company: *******************

SELECT
  reciever,
  COUNT (*) AS count
FROM
  [enron.email_dataset]
GROUP BY
  reciever
ORDER BY
  count DESC
LIMIT
  15;

2.************Top 15 mail senders in the company: *******************
SELECT
  sender_firstname,
  COUNT (*) AS count
FROM
  [enron.email_dataset]
GROUP BY
  sender
ORDER BY
  count DESC
LIMIT
  15;

3. *********** Average emails sent by the top 20 senders ****************
SELECT
  AVG(count)
FROM (
  SELECT
    sender_firstname,
    COUNT (*) AS count
  FROM
    [enron.Email_data]
  GROUP BY
    sender_firstname
  ORDER BY
    count DESC
  LIMIT
    15)[enron.Email_data];

4. ***********Number of senders with same subject line*************
SELECT
  sender_firstname,
  sender_lastname,
  subject,
  COUNT(*) AS CountOf
FROM
  [enron.email_data]
GROUP BY
  sender_firstname,
  sender_lastname,
  subject
HAVING
  COUNT(*)>1
ORDER BY
  countOf DESC;
