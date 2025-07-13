n=int(input())
day=list(map(int,input().split()))
night=list(map(int,input().split()))
mi=int(input())
a=0
day.sort()
night.sort(reverse=True)
for i in range(n):
    day[i]=day[i]+night[i]
    if day[i]>mi:
        a=a+(day[i]-mi)
print(a*100)
