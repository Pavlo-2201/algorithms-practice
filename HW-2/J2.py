n = int(input())
a = list(map(int, input().split()))
m, k = map(int, input().split())
x = list(map(int, input().split()))

prefix = [0] * n
prefix[0] = 1

for i in range(n-1,0,-1):
    if a[i] > a[i-1]:
        prefix[i] = 0
    elif a[i] == a[i-1]:
        prefix[i] = -1
    else:
        prefix[i] = 1

k_arr = [0]*n

for i in range(n):
    if prefix[i] == 1:
        k_arr[i] = k
    else:
        k_arr[i] += k_arr[i-1] + prefix[i]
current_k = k
list = [0] * n
pre_ind = 0

for i in range(n):
    if prefix[i] == 1:
        list[i] = i+1
        current_k = k
        pre_ind = i


    else:
        current_k = k_arr[i]
        if current_k >= 0:
            list[i] = pre_ind + 1

        if current_k < 0:
            if prefix[i]== -1:
                pre_ind +=1
            while prefix[pre_ind] != -1:
                pre_ind +=1

            list[i] = pre_ind + 1

answer = []
for i in x:
    answer.append(list[i-1])
print(' '.join(map(str, answer)))