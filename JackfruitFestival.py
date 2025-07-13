n,d=map(int,input().split())
li=list(map(int,input().split()))
li.sort(reverse="True")
s=0
for i in range(d):
    s=s+li[i]
print(s)
