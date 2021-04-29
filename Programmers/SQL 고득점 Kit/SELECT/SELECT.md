# SELECT

[TOC]



### 모든 레코드 조회하기

```mysql
SELECT *
FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC;
```

> ASC : 오름차순
>
> DESC : 내림차순





### 역순 정렬하기

```mysql
SELECT NAME, DATETIME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC;
```





### 아픈 동물 찾기

```mysql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'Sick'
ORDER BY ANIMAL_ID
```





### 어린 동물 찾기

```mysql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION != 'Aged'
ORDER BY ANIMAL_ID
```

> WHERE ~ != 이런 표현도 가능하다!



### 동물의 아이디와 이름

```mysql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC
```



### 여러 기준으로 정렬하기

```mysql
SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME ASC, DATETIME DESC
```



### 상위 N개 레코드

```mysql
SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1
```

동물원에 들어온 동물 중 가장 먼저 보호소에 들어온 한 마리

> LIMIT num : 원하는 개수만큼 가져오기