n = int(input())
words = []
results = []
for i in range(n):
    words.append(input())

#print(words)

def check(word):
    letters = list(word)
    letters.sort()
    single_letter = list(dict.fromkeys(letters))
    num = []
    
    for l in single_letter:
        num.append(letters.count(l))
        
    if ((sum(num)/len(num))/num[0] == 1):
        return "YES"
    else:
        return "NO"


    
for i in range(n):
    print("Test #"+str(i+1)+": "+check(words[i]))
