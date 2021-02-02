t = int(input())

s = list(map(int,input().split()))
ss = sorted(s)
num = len(ss) // 2
print(ss[num])