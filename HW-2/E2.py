n = int(input())
nums = list(map(int, input().split()))
nums.sort()
new_list = []
while n > 0:
    if len(nums) % 2 != 0:
        new_list.append(nums.pop(n//2))
        n-=1
    if len(nums) == 0:
        break
    if len(nums) % 2 == 0:
        if nums[n//2] < nums[n//2 -1]:
            new_list.append(nums.pop(n // 2))
            n-=1
        elif nums[n//2] > nums[n//2 -1]:
            new_list.append(nums.pop(n // 2 - 1))
            n -= 1
        else:
            new_list.append(nums.pop(n // 2))
            n -= 1

print(" ".join(map(str, new_list)))