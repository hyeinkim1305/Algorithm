
# 문자열을 순회하는 과정 중 ans가 0보다 클 수 는 있어도 작을 수는 없다.
T = int(input())

for i in range(T):
    wo = input()
    word = list(wo)
    ans = 0

    # '(' 일 때는 +1을 더하고 ')'일 때는 -1 하는 방식으로 푼다
    for w in word:

        # 문자열을 순회하면서 ans가 0보다 클 수 는 있어도 작을 수는 없다.
        
        if w =='(':
            ans += 1
            
        elif w == ')':
            ans -= 1

        if ans < 0:
            print('NO')
            break   
        
    if ans == 0:
        print('YES')

    # ans가 0보다 커도 'NO'이다.
    elif ans > 0:                # else: 라고 하게 되면 ans가 음수일 때 NO가 두번 나옴.
        print('NO')
        
