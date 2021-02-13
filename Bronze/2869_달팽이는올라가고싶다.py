
def snail(A, B, V):

    if (V-A) % (A-B) == 0:
        return (V-A)//(A-B) + 1
    else:
        return (V-A)//(A-B) + 2


A, B, V = map(int, input().split())
ans = snail(A, B, V)
print(ans)

