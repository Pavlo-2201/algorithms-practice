n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
p = list(map(int, input().split()))

algorithms = [(i+1,a[i],b[i]) for i in range(n)]

sorted_by_interest = sorted(algorithms, key=lambda x: (-x[1], -x[2], x[0]))
sorted_by_usefullness = sorted(algorithms, key=lambda x: (-x[2], -x[1], x[0]))

interest_point = 0
usefullness_point = 0
used = set()
result = []

for mood in p:
    if mood == 1:
        while sorted_by_usefullness[usefullness_point][0] in used:
            usefullness_point += 1
        chosen_algo = sorted_by_usefullness[usefullness_point]

    else:
        while sorted_by_interest[interest_point][0] in used:
            interest_point += 1
        chosen_algo = sorted_by_interest[interest_point]

    result.append(chosen_algo[0])
    used.add(chosen_algo[0])

print(" ".join(map(str, result)))