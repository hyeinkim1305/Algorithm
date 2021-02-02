T = int(input())
for i in range(T):
	word = input()
	for w in range(len(word) // 2):
		if word[w] != word[-(w+1)]:
			print('#{} {}'.format(i+1, 0))
			break
	else:
		print('#{} {}'.format(i+1, 1))
