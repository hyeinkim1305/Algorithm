# SWEA 1983번



##### 풀이방식

> 우선 각자의 총점을 계산해서 총점이랑 번호를 리스트에 넣고 정렬 후 for문 돌리면서 번호인사람을 찾아 그때의 위치로 학점을 찾으려고 했다. sol1으로 했을 때는 런타임에러가 자꾸 나와서 다른 코드를 찾아보며 불필요한 코드를 빼거나 이중리스트를 리스트 안에 튜플로 바꾸었다.  



##### 리스트 안에 튜플 (index랑 요소)

```python
result = []
    for idx, score in enumerate(scores):
        result.append((score, idx+1))
```



##### 내림차순 정렬

```python
result = sorted(result, reverse=True)
```

