# String, Date



### 루시와 엘라 찾기

```mysql
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME in ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY ANIMAL_ID
```

> in 연산자 활용
>
> NAME이 저기 안에 있을 때 추출



### 이름에 el이 들어가는 동물 찾기

```mysql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME LIKE "%EL%" and ANIMAL_TYPE = 'Dog'
ORDER BY NAME
```

> LIKE 활용
>
> 문제에서 대소문자 구분 안한다고 해서 EL만 해줌
>
> | ANIMAL_ID | NAME    |
> | --------- | ------- |
> | A355753   | Elijah  |
> | A382192   | Maxwell |



### 중성화 여부 파악하기

```mysql
SELECT ANIMAL_ID, NAME,
CASE WHEN SEX_UPON_INTAKE LIKE '%Neutered%' or SEX_UPON_INTAKE LIKE '%Spayed%' THEN 'O' ELSE 'X' END
FROM ANIMAL_INS
```

> - IF
>
>   if (조건문, 참일 때 값, 거짓일 때 값)
>
> - CASE
>
>   `select case a when '1' then a when '2' then b else c end`
>
> | ANIMAL_ID | NAME      | 중성화 |
> | --------- | --------- | ------ |
> | A355753   | Elijah    | O      |
> | A373219   | Ella      | O      |
> | A382192   | Maxwell 2 | X      |



### 오랜 기간 보호한 동물 (2)

```mysql
SELECT OUTS.ANIMAL_ID, OUTS.NAME
FROM ANIMAL_OUTS OUTS
LEFT JOIN ANIMAL_INS INS
ON OUTS.ANIMAL_ID = INS.ANIMAL_ID
ORDER BY OUTS.DATETIME - INS.DATETIME DESC
LIMIT 2
```



### DATETIME에서 DATE로 형 변환

```mysql
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') AS 날짜
FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC
```

> DATE_FORMAT(DATE, 형식) 을 통해 DATE의 형식을 바꿀 수 있다.
>
> `%Y`(4자리 연도), `%y`(2자리 연도), `%m`(월), `%d`(일), `%H`(24시간), `%h`(12시간)