# JOIN

> JOIN 절 은 두 개 이상의 테이블에서 관련성이 있는 컬럼에 기초하여 행을 결합하는 데 사용
>
> - CROSS JOIN
>
> - LEFT JOIN
>
>   왼쪽에 위치한 테이블 전부가 포함 & 오른쪽에 위치한 테이블은 조건이 만족하는 경우만 포함
>
>   A, B 테이블 중에 A 값의 전체와 A의 키값, B의 키값이 같은 결과를 리턴
>
>   ```
>   SELECT ~
>   FROM TABLE_A
>   LEFT JOIN TABLE_B ON TABLE_A.KEY = TABLE_B.KEY
>   ```
>
>   이때, A에는 있으나 B에는 없을 때는 null 값으로 들어가게 됨.
>
>   `WHERE TABLE_B.KEY is null`을 추가하면 순수 A의 값만 뽑힌다.
>
> - INNER JOIN
>
>   두 테이블을 조인하여 조인절에 해당하는 결과만 생성
>
>   ```
>   SELECT t1.id, t2.id
>   FROM t1
>   INNER JOIN t2
>   ON t1.pattern = t2.pattern
>   ```
>
> - RIGHT JOIN
>
>   오른쪽에 위치한 테이블 전부가 포함 & 왼쪽에 위치한 테이블은 조건이 만족하는 경우만 포함
>
>   ```
>   SELECT t1.id, t2.id
>   FROM t1
>   RIGHT JOIN t2
>   ON t1.pattern = t2.pattern
>   ORDER BY t2.id
>   ```
>
>   



### 없어진 기록 찾기

```mysql
SELECT OUTS.ANIMAL_ID, OUTS.NAME
FROM ANIMAL_OUTS OUTS
LEFT JOIN ANIMAL_INS INS
ON OUTS.ANIMAL_ID = INS.ANIMAL_ID
WHERE INS.ANIMAL_ID is NULL
ORDER BY OUTS.ANIMAL_ID
```

> OUTs를 기준으로 INS를 조인
>
> | ANIMAL_ID | NAME   |
> | --------- | ------ |
> | A349480   | Daisy  |
> | A349733   | Allie  |
> | A349990   | Spice  |
> | A362137   | *Darcy |



### 있었는데요 없었습니다

```mysql
SELECT INS.ANIMAL_ID, INS.NAME
FROM ANIMAL_INS INS
LEFT JOIN ANIMAL_OUTS OUTS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE INS.DATETIME > OUTS.DATETIME
ORDER BY INS.DATETIME
```

> ON 부분 주의!
>
> | ANIMAL_ID | NAME     |
> | --------- | -------- |
> | A381217   | Cherokee |



### 오랜 기간 보호한 동물 (1)

```mysql
SELECT INS.NAME, INS.DATETIME 
FROM ANIMAL_INS INS
LEFT JOIN ANIMAL_OUTS OUTS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE OUTS.ANIMAL_ID is NULL
ORDER BY INS.DATETIME ASC
LIMIT 3
```

> | NAME   | DATETIME            |
> | ------ | ------------------- |
> | Shelly | 2015-01-29 15:01:00 |
> | Jackie | 2016-01-03 16:25:00 |
> | Benji  | 2016-04-19 13:28:00 |