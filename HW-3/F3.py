n = int(input())
w = list(map(str, input()))
s = list(map(str, input()))

pairs = {'(': ')', '[': ']', ')': '(', ']': '['}
dictC = {value: ind for ind,value in enumerate(w)}
res = s.copy()
stack = []
for i in s:
    if i == '(' or i == '[':
        stack.append(i)
    elif len(stack) == 0:
        break
    elif (i == ')' and stack[-1] == '(') or (i == ']' and stack[-1] == '['):
        stack.pop()
    else:
        break

while len(res) < n:
    if len(stack) == 0:
        if dictC['('] < dictC['[']:
            res += '('
            stack.append(res[-1])
        else:
            res += '['
            stack.append(res[-1])


    if len(stack) == n - len(res):
        res += pairs[stack.pop()]

    else:

        if stack[-1] == '(':
            if dictC['('] < dictC['[']:
                res += '('
                stack.append(res[-1])

            else:
                res+='['
                stack.append(res[-1])

            if dictC[res[-1]] > dictC[')']:
                res[-1] = ')'
                stack.pop()
                stack.pop()

        else:
            if dictC['['] < dictC['(']:
                res+='['
                stack.append(res[-1])

            else:
                res+='('
                stack.append(res[-1])

            if dictC[res[-1]] > dictC[']']:
                res[-1] = ']'
                stack.pop()
                stack.pop()



print(''.join(res))