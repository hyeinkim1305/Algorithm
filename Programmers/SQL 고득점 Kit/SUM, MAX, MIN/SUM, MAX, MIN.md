#  SUM, MAX, MIN



### 최댓값 구하기

```mysql
SELECT DATETIME
FROM ANIMAL_INS
ORDER BY DATETIME DESC
LIMIT 1
```

> 가장 최근이면 DATETIME 기준으로 내림차순!

**MAX 이용**

```mysql
SELECT MAX(DATETIME) AS 시간
FROM ANIMAL_INS
```

> AS : 별칭을 한다.
>
> ColumnName AS 컬럼명칭 -- 컬럼에 별칭 부여하기 
>
> TableName AS 테이블명칭 -- 테이블에 별칭 부여하기



### 최솟값 구하기

```mysql
SELECT MIN(DATETIME) AS 시간
FROM ANIMAL_INS
```



### 동물 수 구하기

```mysql
SELECT COUNT(*)
FROM ANIMAL_INS
```



### 중복 제거하기

```mysql
SELECT COUNT(DISTINCT NAME)
FROM ANIMAL_INS
```

> DISTINCT : 중복 제거