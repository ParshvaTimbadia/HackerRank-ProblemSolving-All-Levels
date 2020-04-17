#Problem Statment: https://www.hackerrank.com/challenges/maximum-element/problem

index = int(input())
stack, stackMax = [], []
for _ in range(index):
    x, *b = map(int,input().split())
    if x == 1:
        stack.append(b)
        if not stackMax:
            stackMax.append(b)
        else:
            if b < stackMax[-1]:
                stackMax.append(stackMax[-1])
            else:
                stackMax.append(b)
    elif x == 2:
        stack.pop()
        stackMax.pop()
    else:
        print(*stackMax[-1])
        
