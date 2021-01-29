
T = int(input())

info_list = []

for i in range(T):
    a, b = input().split()
    info_list.append((a, b))   # 튜플로 넣기 

info_list_s = sorted(info_list, key = lambda x : x[0])

for s in info_list_s:
    print(s[0], s[1]) # 이렇게 출력하면 한 칸 띄고 보인다
