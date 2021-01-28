word = input()

# word 길이를 잘라서 출력할 횟수
word_count = len(word) // 10 

if len(word) % 10 == 0:
    for i in range(word_count):
        print( word[i*10 : (i+1)*10] )
        
else:
    for i in range(word_count):
        print( word[i*10 : (i+1)*10] )
    print(word[word_count*10 :])



