def maxi(l):
    a=l[0]
    for i in range(len(l)):
        if a<l[i]:
            a=l[i]
    return a
def mini(l):
    a=l[0]
    for i in range(len(l)):
        if a>l[i]:
            a=l[i]
    return a
def second(l):
    m=maxi(l)
    l.remove(m)
    s=maxi(l)
    return s
l=[1,3,4,67,2]
m=maxi(l)
n=mini(l)
q=second(l)
print(m,n,q)
