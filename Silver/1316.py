n = int(input())
s_group = 0
for i in range(n):
    s = input()
    for j in range(len(s)):
        if j != len(s) -1:
            if s[j] == s[j+1]:
                continue 
            elif s[j] in s[j+1:]:
                break
        else:
            s_group += 1
print(s_group)

    
