nums = [10,20,50,90,65]
largest = nums[0]

for ele in nums:
    if ele > largest:
        largest = ele
print(largest)

nums.sort()
print(nums)