n=int(input())
l=[]
r=0
stack=[]
a=0
for i in range(n):
    l.append(list(map(str,input().split())))
    max_iter = 10000  # avoid infinite loops
i=0
while (i<n):
    if l[i][0]=='PUSH':
        stack.append(int(l[i][1]))
    elif l[i][0]=='STORE':
        r=stack[-1]
        stack.pop()
    elif l[i][0]=='LOAD':
        stack.append(r)
    elif l[i][0]=='PLUS':
        if len(stack)>=2:
            a=stack[-1]+stack[-2]
            stack.pop()
            stack.pop()
            stack.append(a)
    elif l[i][0]=='TIMES':
        if len(stack)>=2:
            a=stack[-1]*stack[-2]
            stack.pop()
            stack.pop()
            stack.append(a)
    elif l[i][0]=='IFZERO':
        if stack[-1]==0:
            i=int(l[i][1])
            stack.pop()
            continue
        stack.pop()
    elif l[i][0]=='DONE':
        break
    i+=1
print(stack[-1])
