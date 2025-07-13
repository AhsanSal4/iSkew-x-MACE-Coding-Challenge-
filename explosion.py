n,a,b=map(int, input().split())
l1=[]
for i in range(n):
    l=list(map(int, input().split()))
    l1.append(l)
l2=sorted(l1,key=lambda x: abs(x[0]-a) + abs(x[1]-b))
print(l2)
for i in l2:
    if i in l1:
        print(l1.index(i)+1,end=" ")
