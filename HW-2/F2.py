n = int(input())
nums = list(map(int, input().split()))
nums.sort()

sum2 = nums[-1] * nums[-2] * nums[-3]
current_sum = 0
suffix_sums = [0] * (len(nums)+1)

for i in range(len(nums) - 1, -1, -1):
    suffix_sums[i] = current_sum
    current_sum += nums[i]



sum_t = 0
sum_tt = []
for i in range(1,len(nums)):
    sum_t+=(nums[i]*suffix_sums[i])
    sum_tt.append(sum_t)
sum_tt.sort()

new_arr = []

for i in range(len(sum_tt)-1):
    new_arr.append(sum_tt[i+1]-sum_tt[i])


for i in range(len(nums) - 3):

    sum2 += nums[i]*sum_tt[-1]
    if i >= 1:
        sum_tt[-1] -= new_arr[i-1]
    else:
        sum_tt[-1] -= sum_tt[i]
print(sum2 % (10**9+7))