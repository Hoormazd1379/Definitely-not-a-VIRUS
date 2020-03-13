n = int(input())
words = []

def accept():
    w = sorted(list(input()), reverse=True)
    nw = []
    for c in w:
        nw.append(ord(c))
    return nw
    
for i in range(n):
    s1 = accept()
    s2 = accept()
    words.append([s1, s2])

#words =  [[[122, 122, 122, 121], [122, 121, 120,  99,  98,  97]], [[121,  97], [121, 120]], [[114, 111, 111, 111, 108, 106, 105, 105,  97], [114, 111, 111, 111, 108, 106, 105, 105,  97]]]
#words = [[['z', 'z', 'z', 'y'], ['z', 'y', 'x', 'c', 'b', 'a']], [['y', 'a'], ['y', 'x']], [['r', 'o', 'o', 'o', 'l', 'j', 'i', 'i', 'a'], ['r', 'o', 'o', 'o', 'l', 'j', 'i', 'i', 'a']]]

def check(w1, w2, cp):
    l = min(len(w1), len(w2)) 
    while l > 0:
        l -= 1
        if w1[0] == w2[0]:
            w1.pop(0)
            w2.pop(0)
        elif w1[0] > w2[0]:
            print("Data set #" + str(cp) + ": First is older")
            return False
        elif w1[0] < w2[0]:
            print("Data set #" + str(cp) + ": First is younger")
            return False
    return True
            
            
            
            
cpN = 0
for couple in words:
    cpN += 1
    wA = couple[0]
    wB = couple[1]
    if check(wA, wB, cpN):
        if len(wA) == 0 and len(wB) == 0:
            print("Data set #" + str(cpN) + ": Same age")
        elif len(wA) > len(wB):
            print("Data set #" + str(cpN) + ": First is older")
        elif len(wA) < len(wB):
            print("Data set #" + str(cpN) + ": First is younger")
            