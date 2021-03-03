
N, M = map(int, input().split())
tree = list(map(int, input().split()))
start = 1
end = max(tree)
ans = 0

while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for i in tree:
        if i < mid:
            continue
        cnt += i - mid
    if cnt >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)

'''
# 이분 탐색_재귀
def binary(arr, key, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if arr[mid] > key:
        return binary(arr, key, start, mid-1)
    elif arr[mid] < key:
        return binary(arr, key, mid + 1, end)
    else:
        return True
'''

