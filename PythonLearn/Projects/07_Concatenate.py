text = input()
words = text.split()
# print(type(words))
# concat = "-".join(words)
# print(concat)
def concatenate(*args):
    l=[]
    for arg in args:
        l=l+arg
    concat="-".join(l)
    return concat

print(concatenate(words))
# print(c)
# print(type(c))
