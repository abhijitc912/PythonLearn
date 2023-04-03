import random
passlen = int(input("Enter the length of password: "))
l="abcdefghijklmnopqrstuvwxyz"
n="01234567890"
u="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s="!@#$%^&*()?"
allchar="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
count=passlen//4
pl = "".join(random.sample(l,count))
pn = "".join(random.sample(n,count ))
pu = "".join(random.sample(u,count ))
ps = "".join(random.sample(s,count ))
print(pl,pn,pu,ps)
chars = pl+pn+pu+ps
diff = passlen - len(chars)
diffchars = "".join(random.sample(allchar,diff ))
finalchar=chars+diffchars
password= "".join(random.sample(finalchar,passlen))      #Since strings and tuples are immutable. Using random.shuffle() on them raises a TypeError
#print(finalchar)
print(password)
#print(len(password))
