n=int(input())
l1=[]
l2=[]
a=0
b=0
for i in range(n):
    x,y=map(int,input().split())
    l1.append(x)
    l2.append(y)
l1.sort()
l2.sort()
if n%2==0:
    a=l1[(n//2)-1]+l1[(n//2)]
    a=a//2
    b=l2[(n//2)-1]+l2[(n//2)]
    b=b//2
else:
    a=l1[n//2]
    b=l2[n//2]
print(a,b)
