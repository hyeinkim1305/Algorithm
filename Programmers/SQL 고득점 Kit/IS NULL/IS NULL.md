# IS NULL



### 이름이 없는 동물의 아이디

```mysql
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME is NUll
```



### 이름이 있는 동물의 아이디

```mysql
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME is NOT NULL
```

> 이름이 null이 아닌 ID 추출



### NULL 처리하기

```mysql
SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name') AS NAME, SEX_UPON_INTAKE 
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```

> IFNULL(A, B) : A가 Null이면 B, 그렇지 않다면 A
>
> | ANIMAL_TYPE | NAME    | SEX_UPON_INTAKE |
> | ----------- | ------- | --------------- |
> | Cat         | Jewel   | Spayed Female   |
> | Cat         | Meo     | Neutered Male   |
> | Dog         | No name | Spayed Female   |