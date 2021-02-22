
T = int(input())
for tc in range(1, T+1):
     N = int(input())

     tri = []
     for i in range(N):
         tri.append([1]*(i+1))

     for j in range(2, N):
         for k in range(1,len(tri[j])-1):
            tri[j][k] = tri[j-1][k-1] + tri[j-1][k]

     print(f'#{tc}')
     for i in tri:
         for j in i:
             print(j, end = " ")
         print()