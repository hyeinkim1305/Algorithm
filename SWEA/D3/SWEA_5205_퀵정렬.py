'''
2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8
'''

def quicksort(a, l, r):
    if l < r:
        s = partition(a, l, r)
        quicksort(a, l, s-1)
        quicksort(a, s+1, r)

def partition(a, l, r):
    p = a[l]
    i, j = l, r
    while i <= j:
        while i <= r and a[i] <= p:
            i += 1
        while j > l and a[j] >= p:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]

    a[l], a[j] = a[j], a[l]

    return j

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    quicksort(a, 0, len(a)-1)
    print(f'#{tc} {a[N//2]}')

