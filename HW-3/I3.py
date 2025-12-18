from collections import deque


num_ways = int(input())
priority_start, priority_end = map(int, input().split())

way_priority = {1: 1, 2: 1, 3: 1, 4: 1}
priority_range = [1, 2, 3, 4]
lower, higher = min(priority_start, priority_end), max(priority_start, priority_end)

if higher - lower == 2:
    way_priority[lower] -= 1
    way_priority[higher] -= 1
else:
    boss = lower if higher - lower == 1 else higher
    priority_value = 1
    for i in range(boss, boss + 4):
        way_priority[priority_range[(i - 1) % 4]] = priority_value
        priority_value += 1

queue1, queue2, queue3, queue4 = [], [], [], []
for i in range(num_ways):
    direction, time = map(int, input().split())
    if direction == 1:
        queue1.append((time, direction, i))
    elif direction == 2:
        queue2.append((time, direction, i))
    elif direction == 3:
        queue3.append((time, direction, i))
    elif direction == 4:
        queue4.append((time, direction, i))

queue1.sort(key=lambda x: (x[0], way_priority[x[1]]))
queue2.sort(key=lambda x: (x[0], way_priority[x[1]]))
queue3.sort(key=lambda x: (x[0], way_priority[x[1]]))
queue4.sort(key=lambda x: (x[0], way_priority[x[1]]))

queue1 = deque(queue1)
queue2 = deque(queue2)
queue3 = deque(queue3)
queue4 = deque(queue4)

results = [0] * num_ways
current_time = 0
no_candidate = (float('inf'), float('inf'), float('inf'))
while queue1 or queue2 or queue3 or queue4:
    candidates = [
        queue1[0] if queue1 else no_candidate,
        queue2[0] if queue2 else no_candidate,
        queue3[0] if queue3 else no_candidate,
        queue4[0] if queue4 else no_candidate
    ]


    if current_time < min(candidates[0][0], candidates[1][0], candidates[2][0], candidates[3][0]):
        current_time = min(candidates[0][0], candidates[1][0], candidates[2][0], candidates[3][0])


    min_priority = 5
    for i in range(4):
        if current_time >= candidates[i][0]:
            min_priority = min(min_priority, way_priority[candidates[i][1]])


    for i in range(4):
        if current_time >= candidates[i][0] and way_priority[candidates[i][1]] <= min_priority:
            results[candidates[i][2]] = current_time
            if i == 0:
                queue1.popleft()
            elif i == 1:
                queue2.popleft()
            elif i == 2:
                queue3.popleft()
            elif i == 3:
                queue4.popleft()

    current_time += 1

for res in results:
    print(res)