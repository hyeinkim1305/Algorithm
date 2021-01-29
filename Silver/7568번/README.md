# BOJ 7568번

##### 덩치 https://www.acmicpc.net/problem/7568 



##### 이중for문

> 이중 for문을 사용해서 풀었다. 꽤 시간이 걸렸다. 종종 연습하기!
>
> ```python
> rank_list = []
> for j in range(len(student_list)):
>     # 기본 rank는 1로 설정
>     rank = 1
>     # 조건에 맞으면 rank에 1을 더한다
>     for k in range(len(student_list)):
>         if (student_list[j][0] < student_list[k][0]) and (student_list[j][1] < student_list[k][1]):
>             rank += 1
>     # rank리스트에 넣는다.
>     rank_list.append(rank)
> ```