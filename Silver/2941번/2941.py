
word = input()
alphabet = ['c=', 'c-', 'dz=','d-','lj','nj','s=','z=']

for al in alphabet:
    
    if al in word:
        n = word.count(al)
        
        for i in range(n):
            word = word.replace(al,' ')

print(len(word))

