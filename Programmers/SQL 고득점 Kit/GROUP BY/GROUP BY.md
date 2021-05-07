# GROUP BY

> **GROUP BY**
>
> 지정된 기준에 따라 행 세트를 그룹으로 결합한다. (어떤 필드의 값을 기준으로 그룹화시킴)
>
> 데이터를 요약하는 상황에서 주로 사용한다.
>
> GROUP BY : 특정 컬럼을 그룹화
>
> HAVING : 특정 컬럼을 그룹화한 결과에 조건을 건다.
>
> - django ORM에서 `annotate`와 대응
>
> ```sql
> SELECT column1, aggregate_function(column_2)
> FROM table
> GROUP BY column1, column2;
> ```



### 고양이와 개는 몇 마리 있을까

```mysql
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE)
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE ASC
```

> 컬럼이 Dog와 Cat 두 가지라서 GROUP BY 컬럼명만 해주면 된다.
>
> 여기서 만약, `ORDER BY ANIMAL_TYPE DESC` 라고 하면 Cat -> Dog 순서가 아닌 Dog -> Cat 순서로 나오게 된다.
>
> | ANIMAL_TYPE | count |
> | ----------- | ----- |
> | Cat         | 2     |
> | Dog         | 1     |



### 동명 동물 수 찾기

```mysql
SELECT NAME, COUNT(NAME) AS COUNT
FROM ANIMAL_INS
GROUP BY NAME 
HAVING COUNT(NAME) >= 2
ORDER BY NAME
```

> WHERE절은 한 행마다 조건을 걸어 가져오는것, 그런데 COUNT(NAME)은 이미 묶어서 가져온 것이기 때문에 WHERE절이 적용되지 못한다.
>
> 따라서 HAVING을 이용한다.
>
> | NAME  | COUNT |
> | ----- | ----- |
> | Lucy  | 3     |
> | Raven | 2     |



### 입양 시각 구하기(1)

```mysql
SELECT HOUR(DATETIME) AS HOUR, COUNT(DATETIME) AS COUNT
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) >= 9 AND HOUR(DATETIME) <= 19
GROUP BY HOUR(DATETIME)
ORDER BY HOUR(DATETIME) ASC
```

```mysql
SELECT HOUR(DATETIME) AS HOUR, COUNT(DATETIME) AS COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR(DATETIME)
HAVING HOUR >= 9 AND HOUR <= 19
ORDER BY HOUR
```

> 시간대별로 분류해서 COUNT를 구함
>
> HOUR() : 시 추출
>
> MONTH() : 월 추출
>
> YEAR() : 연도 추출
>
> MINUTE() : 분 추출
>
> DAY() : 일 추출
>
> | HOUR | COUNT |
> | ---- | ----- |
> | 9    | 1     |
> | 10   | 2     |
> | 11   | 13    |
> | 12   | 10    |



### 입양 시각 구하기(2)

```mysql
```







```mysql
count(*) : null값을 포함한 행의 수를 출력
count(표현식) : 표현식의 값이 null값인 것을 제외한 행의 수를 출력
sum(표현식) : 표현식의 null값을 제외한 합계를 출력
avg(표현식) : 표현식의 null값을 제외한 평균을 출력
max(표현식) : 표현식의 최대값 출력(문자,날짜데이터도 가능)
min(표현식) : 표현식의 최소값 출력
stddev(표현식) : 표현식의 표준편차 출력
varian(표현식) : 표현식의 분산 출력
```

