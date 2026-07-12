nums = [1,2,3,3,3,4,4,5,6,7,8,8,9,9]

#def duplicates(nums):
#   return [i for i in nums if nums.count(i) > 1]

#print(duplicates(nums))  

def duplicates(nums):
    seen = set()
    duplicates = set()

    for i in nums:
        if i in seen:
            duplicates.add(i)
        else:
            seen.add(i)
    return list(duplicates)   

print(duplicates(nums))