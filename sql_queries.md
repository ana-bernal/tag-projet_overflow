# SQL queries

This file contains the different SQL queries tested and comments about them.

The queries are made in the official query [stack overflow API](https://data.stackexchange.com/stackoverflow/query/new)

## OC suggested
Returned 1 row in total.

```SQL
SELECT TOP 100000 Title, 
                  Body, 
                  Tags, 
                  Id, 
                  Score, 
                  ViewCount, 
                  FavoriteCount, 
                  AnswerCount
FROM Posts 
WHERE PostTypeId = 1 AND ViewCount > 10 AND FavoriteCount > 10
AND Score > 5 AND AnswerCount > 0 AND LEN(Tags) - LEN(REPLACE(Tags, '<','')) >= 5
```

returned 1 row since

```SQL
SELECT COUNT(*)
FROM Posts 
WHERE FavoriteCount>0
```
returned `133`.

## Others

```SQL
SELECT TOP 100000 COUNT(*)
FROM Posts 
WHERE ViewCount > 0
```
Return: `23436251`

```SQL
SELECT COUNT(*)
FROM Posts
```
Returns:  `58095040`

```SQL
SELECT AVG(ViewCount)
FROM Posts
```
Returns error

```SQL
SELECT COUNT(*)
FROM Posts
WHERE AnswerCount>0
```

Returns : `20040292`

## V-01

```SQL
SELECT TOP 100000 Title, 
                  Body, 
                  Tags, 
                  Id, 
                  Score, 
                  ViewCount,
                  AnswerCount
FROM Posts 
WHERE (PostTypeId = 1 AND 
       ViewCount > 10 AND 
       Score > 5 AND 
       AnswerCount > 0 AND 
       LEN(Tags) - LEN(REPLACE(Tags, '<','')) >= 5)
```

Returns: `50 000` rows (verify)

```SQL
SELECT Title,
       Body, 
       Tags, 
       Id,
       Score, 
       ViewCount,
       AnswerCount
FROM Posts 
WHERE (PostTypeId = 1 AND 
       ViewCount > 10 AND 
       Score > 5 AND 
       AnswerCount > 0 AND 
       LEN(Tags) - LEN(REPLACE(Tags, '<','')) >= 5)
```

Returns: `50 000` rows (verify)