import random
passlen = int(input("Enter the length of password: "))
l="abcdefghijklmnopqrstuvwxyz"
u="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n="01234567890"
s="!@#$%^&*()?"
allchar="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
count=passlen//4
pl = "".join(random.sample(l,count))
pu = "".join(random.sample(u,count ))
pn = "".join(random.sample(n,count ))
ps = "".join(random.sample(s,count ))
print(pl,pu,pn,ps)
chars = pl+pu+pn+ps
diff = passlen - len(chars)
diffchars = "".join(random.sample(allchar,diff ))
finalchar=chars+diffchars
password= "".join(random.sample(finalchar,passlen))      #Since strings and tuples are immutable. Using random.shuffle() on them raises a TypeError
#print(finalchar)
print(password)
#print(len(password))
