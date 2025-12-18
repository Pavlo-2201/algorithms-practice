seq = str(input())
stack = []
check = False
for i in seq:
    if i == '(' or i == '[' or i == '{':
        stack.append(i)
    elif len(stack) == 0:
        check = True
        break
    elif (i == ')' and stack[-1] == '(') or (i == ']' and stack[-1] == '[') or (i == '}' and stack[-1] == '{'):
        stack.pop()
    else:
        check = True
        break

if not check and len(stack) == 0:
    print("yes")
else:
    print("no")