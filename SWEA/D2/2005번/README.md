# SWEA 2005번



##### 이중 리스트 출력시

> ```python
> answer = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
> for num in answer:
>     num = map(str, num)
>     print(' '.join(num))
> ```
>
> 1
> 1 1
> 1 2 1
> 1 3 3 1
>
> 이렇게 나온다! join은 문자열로 된 것을 합칠 수 있어서 숫자로 되어있는 리스트를 바꿔야했다. 