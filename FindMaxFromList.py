nums = [4,2,1,0,3,7,9,6,5,8]

max_num = nums[0]
for num in nums:
    if num > max_num:
        max_num = num

print(f"The maximum number in the list is: {max_num}")