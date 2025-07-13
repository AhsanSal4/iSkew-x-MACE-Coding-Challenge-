l1=list(map(int,input().split(',')))
k=int(input())
l1.sort()
a=l1[:k]
mi=a[-1]-a[0]
s=0
for i in range(1,len(l1)-k+1):
    s=l1[i+k-1]-l1[i]
    if s<mi:
        mi=s
        a=l1[i:i+k]
for i in a:
    print(i,end=" ")
