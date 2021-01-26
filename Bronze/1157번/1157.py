
# sol1
word = input()

word_list = []
num_list = []

# 모든 문자를 대문자로 바꾼다.
word = word.upper()

for w in word:
    if w not in word_list:
        num_list.append(word.count(w))
        word_list.append(w)
    else:
        continue

max_num = max(num_list)

if (num_list.count(max_num)) > 1:
    print('?')
else:
    idx = num_list.index(max_num)
    print(word_list[idx])


# sol2
# set 활용하기
word = input().upper()
words = list(set(word))

num_list = []
for w in words:
    num = word.count(w)
    num_list.append(num)

if num_list.count(max(num_list)) > 1:
    print("?")
else:
    idx = num_list.index(max(num_list))
    print(words[idx])
