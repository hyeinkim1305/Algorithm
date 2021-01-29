# BOJ 10814번

##### 나이순 정렬 https://www.acmicpc.net/problem/10814 



##### 튜플로 리스트에 넣기

```python
info_list = []
for i in range(T):
    a, b = input().split()
    info_list.append((a, b))  
```



##### 리스트 내 튜플 정렬

```python
info_list_s = sorted(info_list, key = lambda x : x[0])
```



궁금점.. a를 int로 안바꿨는데 람다사용해서 sorted했는데 int형으로 한 것 처럼 정렬이 되었다.. 왜지? 잘못 푼 건가 싶다

