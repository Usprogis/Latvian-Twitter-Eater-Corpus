# Data-preparation

1. Export `tweets`, `media` and `words` tables & import locally

```sql
SELECT * FROM `tweets` WHERE `tweets`.`created_at` BETWEEN '2020-02-19 02:27:41' and NOW() 
SELECT * FROM `media` WHERE `media`.`date` BETWEEN '2020-02-19 02:27:41' and NOW() 
SELECT * FROM `words` WHERE `words`.`datums` BETWEEN '2020-02-19 02:27:41' and NOW() 
```

2. Drop old, merge into one

```sql
DROP TABLE `tweets1`, `tweets2`, `tweets3`, `tweets4`;
CREATE TABLE `tweets1` as select * from tweets left join media on tweets.id = media.tweet_id;
CREATE TABLE `tweets2` as select * from tweets1 left join vietas on tweets1.geo = vietas.nosaukums;

CREATE TABLE `tweets3` as select * from tweets2 t left join (SELECT distinct(tvits) FROM words o) AS o ON o.tvits = t.id;
ALTER TABLE `tweets3` drop column tweet_id, drop column date, drop column emo;

CREATE TABLE `tweets4` as select * from tweets3 t left join (SELECT `tvits` tvid, GROUP_CONCAT(`vards`  SEPARATOR ';') vards, GROUP_CONCAT(`nominativs` SEPARATOR ';') nominativs, GROUP_CONCAT(`grupa` SEPARATOR ';') grupa, GROUP_CONCAT(`eng` SEPARATOR ';') eng FROM words GROUP BY tvid) AS o ON o.tvits = t.id;
```

3. Export to JSON