list_n = list(map(str, str(input())))

check_str = "0123456789()+-* "
wrong_check = False
for i in range(len(list_n)):
    if list_n[i] not in check_str:
        wrong_check = True
        break
str = ''.join(list_n)
if "(-" in str or "(+" in str or "(*" in str:
    wrong_check = True

stack = []
check = False
count = 0
for i in list_n:
    if i == "(":
        stack.append(i)
    elif i == ")":
        if not stack:
            check = True
            break
        stack.pop()

wrong2_check = False
if stack or (not stack and check) or wrong_check:
    wrong2_check = True
    print("WRONG")


stack = []

dict = {'+': 1, '-': 1, '*': 2}
postfix = []
i = 0
if not wrong_check and not wrong2_check:
    while i < len(list_n):
        char = list_n[i]
        if char.isdigit():
            num = char
            i += 1

            while i < len(list_n) and list_n[i].isdigit():
                num += list_n[i]
                i += 1
            postfix.append(num)
            continue
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        elif char in dict:

            while stack and stack[-1] != '(' and dict[stack[-1]] >= dict[char]:
                postfix.append(stack.pop())
            stack.append(char)
        i+=1

while stack:
    postfix.append(stack.pop())
tr = False
stack = []
nun_list = "+-*"
res = 0
if not wrong_check and not wrong2_check:
    try:
        for i in range(len(postfix)):
            if postfix[i] not in nun_list:
                stack.append(int(postfix[i]))

            if postfix[i] == '+':
                res = int(stack[-1]) + int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(res)
            elif postfix[i] == '-':
                res = int(stack[-2]) - int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(res)
            elif postfix[i] == '*':
                res = int(stack[-1]) * int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(res)
    except (IndexError, ValueError) as e:
        print("WRONG")
        tr = True

if len(stack) == 1 and not wrong2_check and not wrong_check and not tr:
    print(stack[0])
elif not wrong2_check and not wrong_check and not tr:
    print("WRONG")