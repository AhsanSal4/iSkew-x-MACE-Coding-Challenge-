n,t=map(int,input().split())
s=0
c=0
l1=list(map(int,input().split()))
print(l1)
for i in l1:
    s=s+i
    c+=1
    if s>t:
        s=s-i
        c-=1
        break
print(c)
