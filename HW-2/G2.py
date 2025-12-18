n, k = list(map(int, input().split()))

str = list(map(str, input()))
first = last = count_a = count_b = rough = max_len = 0

while last < n:
    if str[last] == 'a':
        count_a += 1
    elif str[last] == 'b':
        count_b += 1
        rough += count_a

    while rough > k:
        if str[first] == 'a':
            count_a -= 1
            rough -= count_b
        elif str[first] == 'b':
            count_b -= 1
        first += 1

    max_len = max(max_len, last - first + 1)

    last += 1

print(max_len)