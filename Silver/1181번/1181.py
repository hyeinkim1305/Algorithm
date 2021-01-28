n = int(input())

word_list = []

# word의 길이와 word를 리스트에 튜플로 넣어준다.
for i in range(n):
    word = input()
    word_list.append((len(word), word))

# 리스트를 set을 활용해 중복을 제거한다.
word_list = list(set(word_list))

# 문자의 길이, 문자 순으로 정렬해준다
word_list.sort(key = lambda x : (x[0],x[1]))

for w in word_list:
    print(w[1])


