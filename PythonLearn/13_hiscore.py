def game():
    return 5000

score = game()

with open('13_hiscore.txt') as f:
    hiscore= f.read()
    
if hiscore == '':
    with open('13_hiscore.txt','w') as f:
        f.write(str(score))  
         
elif score>int(hiscore):
    with open('13_hiscore.txt','w') as f:
        f.write(str(score))
