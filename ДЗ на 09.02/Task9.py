nums = [7, 1, 3, 4, 3, 9, 14, -5, -17, -13, -19, -18]
i = 0
sum = 0
while i < len(nums):
    if nums[i] < 0:
        sum+=nums[i]
    i+=1
print(sum)