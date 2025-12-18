list_n = list(map(str, input().split()))

stack = []
nun_list = "+-*"
res = 0

for i in range(len(list_n)):
    if list_n[i] not in nun_list:
        stack.append(list_n[i])

    if list_n[i] == '+':
        res = int(stack[-1]) + int(stack[-2])
        stack.pop()
        stack.pop()
        stack.append(res)

    elif list_n[i] == '-':
        res = int(stack[-2]) - int(stack[-1])
        stack.pop()
        stack.pop()
        stack.append(res)

    elif list_n[i] == '*':
        res = int(stack[-1]) * int(stack[-2])
        stack.pop()
        stack.pop()
        stack.append(res)

print(stack[0])