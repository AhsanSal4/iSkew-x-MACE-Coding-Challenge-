n=int(input())
li=[]
stack=[]
for i in range(n):
    li.append(list(map(int,input().split())))
stack.append(li[0])
for i in range(1,n):
    if (abs((stack[-1][0]-li[i][0]))<=(stack[-1][1]-li[i][1])):
        continue
    elif (abs(li[i][0]-stack[-1][0])<=(li[i][1]-stack[-1][1])):
        stack.pop()
        stack.append(li[i])
    else:
        stack.append(li[i])
print(len(stack))
