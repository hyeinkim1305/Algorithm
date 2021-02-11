
def testnum(n):
    count = 0
    if n <= 99:
        return n
    else:
        for i in range(100, n+1):
            hund = i // 100
            ten = (i % 100) // 10
            one = (i % 100) % 10

            if hund - ten == ten - one:
                count += 1

        return 99 + count

N = int(input())
# N까지 하면서
output = testnum(N)
print(output)






