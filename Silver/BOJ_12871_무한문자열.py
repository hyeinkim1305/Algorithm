def compare(l, s):
    mul = len(l) * len(s)
    l = l * len(s)
    s = s * len(l)
    for i in range(mul):
        if l[i] != s[i]:
            return 0
    return 1


s = input()
t = input()

print(compare(s, t))
