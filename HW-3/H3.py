n = int(input())
pos = []
for i in range(n):
    pos.append(str(input()))

prefix = []
cur_sum = 0
stack = []
for i in pos:
    if i[0] == "+":
        value = int(i[1:])
        stack.append(value)
        cur_sum += value
    elif i[0] == "-":
        if stack:
            cur_sum -= stack.pop()

    prefix.append(cur_sum)

for i in range(n):
    if pos[i][0] != "+":
        prefix[i] = 0


prefix = [0] + list(filter(lambda x: x != 0, prefix))
stack = []

for i in range(len(pos)):

    if pos[i][0] == "+":
        stack.append(int(pos[i][1:]))

    if pos[i][0] == "?":
        print(prefix[len(stack)] - prefix[len(stack)-int(pos[i][1:])])

    if pos[i][0] == "-":
        print(stack.pop())
        prefix.pop(len(stack)+1)