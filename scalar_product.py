n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l1.sort()
a=0
l2.sort(reverse=True)
for i in range(n):
    a=a+(l1[i]*l2[i])
print(a)
