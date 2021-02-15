
x, y, w, h = map(int, input().split())
distance = [h-y, y, x, w-x]
min_distance = 987654321

for i in distance:
    if i < min_distance:
        min_distance = i

print(min_distance)