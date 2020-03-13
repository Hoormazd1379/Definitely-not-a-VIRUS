money = []
listen = True
while listen:
    mm = int(input())
    if mm != 0:
        money.append(mm)
    else:
        listen = False
 
def sweet(i, word):
    to_print = "Input #" + str(i) + ": " + word + "!"
    print(to_print)
    
base = 0
s = "Sweet"
ts = "Totally Sweet"
index = 1  
for pay in money:
    base += pay
    if base >= 50 and base < 100:
        base -= 50
        sweet(index, s)
        
    elif base >= 100:
        base = base%50
        sweet(index, ts)
        
    index += 1
        
        
        
        
        
